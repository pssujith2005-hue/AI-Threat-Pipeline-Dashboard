import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

num_records = 5000
start_time = datetime(2026, 5, 1)

print("⏳ Generating 5,000 simulated network logs...")

# Generate structural data fields
log_ids = [100000 + i for i in range(num_records)]
timestamps = [start_time + timedelta(minutes=int(i * random.uniform(1, 5))) for i in range(num_records)]

# Mock target IP categories
ips = [f"192.168.1.{random.randint(1, 254)}" for _ in range(100)] + \
      [f"10.0.0.{random.randint(1, 254)}" for _ in range(50)] + \
      [f"203.0.113.{random.randint(1, 50)}" for _ in range(10)] # External malicious IPs

source_ips = [random.choice(ips) for _ in range(num_records)]
device_types = [random.choice(["Server", "Workstation", "Gateway", "IoT_Device"]) for _ in range(num_records)]

# Generate features with intentional anomaly behavior rules
login_attempts = []
data_transferred = []
access_hours = []

for i in range(num_records):
    hr = timestamps[i].hour
    access_hours.append(hr)
    
    # Baseline rules for a normal user pattern
    if hr >= 8 and hr <= 18:  # Business hours
        login_attempts.append(random.randint(1, 3))
        data_transferred.append(round(random.uniform(0.5, 50.0), 2))
    else: # Late night background traffic
        # 95% chance it's normal background automation
        if random.random() > 0.05:
            login_attempts.append(random.randint(1, 2))
            data_transferred.append(round(random.uniform(0.1, 5.0), 2))
        else: # 5% chance it's an anomalous threat activity spike
            login_attempts.append(random.randint(8, 25)) # Brute force hint
            data_transferred.append(round(random.uniform(500.0, 4500.0), 2)) # Data exfiltration hint

# Compile array columns into a structured DataFrame matrix
df = pd.DataFrame({
    'LogID': log_ids,
    'Timestamp': timestamps,
    'SourceIP': source_ips,
    'DeviceType': device_types,
    'LoginAttempts': login_attempts,
    'DataTransferred_MB': data_transferred,
    'AccessHour': access_hours
})

# Export directly to your project workspace
output_path = "../Database/raw_network_logs.csv"
df.to_csv(output_path, index=False)
print(f"✅ Success! Raw dataset generated and saved to: {output_path}")