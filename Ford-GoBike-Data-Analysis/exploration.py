def explore_data(df):
    """Explore the GoBike dataset."""
    print("Dataset shape:")
    print(df.shape)
    print("\nMissing values:")
    print(df.isnull().sum())
    print("\nDuplicate rows:")
    print(df.duplicated().sum())
    print("\nUser types:")
    print(df["user_type"].value_counts())
    print("\nMember genders:")
    print(df["member_gender"].value_counts())
    print("\nBike share for all trips:")
    print(df["bike_share_for_all_trip"].value_counts())