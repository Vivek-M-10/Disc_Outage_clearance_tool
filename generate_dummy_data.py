import os
import time

# Matching config.py paths
TARGET_DIRECTORIES = [
    "/Users/keviv/Desktop/Disc_outage_clearance/logs/app_log",
    "/Users/keviv/Desktop/Disc_outage_clearance/logs/temp_logs",
    "/Users/keviv/Desktop/Disc_outage_clearance/logs/transaction_logs"
]

def create_file(folder, name, days_old):
    file_path = os.path.join(folder, name)
    with open(file_path, 'w') as f:
        f.write(f"Dummy content for {name}\n")
    old_time = time.time() - (days_old * 86400)
    os.utime(file_path, (old_time, old_time))

for folder in TARGET_DIRECTORIES:
    os.makedirs(folder, exist_ok=True)
    create_file(folder, "old_file_1.log", 10)
    create_file(folder, "old_file_2.txt", 12)
    create_file(folder, "recent_file_1.log", 2)
    create_file(folder, "recent_file_2.txt", 1)

print("✅ Dummy files created.")
