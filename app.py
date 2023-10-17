import pickle
import os


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
