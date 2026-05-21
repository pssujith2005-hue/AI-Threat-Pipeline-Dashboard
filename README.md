# AI-Powered Security Operations Center (SOC) Analytics Dashboard

An end-to-end data engineering and security analytics pipeline built to ingest, log, and visualize automated network threats. This project demonstrates how raw security database logs can be transformed into actionable visual threat intelligence.

## ⚙️ Project Architecture
1. **Automation Layer (Python):** Simulates standard security threat logs and updates the relational model features.
2. **Storage Layer (SQLite):** Main local data vault (`cybersecurity_vault.db`) storing transactional log records.
3. **Analytics Layer (Power BI):** Direct structural data ingestion to map trend metrics and enterprise asset vulnerabilities.

## 📊 Core Insights Tracked
* **Time-Series Anomalies:** A severe metric spike identified at **4:00 AM**, standard operational behavior indicating automated brute-force or botnet activities.
* **Asset Blast Radius:** The dynamic donut chart reveals that **Servers (20.9%)** and **Workstations (20.7%)** are highly prioritized by current threat actors.
