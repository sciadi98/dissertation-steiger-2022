import glob
import json
import os
import pickle
import pandas as pd
import time

CONFIG_FILE = "config.json"


def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def display_model_list(model_list):
    """Show which models are available"""
    for index, name in enumerate(model_list):
        print(f"{index + 1}. {os.path.basename(name)}")


def choose_model(model_list):
    """User can choose the model"""

    # Loop until a valid index is provided
    chosen_index = None
    while True:
        chosen_index_str = input(
            f"What model do you want to use? [1-{len(model_list)}] "
        )

        try:
            chosen_index = int(chosen_index_str)
        except ValueError:
            print(
                f"Error: Invalid value provided, must be an integer between 1 and {len(model_list)}\n"
            )
            # Skip next check and loop
            continue

        if chosen_index < 1 or chosen_index > len(model_list):
            print(
                f"Error: Invalid index provided, must be between 1 and {len(model_list)}\n"
            )
        else:
            # Valid index was provided
            break

    chosen_model = model_list[chosen_index - 1]
    print(f"Using model {os.path.basename(chosen_model)}\n")

    return chosen_model


def load_metadata(model_file):
    model_file_no_extension = os.path.splitext(model_file)[0]
    metadata_file = model_file_no_extension + ".json"
    with open(metadata_file, "r") as f:
        return json.load(f)


def load_model(model_file):
    """Import the model chosen"""
    with open(model_file, "rb") as f:
        return pickle.load(f)


def choose_dataset():
    """User can choose the dataset"""

    # Loop until a valid value is found
    chosen_dataset = None
    while True:
        chosen_dataset = input("Enter the name/path of your dataset: ").strip()

        # Error handling
        if not os.path.isfile(chosen_dataset):
            print(
                f"Error: Provided file {chosen_dataset} does not exists, please provide a valid file path\n"
            )
        elif os.path.splitext(chosen_dataset)[1] != ".xlsx":
            print(
                f"Error: Invalid file type provided, this script only supports Excel workbooks (.xlsx extension)\n"
            )
        else:
            break

    print(f"Using dataset {chosen_dataset}\n")

    return chosen_dataset


def prepare_dataset(dataset_file, input_cols, categories_for_cols):
    """Load a dataset and select the provided columns."""

    # Load data
    df = pd.read_excel(dataset_file)

    # Filter bad data, replace categories with dummies
    x_df = df[input_cols].apply(lambda x: x.str.strip())

    # Convert df values to categorical to account for missing values
    for col in x_df.columns:
        x_df[col] = df[col].astype(
            pd.CategoricalDtype(categories=categories_for_cols[col])
        )

    x = pd.get_dummies(x_df, drop_first=True, sparse=True)
    return x, df


def display_classification_summary(
    model_file, model_metadata, dataset_file, dataset, raw_dataset
):
    print("Classification summary:")
    print(f"Model: {os.path.basename(model_file)}")
    print(f"Features: {', '.join(model_metadata['input_cols'])}")
    print(f"Dataset: {dataset_file}")
    print(f"Dataset preview:\n{raw_dataset.head()}\n")


def classify(model, dataset, result_conversion, raw_dataset):
    # reorder columns according to model
    dataset = dataset[model.feature_names_in_]

    # print('Model features:')
    # print(model.feature_names_in_)
    # print('Dataset columns:')
    # print(dataset.columns)

    result = model.predict(dataset)

    def convert_result(r: bool):
        return result_conversion[str(r)]

    converted_result = list(map(convert_result, result))
    return converted_result


def print_and_save_report(raw_df, converted_result):
    label = raw_df["label"]
    data = {"label": label, "result": converted_result}
    final_df = pd.DataFrame(data)

    print("Classification report: ")
    print(str(final_df) + "\n")

    timestamp = int(time.time())
    report_file = f"results/{timestamp}_report.xlsx"
    final_df.to_excel(excel_writer= report_file, na_rep="NA", index = False)
    print(f"The report is saved in {report_file}")


def main():
    """Define the main function"""

    config = load_config()

    model_list = glob.glob("models/*.pickle")
    display_model_list(model_list)

    model_file = choose_model(model_list)

    metadata = load_metadata(model_file)
    model = load_model(model_file)

    dataset_file = choose_dataset()

    dataset, raw_dataset = prepare_dataset(
        dataset_file, metadata["input_cols"], config["categories_for_cols"]
    )

    display_classification_summary(
        model_file, metadata, dataset_file, dataset, raw_dataset
    )

    converted_result = classify(
        model, dataset, metadata["result_conversion"], raw_dataset
    )

    print_and_save_report(raw_dataset, converted_result)


# Call main function
if __name__ == "__main__":
    main()
