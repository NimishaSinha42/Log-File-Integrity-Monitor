# Log File Integrity Monitor

A Python-based File Integrity Monitoring tool that calculates the SHA-256 hash of a monitored file and detects unauthorized or unexpected modifications.

The script stores the original hash as a baseline and compares it with the latest hash whenever it runs. If a change is detected, an alert is recorded in `integrity_alerts.log`. Windows Task Scheduler is used to automatically execute the script every 5 minutes.

## Features

- Calculates SHA-256 hash of a file
- Creates and stores a baseline hash
- Detects file modifications
- Logs integrity changes with timestamps
- Automatically runs every 5 minutes using Windows Task Scheduler

## Technologies Used

- Python
- hashlib
- Windows Task Scheduler

## Setup

1. Install Python 3.
2. Clone or download this repository.
3. Place the file you want to monitor in the project directory.
4. Configure the file path in the Python script if required.

No external Python packages are required.

## Run

Run the script manually using:

```bash
python integrity_monitor.py
