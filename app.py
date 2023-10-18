import os
import pickle
import pandas as pd

def display_model_list(model_list):
    """Show which models are available"""
    for index, name in enumerate(model_list):
        print(f"{index + 1}. {name}")


def choose_model(model_list):
    """User can choose the model"""
    choosen_index = input("What model do you want to use? ")
    return model_list[int(choosen_index) - 1]


def load_model(model_file):
    """Import the model choosen"""
    with open(model_file, "rb") as f:
        return pickle.load(f)

def prepare_dataset(dataset_file, input_cols, result_col=None):
    """Load a dataset and select the provided columns (w/ optional result column)."""
    # Load data
    df = pd.read_excel(dataset_file)

    # Filter bad data, replace categories with dummies
    x_df = df[input_cols].apply(lambda x: x.str.strip())
    x = pd.get_dummies(x_df, drop_first=True)

    return x

def main():
    """Define the main function"""
    model_list = os.listdir(
        "models"
    )
    display_model_list(model_list)
    model_file = choose_model(model_list)
    model = load_model(model_file)


# Call main function
if __name__ == "__main__":
    main()
