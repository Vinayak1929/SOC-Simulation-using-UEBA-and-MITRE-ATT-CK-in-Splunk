# SOC-Simulation-using-UEBA-and-MITRE-ATT-CK-in-Splunk

## 📌 Overview

This project simulates a real-time **Security Operations Center (SOC)** using Splunk. It detects abnormal user behavior through **User and Entity Behavior Analytics (UEBA)** and maps suspicious activities to the **MITRE ATT&CK framework** for threat classification.

The system uses a Python-based log generator to create real-time JSON logs, which are ingested into Splunk for analysis and visualization.

---

## 🚀 Features

* 📡 Real-time log generation using Python
* 🧠 UEBA-based anomaly detection
* 🎯 MITRE ATT&CK technique mapping
* 📊 Interactive Splunk dashboard
* 📈 Risk scoring and threat classification

---

## 🏗️ Architecture

Python Log Generator → JSON Logs → Splunk → UEBA Detection → MITRE Mapping → Dashboard

---

## 🧰 Technologies Used

* Splunk Enterprise (SIEM)
* Python
* JSON (log format)
* CSV (lookup table)
* SPL (Search Processing Language)

---

## 📁 Project Structure

```text
SOC-Splunk-Project/
├── data/
│   └── soc_logs.json
├── scripts/
│   └── log_generator.py
├── lookups/
│   └── mitre_lookup.csv
├── queries/
│   └── splunk_queries.txt
├── dashboards/
│   └── soc_monitoring_dashboard
├── README.md
```

---

## ▶️ How to Run

### 1️⃣ Run Log Generator

```bash
python scripts/log_generator.py
```

---

### 2️⃣ Ingest Data into Splunk

* Go to **Settings → Add Data → Monitor**
* Select `soc_logs.json`
* Set:

  * Sourcetype = `_json`
  * Index = `soc_logs`
  * Timestamp field = `timestamp`

---

### 3️⃣ Run Detection Query

```spl
index=soc_logs 
| eval hour=strftime(_time,"%H") 
| eventstats avg(hour) as avg_hour by user 
| eval risk_score=abs(hour-avg_hour)*10 
| lookup mitre_lookup.csv action OUTPUT technique_id technique_name
```

---

## 📊 Dashboard

The project includes a Splunk dashboard:

```text
dashboards/soc_monitoring_dashboard
```

This dashboard provides:

* Real-time event monitoring
* User risk analysis
* Threat classification
* MITRE ATT&CK mapping

---

## 📊 Dashboard Panels

* Total Events
* High Risk Users
* Detected Attacks
* Unique Users
* Activity Over Time
* Threat Level Distribution
* MITRE ATT&CK Mapping
* Active Threats
* High Risk Activity 
* Recent Events
  

---

## 🎯 MITRE ATT&CK Mapping

The system maps suspicious activities to MITRE ATT&CK techniques such as:

* T1110 – Brute Force
* T1059 – Command Execution
* T1005 – Data from Local System

---

## ⚠️ Challenges Faced

* Timestamp extraction issues
* Lookup configuration errors
* Real-time data ingestion debugging

---

## 🚀 Future Enhancements

* Machine learning-based anomaly detection
* Threat intelligence integration
* Automated incident response (SOAR)

---

## 👨‍💻 Author

Vinayak

---

## 📌 Keywords

Splunk, Cybersecurity, SOC, UEBA, MITRE ATT&CK, SIEM, Threat Detection
