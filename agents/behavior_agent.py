def learn_behavior(df):
    behavior = {
        "avg_amount": df['Amount'].mean(),
        "common_vendors": df['Vendor'].value_counts().head(3).index.tolist(),
        "common_hours": df['Hour'].value_counts().head(5).index.tolist()
    }
    return behavior