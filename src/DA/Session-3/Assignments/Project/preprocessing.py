import pandas as pd

def Check_data_type(df):
    """
    This function takes a pandas DataFrame as input
     returns a new DataFrame containing the data types and the number of unique values for each column in the input DataFrame.
    """
    return pd.DataFrame({'dtypes': df.dtypes, 'unique': df.nunique()}).T

def Read_data_file(file_path):
    """
    Reads a CSV file and returns a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: A DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        raise FileNotFoundError("The specified file was not found.")
    except pd.errors.EmptyDataError:
        raise pd.errors.EmptyDataError("The CSV file is empty.")

    return df

def Drop_unnecessary_features(df, columns_to_drop):
    """
    Drops specified columns from a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns_to_drop (list): A list of column names to drop.

    Returns:
    pd.DataFrame: A new DataFrame with the specified columns dropped.
    """
    return df.drop(columns=columns_to_drop, errors='ignore')