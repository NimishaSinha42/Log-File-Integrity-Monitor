import hashlib
from pathlib import Path
from datetime import datetime

MONITORED_FILE = Path("sample.log")
HASH_FILE = Path("stored_hash.txt")
ALERT_FILE = Path("integrity_alerts.log")


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


def log_alert(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(ALERT_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{timestamp}] {message}\n")


def monitor_file():

    if not MONITORED_FILE.exists():
        log_alert("ERROR: Monitored file not found.")
        return

    current_hash = calculate_sha256(MONITORED_FILE)

    if not HASH_FILE.exists():
        HASH_FILE.write_text(current_hash)
        print("Baseline hash saved.")
        return

    old_hash = HASH_FILE.read_text().strip()

    if current_hash != old_hash:
        print("WARNING: File changed!")

        log_alert(
            f"{MONITORED_FILE} was modified. "
            f"Old Hash: {old_hash} | New Hash: {current_hash}"
        )

        HASH_FILE.write_text(current_hash)

    else:
        print("No change detected.")


if __name__ == "__main__":
    monitor_file()