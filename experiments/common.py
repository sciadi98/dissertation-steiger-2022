# Imports and global options
import itertools

import pandas as pd
from sklearn.linear_model import LogisticRegression


def prepare_dataset(dataset_file, input_cols, result_col=None):
    """Load a dataset and select the provided columns (w/ optional result column)."""
    # Load data
    df = pd.read_excel(dataset_file)

    # Filter bad data, replace categories with dummies
    x_df = df[input_cols].apply(lambda x: x.str.strip())
    x = pd.get_dummies(x_df, drop_first=True)

    if result_col:
        y_df = df[result_col].str.strip()
        y = pd.get_dummies(y_df, drop_first=True).iloc[:, 0]

        return x, y
    else:
        return x


def display_input_data(dataset_file, input_cols):
    """Display data and dummies in a table."""
    x = prepare_dataset(dataset_file, input_cols)
    display(x)


def check_input_data_indices(train_dataset_file, test_dataset_file, input_cols):
    """Check train and test dataset for compatibility, i.e. checks whether the provided input columns are present on both"""
    x_train = prepare_dataset(train_dataset_file, input_cols)
    x_test = prepare_dataset(test_dataset_file, input_cols)

    if not x_train.columns.equals(x_test.columns):
        raise Exception('Datasets are incompatible!');
    print('Datasets are compatible')


def train_model(train_dataset_file, input_cols, result_col):
    """Create a logistic regression model on the provided dataset (including an expected result column) and fits/trains it on the result column."""
    x, y = prepare_dataset(train_dataset_file, input_cols, result_col)

    # Instantiate the model
    model = LogisticRegression(solver='liblinear', random_state=0)

    # Train (=fit) the model
    model.fit(x, y)

    return model


def evaluate_model(model, test_dataset_file, input_cols, result_col):
    """Evaluate the provided model on the given test dataset, printing its score."""
    x, y = prepare_dataset(test_dataset_file, input_cols, result_col)

    return model.score(x, y)


def _evaluate_for_input_combination(train_dataset_file, test_dataset_file, input_combination, result_col):
    # print(input_cols_comb)
    model = train_model(
        train_dataset_file,
        list(input_combination),
        result_col
    )
    score = evaluate_model(
        model,
        test_dataset_file,
        list(input_combination),
        result_col
    )
    # print(score)
    return score, model


def run_input_optimizer(train_dataset_file, test_dataset_file, input_cols, result_col):
    """Finds the best and worst combination of columns and their corresponding scores by brute force (by trying all
    the combinations)."""

    # Contains all combinations by input length (3D list)
    input_combinations = []
    for l in range(2, len(input_cols) + 1):
        input_combinations.append(list(itertools.combinations(input_cols, l)))

    scores = []
    models = []
    flat_input_combinations = []

    for input_combinations_of_len in input_combinations:
        print('Testing combinations of length ' + str(len(input_combinations_of_len[0])))

        for input_combination in input_combinations_of_len:
            score, model = _evaluate_for_input_combination(train_dataset_file, test_dataset_file, input_combination,
                                                           result_col)
            scores.append(score)
            models.append(model)
            flat_input_combinations.append(input_combination)

    # Pick and print results
    max_score = max(scores)
    max_score_idx = scores.index(max_score)
    max_score_cols = flat_input_combinations[max_score_idx]
    max_score_model = models[max_score_idx]

    min_score = min(scores)
    min_score_idx = scores.index(min_score)
    min_score_cols = flat_input_combinations[min_score_idx]
    min_score_model = models[min_score_idx]

    return {
        'max_score': max_score,
        'max_score_cols': max_score_cols,
        'max_score_model': max_score_model,
        'min_score': min_score,
        'min_score_cols': min_score_cols,
        'min_score_model': min_score_model
    }


def calculate_accuracy(df):
    tot_corr = 0
    for index, row in df.iterrows():
        if row["result"] == row["expected_result"]:
            tot_corr += 1
    tot = len(df)

    accuracy_perc = (tot_corr / tot) * 100
    return accuracy_perc


def calculate_error_rate(df):
    return 100 - calculate_accuracy(df)
