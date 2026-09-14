import pandas as pd
def load_data(file_path):
    """Load the GoBike dataset from a CSV file."""
    return pd.read_csv(file_path)
def clean_data(df):
    """Clean and prepare the GoBike dataset."""
    df = df.drop_duplicates()
    df["duration_min"] = df["duration_sec"] / 60
    df["duration_hour"] = df["duration_sec"] / 3600
    df["age"] = 2019 - df["member_birth_year"]
    df.loc[(df["age"] > 100) | (df["age"] < 18), "age"] = pd.NA
    return df