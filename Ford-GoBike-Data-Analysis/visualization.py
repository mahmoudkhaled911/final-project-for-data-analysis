import matplotlib.pyplot as plt
import seaborn as sns
def plot_user_type_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="user_type")
    plt.title("Distribution of User Types")
    plt.xlabel("User Type")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.show()
def plot_bike_share_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="bike_share_for_all_trip")
    plt.title("Distribution of Bike Share for All Trips")
    plt.xlabel("Bike Share for All")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.show()
def plot_age_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="age", bins=30)
    plt.title("Distribution of Users' Ages")
    plt.xlabel("Age")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.show()
def plot_age_outliers(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="age")
    plt.title("Age Outliers")
    plt.xlabel("Age")
    plt.tight_layout()
    plt.show()
def plot_trip_duration_minutes(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="duration_min", bins=50)
    plt.title("Distribution of Trip Duration")
    plt.xlabel("Trip Duration (Minutes)")
    plt.ylabel("Number of Trips")
    plt.xlim(0, 60)
    plt.tight_layout()
    plt.show()
def plot_gender_distribution(df):
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="member_gender")
    plt.title("Distribution of Member Gender")
    plt.xlabel("Gender")
    plt.ylabel("Number of Trips")
    plt.tight_layout()
    plt.show()
def plot_trip_duration_hours(df):
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x="duration_hour", bins=50)
    plt.title("Distribution of Trip Duration in Hours")
    plt.xlabel("Trip Duration (Hours)")
    plt.ylabel("Number of Trips")
    plt.xlim(0, 1)
    plt.tight_layout()
    plt.show()
def plot_average_duration_by_user_type(df):
    average_duration = (
        df.groupby("user_type")["duration_min"]
        .mean()
        .reset_index()
    )
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=average_duration,
        x="user_type",
        y="duration_min"
    )
    plt.title("Average Trip Duration by User Type")
    plt.xlabel("User Type")
    plt.ylabel("Average Trip Duration (Minutes)")
    plt.tight_layout()
    plt.show()
def plot_duration_by_gender(df):
    average_duration = (
        df.groupby("member_gender")["duration_min"]
        .mean()
        .reset_index()
    )
    plt.figure(figsize=(8, 5))
    sns.barplot(
        data=average_duration,
        x="member_gender",
        y="duration_min"
    )
    plt.title("Average Trip Duration by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Average Trip Duration (Minutes)")
    plt.tight_layout()
    plt.show()
def plot_duration_by_user_type(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="user_type",
        y="duration_min"
    )
    plt.title("Trip Duration by User Type")
    plt.xlabel("User Type")
    plt.ylabel("Trip Duration (Minutes)")
    plt.ylim(0, 60)
    plt.tight_layout()
    plt.show()
def plot_age_by_user_type(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="user_type",
        y="age"
    )
    plt.title("Age Distribution by User Type")
    plt.xlabel("User Type")
    plt.ylabel("Age")
    plt.tight_layout()
    plt.show()
def plot_age_by_gender(df):
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="member_gender",
        y="age"
    )
    plt.title("Age Distribution by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Age")
    plt.tight_layout()
    plt.show()
def plot_correlation_matrix(df):
    numeric_columns = ["duration_sec","start_station_id","start_station_latitude","start_station_longitude"
        ,"end_station_id","end_station_latitude","end_station_longitude","bike_id","member_birth_year","age"]
    correlation = df[numeric_columns].corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm"
    )
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.show()
def plot_specific_correlations(df):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df.sample(min(5000, len(df)), random_state=42),
        x="age",
        y="duration_min"
    )
    plt.title("Age vs Trip Duration")
    plt.xlabel("Age")
    plt.ylabel("Trip Duration (Minutes)")
    plt.ylim(0, 60)
    plt.tight_layout()
    plt.show()
def plot_data_stat_correlations(df):
    data = df[["duration_sec","duration_min","duration_hour","age"]].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        data,
        annot=True,
        fmt=".2f",
        cmap="coolwarm"
    )
    plt.title("Correlation Between Data Statistics")
    plt.tight_layout()
    plt.show()