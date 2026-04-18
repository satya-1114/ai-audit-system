def detect_anomalies(df):
    threshold = df['Amount'].mean() * 2

    anomaly_flags = []
    scores = []

    for _, row in df.iterrows():
        score = 0

        # Amount impact (0–50)
        if row['Amount'] > threshold:
            score += min(50, int((row['Amount'] / threshold) * 25))

        # Vendor impact (0–30)
        if row['Vendor'] not in df['Vendor'].value_counts().head(3).index:
            score += 30

        # Time impact (0–20)
        if row['Hour'] < 6 or row['Hour'] > 22:
            score += 20

        scores.append(score)

        # Flag anomaly
        anomaly_flags.append(1 if score >= 50 else 0)

    df['risk_score'] = scores
    df['anomaly_flag'] = anomaly_flags

    return df