import streamlit as st
import pandas as pd
import random

from agents.behavior_agent import learn_behavior
from agents.detection_agent import detect_anomalies
from agents.explanation_agent import generate_explanation

st.set_page_config(page_title="AI Audit System", layout="wide")

st.title("Behavior-Based Intelligent Audit Assistant")

# -------------------------------
# FILE UPLOAD
# -------------------------------
st.sidebar.header("Upload Data")

file = st.sidebar.file_uploader("Upload Transactions CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
else:
    df = pd.read_csv("data/transactions.csv")

# -------------------------------
# PREPROCESSING
# -------------------------------
df['Hour'] = pd.to_datetime(df['Date']).dt.hour

# -------------------------------
# AGENT WORKFLOW
# -------------------------------
behavior = learn_behavior(df)
df = detect_anomalies(df)

# -------------------------------
# RISK LEVEL (UPDATED)
# -------------------------------
df['confidence'] = df['risk_score'].apply(
    lambda x: "High Risk" if x >= 70 else ("Moderate" if x >= 40 else "Normal")
)
df.rename(columns={"confidence": "Risk Level"}, inplace=True)
# -------------------------------
# EXPLANATION
# -------------------------------
df['Explanation'] = df.apply(
    lambda row: generate_explanation(row, behavior), axis=1
)

# -------------------------------
# METRICS
# -------------------------------
col1, col2 = st.columns(2)

col1.metric("Total Transactions", len(df))
col2.metric("Anomalies Detected", int(df['anomaly_flag'].sum()))

# -------------------------------
# BUSINESS INSIGHTS
# -------------------------------
st.subheader("📊 Risk Insights")

anomalies_df = df[df['anomaly_flag'] == 1]

if not anomalies_df.empty:
    risk_vendors = anomalies_df['Vendor'].value_counts()

    st.write("### ⚠️ High Risk Vendors")
    st.write(risk_vendors)

    st.write(f"🔴 {len(anomalies_df)} risky transactions detected out of {len(df)}")
else:
    st.success("No anomalies detected")
st.info("System automatically prioritizes high-risk transactions for audit review using behavior-based analysis.")
# -------------------------------
# 🔥 KEY OBSERVATIONS (UPGRADED)
# -------------------------------
st.subheader("🔍 Key Observations")

total = len(df)
anomalies = df['anomaly_flag'].sum()
high_risk = df[df['risk_score'] > 70]
vendors_list = anomalies_df['Vendor'].unique()

if total > 0:
    st.markdown(f"""
- {round((anomalies/total)*100, 1)}% of transactions are flagged as anomalous  
- Risk concentration identified in non-recurring vendors (e.g., {', '.join(vendors_list) if len(vendors_list) > 0 else "None"})  
- Primary risk driver identified: abnormal transaction magnitude relative to learned behavior  
- {len(high_risk)} transaction{'s' if len(high_risk) != 1 else ''} classified as high-risk requiring audit attention  
""")

# -------------------------------
# 🔥 RISK DISTRIBUTION (FIXED)
# -------------------------------
st.subheader("📊 Transaction Risk Distribution")
st.write("Risk Category vs Number of Transactions")

risk_counts = df['Risk Level'].value_counts()
st.bar_chart(risk_counts)

st.caption("Risk score is computed based on weighted deviation across transaction amount, vendor familiarity, and transaction timing.")
st.caption("Higher scores indicate stronger deviation from learned behavioral patterns.")
# -------------------------------
# SORT DATA
# -------------------------------
df_sorted = df.sort_values(by="risk_score", ascending=False)

# -------------------------------
# HIGHLIGHT ANOMALIES (RESTORED)
# -------------------------------
def highlight(row):
    if row['anomaly_flag'] == 1:
        return ['background-color: #ff4b4b'] * len(row)
    return [''] * len(row)

# -------------------------------
# DISPLAY TABLE (FIXED)
# -------------------------------
st.subheader("📄 Transaction Analysis")

display_df = df_sorted[['Date','Vendor','Amount','risk_score','Risk Level','Explanation']]

st.dataframe(
    display_df,
    use_container_width=True
)

# -------------------------------
# DOWNLOAD REPORT
# -------------------------------
st.download_button(
    label="📥 Download Audit Report",
    data=df_sorted.to_csv(index=False),
    file_name="audit_report.csv",
    mime="text/csv"
)

# -------------------------------
# SYSTEM WORKFLOW
# -------------------------------
st.subheader("⚙️ System Workflow")

st.markdown("""
1. **Data Agent** → Processes transaction data  
2. **Behavior Agent** → Learns normal patterns  
3. **Detection Agent** → Identifies anomalies  
4. **Explanation Agent** → Explains risks  
5. **Report Agent** → Generates insights  
""")

# -------------------------------
# 🔥 AUDIT DECISION (UPGRADED)
# -------------------------------
st.subheader("📌 Audit Decision")

if len(anomalies_df) > 0:
    st.error("Immediate audit intervention is recommended for identified high-risk transactions due to significant behavioral deviations.")
else:
    st.success("No high-risk transactions detected. Current activity aligns with expected behavioral patterns.")

# -------------------------------
# AI AUDIT SUMMARY
# -------------------------------
st.subheader("🧾 AI Audit Summary")

if st.button("Generate Audit Summary"):
    total = len(df)
    anomalies = int(df['anomaly_flag'].sum())
    vendors = df[df['anomaly_flag'] == 1]['Vendor'].unique()

    risk_level = "Low"
    if anomalies > 0:
        risk_level = "Moderate"
    if anomalies > 3:
        risk_level = "High"

    summary = f"""
🔍 Risk Assessment:
- Total Transactions Analyzed: {total}
- Anomalies Detected: {anomalies}
- Overall Risk Level: {risk_level}

⚠️ Key Risk Indicators:
- Significant deviation in transaction amounts from learned behavior
- Presence of non-regular vendors: {', '.join(vendors) if len(vendors) > 0 else "None"}

📉 Business Impact:
- Potential financial discrepancies and fraud exposure
- Weak control over vendor validation processes

✅ Recommended Actions:
- Conduct immediate audit of flagged transactions
- Implement vendor verification mechanisms
- Enable continuous monitoring using intelligent audit systems
"""

    st.success(summary)