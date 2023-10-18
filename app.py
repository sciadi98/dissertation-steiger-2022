import glob
import json
import os
import pickle
import pandas as pd

CATEGORIES_FOR_COLS = {
    "shape": ["D", "indeterminate", "E"],
    "profile_entrance": ["I/", "V"],
    "profile_exit": ["I/", "V"],
    "rising_entrance": ["absent", "bilateral", "single"],
    "rising_exit": ["absent", "single", "bilateral"],
    "shards": ["absent", "present"],
    "feathering": ["absent", "present"],
    "entrance_mounding": ["absent", "single", "bilateral"],
    "center_mounding": ["absent", "single", "bilateral"],
    "exit_mounding": ["absent", "single", "bilateral"],
    "mounding": ["absent", "not marked", "marked"],
}


def display_model_list(model_list):
    """Show which models are available"""
    for index, name in enumerate(model_list):
        print(f"{index + 1}. {name}")


def choose_model(model_list):
    """User can choose the model"""
    choosen_index = input("What model do you want to use? ")
    return model_list[int(choosen_index) - 1]


def load_metadata(model_file):
    model_file_no_extension = os.path.splitext(model_file)[0]
    metadata_file = model_file_no_extension + ".json"
    with open(metadata_file, "r") as f:
        return json.load(f)


def load_model(model_file):
    """Import the model choosen"""
    with open(model_file, "rb") as f:
        return pickle.load(f)


def prepare_dataset(dataset_file, input_cols):
    """Load a dataset and select the provided columns."""

    # Load data
    df = pd.read_excel(dataset_file)

    # Filter bad data, replace categories with dummies
    x_df = df[input_cols].apply(lambda x: x.str.strip())

    # Convert df values to categorical to account for missing values
    for col in x_df.columns:
        x_df[col] = df[col].astype(pd.CategoricalDtype(categories=CATEGORIES_FOR_COLS[col], ordered=True))

    x = pd.get_dummies(x_df, drop_first=True, sparse=True)
    return x


def main():
    """Define the main function"""
    model_list = glob.glob("models/*.pickle")
    display_model_list(model_list)

    model_file = choose_model(model_list)

    metadata = load_metadata(model_file)
    model = load_model(model_file)
    choosen_dataset = input("What dataset do you want to use? ")

    print(choosen_dataset)
    dataset = prepare_dataset(choosen_dataset, metadata["input_cols"])
    # reorder columns according to models
    dataset = dataset[model.feature_names_in_]

    print('Model features:')
    print(model.feature_names_in_)
    print('Dataset columns:')
    print(dataset.columns)

    result = model.predict(dataset)
    print(result)


# Call main function
if __name__ == "__main__":
    main()
