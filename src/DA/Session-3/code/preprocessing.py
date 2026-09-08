import pandas as pd
def drop_columns(df : pd.DataFrame, columns : list) -> pd.DataFrame:
    """
    Drops specified columns from the DataFrame.

    Parameters:
    df (pd.DataFrame): The input DataFrame.
    columns (list): List of column names to drop.

    Returns:
    pd.DataFrame: DataFrame with specified columns dropped.
    """
    return df.drop(columns=columns)

def get_type_info(df):
    return pd.DataFrame({'dtypes': df.dtypes, 'unique': df.nunique()}).T