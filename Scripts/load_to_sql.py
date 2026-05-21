import pandas as pd
import sqlite3
import os

print("📂 Initializing SQL Database Engineering Engine...")

# 1. Connect to the local SQLite Database file container
db_dir = "../Database"
db_path = os.path.join(db_dir, "cybersecurity_vault.db")

# Establish a connection channel (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. Define our structured Relational Table Schema
# This ensures strict data types, data integrity, and lightning-fast primary key indexing
print("🏗️ Creating structured 'network_security_logs' table...")
cursor.execute("""
    DROP TABLE IF EXISTS network_security_logs;
""")

cursor.execute("""
    CREATE TABLE network_security_logs (
        LogID INTEGER PRIMARY KEY,
        Timestamp TEXT,
        SourceIP TEXT,
        DeviceType TEXT,
        LoginAttempts INTEGER,
        DataTransferred_MB REAL,
        AccessHour INTEGER,
        ThreatScore INTEGER,
        ThreatLevel TEXT
    );
""")

# 3. Load our processed AI pipeline data from Step 2
csv_path = os.path.join(db_dir, "enriched_security_logs.csv")
if not os.path.exists(csv_path):
    print(f"❌ Error: Could not find enriched file at {csv_path}. Please rerun Step 2!")
    conn.close()
    exit()

df = pd.read_csv(csv_path)

# 4. Stream the data row matrix into our structured SQL engine
print(f"🚀 Streaming {len(df)} entries into the relational database ledger...")
df.to_sql('network_security_logs', conn, if_exists='append', index=False)

# Commit changes and close the secure transaction pipeline link
conn.commit()

# 5. Technical Validation Check
# Let's run a quick native SQL query to prove our data is safely inside the engine
print("🔬 Running verification SQL query query...")
cursor.execute("SELECT COUNT(*), ThreatLevel FROM network_security_logs GROUP BY ThreatLevel;")
validation_results = cursor.fetchall()

print("\n✅ SQL Database Verification Metrics:")
for row in validation_results:
    print(f" 🔹 Threat Level: {row[1]:<12} | Database Record Count: {row[0]}")

conn.close()
print(f"\n🔒 Relational architecture locked! Database file active at: {db_path}")