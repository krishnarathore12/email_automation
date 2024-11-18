def get_placeholders(df):
    columns = df.columns.tolist()

    # Generate placeholders for each column
    placeholders = [f"{{{col}}}" for col in columns]
    return placeholders