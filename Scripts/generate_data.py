import sqlite3
import datetime
import random

# Direct file path to your database
DB_PATH = r"D:\PROJECT\AI_Threat_Pipeline\Database\cybersecurity_vault.db"
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Using the exact table name from your database
table_name = "network_security_logs"

device_types = ["Server", "Database", "Firewall", "IoT Device", "Workstation"]
threat_levels = ["Low", "Medium", "High", "Critical"]
source_ips = ["192.168.1.50", "10.0.0.15", "185.220.101.5", "45.227.254.12", "199.19.224.43"]

print(f"Inserting 1000 clean rows into {table_name}...")

for _ in range(1000):
    random_days_ago = random.randint(0, 7)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    timestamp = datetime.datetime.now() - datetime.timedelta(days=random_days_ago, hours=random_hour, minutes=random_minute)
    
    access_hour = timestamp.hour
    source_ip = random.choice(source_ips)
    device_type = random.choice(device_types)
    threat_level = random.choice(threat_levels)
    login_attempts = random.randint(1, 15) if threat_level in ["High", "Critical"] else random.randint(1, 3)

    # ONLY using the standard columns that already exist in your table
    query = f"""
    INSERT INTO {table_name} (Timestamp, AccessHour, SourceIP, DeviceType, ThreatLevel, LoginAttempts)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    
    cursor.execute(query, (
        timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        access_hour,
        source_ip,
        device_type,
        threat_level,
        login_attempts
    ))

conn.commit()
conn.close()
print("🎉 Success! 1,000 security logs generated with no extra column bugs.")