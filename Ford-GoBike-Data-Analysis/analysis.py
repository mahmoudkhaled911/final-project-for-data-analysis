def analyze_user_type_duration(df):
    """Calculate the average trip duration for each user type."""
    return df.groupby("user_type")["duration_sec"].mean()
def analyze_gender_duration(df):
    """Calculate the average trip duration for each gender."""
    return df.groupby("member_gender")["duration_sec"].mean()
def analyze_user_type_age(df):
    """Calculate the average age for each user type."""
    return df.groupby("user_type")["age"].mean()
def analyze_gender_age(df):
    """Calculate the average age for each gender."""
    return df.groupby("member_gender")["age"].mean()
def analyze_correlations(df):
    """Calculate correlations between numerical variables."""
    numeric_columns = ["duration_sec","start_station_id","start_station_latitude","start_station_longitude",
                      "end_station_id","end_station_latitude","end_station_longitude","bike_id","member_birth_year","age"]
    return df[numeric_columns].corr()
def analyze_specific_correlations(df):
    """Calculate correlation between age and trip duration."""
    return df[["age", "duration_min"]].corr()
def analyze_data_stat_correlations(df):
    """Calculate correlations between derived trip statistics."""
    columns = [
        "duration_sec",
        "duration_min",
        "duration_hour",
        "age"
    ]
    return df[columns].corr()