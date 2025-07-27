import os
import time
import logging
from config import TARGET_DIRECTORIES, LOG_FILE_PATH

# Ensure log directory exists
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)

# Setup logger
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def remove_old_logs(days_old=7, extensions=(".log", ".txt")):
    current_time = time.time()
    deleted_files = []

    for target_dir in TARGET_DIRECTORIES:
        if not os.path.exists(target_dir):
            logging.warning(f"Directory not found: {target_dir}")
            continue

        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith(extensions):
                    file_path = os.path.join(root, file)
                    try:
                        file_mtime = os.path.getmtime(file_path)
                        if current_time - file_mtime > days_old * 86400:
                            os.remove(file_path)
                            deleted_files.append(file_path)
                            logging.info(f"Deleted: {file_path}")
                    except Exception as e:
                        logging.error(f"Failed to delete {file_path}: {str(e)}")

    if not deleted_files:
        logging.info("Cleanup complete. No files deleted.")
    return deleted_files
