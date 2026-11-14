import json
import os

filename = "app_logs.json"

def analyze_logs():
    if not os.path.exists(filename):
        print("Log file not found.")
        return

    try:
        with open(filename, "r") as f:
            logs = json.load(f)

        info = 0
        warning = 0
        error = 0

        print("\n--- LOG RECORDS ---")

        for log in logs:
            print(log)

            if log["level"] == "INFO":
                info += 1
            elif log["level"] == "WARNING":
                warning += 1
            elif log["level"] == "ERROR":
                error += 1

        print("\n--- LOG SUMMARY ---")
        print("INFO messages:", info)
        print("WARNING messages:", warning)
        print("ERROR messages:", error)

    except json.JSONDecodeError:
        print("Invalid JSON data.")


logs = [
    {"timestamp": "10:00", "level": "INFO", "message": "Application started"},
    {"timestamp": "10:05", "level": "WARNING", "message": "Low memory"},
    {"timestamp": "10:10", "level": "ERROR", "message": "Database connection failed"},
    {"timestamp": "10:15", "level": "INFO", "message": "User logged in"},
    {"timestamp": "10:20", "level": "ERROR", "message": "File not found"}
]

with open(filename, "w") as f:
    json.dump(logs, f, indent=4)

analyze_logs()