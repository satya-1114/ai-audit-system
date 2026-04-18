# 🔍 Behavior-Based Intelligent Audit Assistant

## 📌 Overview
The Behavior-Based Intelligent Audit Assistant is a lightweight, explainable AI-driven system designed to identify anomalous financial transactions and generate actionable audit insights.

Unlike traditional rule-based systems, this solution learns behavioral patterns from transaction data and detects deviations in real time, enabling efficient and intelligent audit decision-making.

---

## 🚀 Live Prototype
Access the deployed application:
👉 https://ai-audit-system-b3wmhejrdndqozwekyvcxe.streamlit.app/

The system demonstrates:
- Real-time anomaly detection
- Risk classification (High / Moderate / Normal)
- Automated audit insights generation
- Explainable reasoning for flagged transactions

---

## 🧪 Sample Dataset (For Testing)
To evaluate the system, use the sample dataset:

👉 https://raw.githubusercontent.com/your-username/your-repo/main/audit_test_dataset.csv

The dataset includes:
- Normal transactions across common vendors
- High-value transactions simulating anomalies
- Unfamiliar vendors to trigger risk detection
- Time-based variations for behavioral analysis

---

## 🧠 System Architecture
The system follows a modular, agent-based architecture:

1. **Data Preprocessing & Feature Engineering**
   - Data cleaning
   - Time feature extraction

2. **Behavior Learning Agent**
   - Learns normal transaction patterns
   - Identifies frequent vendors and spending behavior

3. **Anomaly Detection Agent**
   - Detects deviations from learned behavior
   - Flags suspicious transactions

4. **Explanation Agent**
   - Generates human-readable explanations
   - Provides contextual reasoning for risks

5. **Risk Scoring & Classification Engine**
   - Assigns risk levels (High / Moderate / Normal)

6. **Audit Dashboard**
   - Visualizes insights
   - Displays transaction-level analysis
   - Generates audit summaries

---

## 📊 Key Features
- ✅ Behavior-based anomaly detection (no hard-coded rules)
- ✅ Explainable AI (clear reasoning for every anomaly)
- ✅ Real-time audit insights
- ✅ Interactive dashboard (Streamlit)
- ✅ Risk prioritization for audit efficiency

---

## ⚙️ Tech Stack
- Python
- Pandas
- Streamlit
- Rule-based + statistical anomaly detection

---

## 📈 Example Output
The system provides:
- High-risk vendor identification
- Transaction-level risk classification
- Explanation for each flagged transaction
- Business impact and recommended actions

---

## 🔧 How to Run Locally

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
pip install -r requirements.txt
streamlit run app.py
