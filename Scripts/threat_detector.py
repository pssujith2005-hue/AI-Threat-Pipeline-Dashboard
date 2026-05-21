import pandas as pd
import numpy as np
import os

print("⏳ Initializing AI Threat Intelligence Engine...")

# 1. Load the raw network logs
input_path = "../Database/raw_network_logs.csv"
if not os.path.exists(input_path):
    print(f"❌ Error: Could not find raw log file at {input_path}. Please rerun Step 1!")
    exit()

df = pd.read_csv(input_path)
print(f"📂 Successfully loaded {len(df)} raw entries for inspection.")

# 2. Heuristic Feature Engineering & Threat Labeling Engine
# We evaluate the metrics to flag clear system anomalies
threat_scores = []
threat_labels = []

for idx, row in df.iterrows():
    attempts = row['LoginAttempts']
    data_mb = row['DataTransferred_MB']
    hour = row['AccessHour']
    
    # Calculate a custom risk metric score
    score = 0
    if attempts > 5:
        score += 4  # High login failure points (Brute force indicator)
    if data_mb > 500:
        score += 4  # High volume data movement points (Exfiltration indicator)
    if hour < 6 or hour > 20:
        score += 2  # Suspicious off-hours activity points
        
    # Classify the threat level context based on our calculated risk score
    if score >= 7:
        threat_scores.append(score)
        threat_labels.append("High Threat")
    elif score >= 4:
        threat_scores.append(score)
        threat_labels.append("Suspicious")
    else:
        threat_scores.append(score)
        threat_labels.append("Safe")

# 3. Inject the engineered AI metadata columns into our DataFrame
df['ThreatScore'] = threat_scores
df['ThreatLevel'] = threat_labels

# Print processing statistics directly to the terminal console
print("\n📊 Intelligence Threat Analysis Summary:")
print(df['ThreatLevel'].value_counts())

# 4. Save the finalized enriched security matrix
output_path = "../Database/enriched_security_logs.csv"
df.to_csv(output_path, index=False)
print(f"\n✅ Pipeline complete! Enriched dataset saved to: {output_path}")