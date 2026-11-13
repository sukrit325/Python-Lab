from collections import Counter
import os


def create_sample_log(filename="server.log"):
  """Creates a sample log file for demonstration purposes."""
  sample_logs = [
      "2026-06-01 10:00:15 INFO Server started successfully on port 8080\n",
      "2026-06-01 10:05:22 WARNING High memory usage detected: 85%\n",
      "2026-06-01 10:10:04 ERROR Database connection timeout\n",
      "2026-06-01 10:12:30 INFO User 'admin' logged in\n",
      "2026-06-01 10:15:45 ERROR Failed to write to cache directory\n",
      "2026-06-01 10:20:00 WARNING Disk space running low\n",
  ]
  with open(filename, "w") as f:
    f.writelines(sample_logs)


def analyze_log_file(filename):
  """Reads a log file, counts log levels, and prints error summaries."""
  if not os.path.exists(filename):
    print(f"Error: The file '{filename}' does not exist.")
    return

  log_levels = Counter()
  error_messages = []

  try:
    with open(filename, "r") as file:
      for line in file:
        parts = line.strip().split(" ", 3)
        if len(parts) >= 3:
          level = parts[2]
          log_levels[level] += 1
          if level == "ERROR":
            error_messages.append(line.strip())

    print("--- Log Analysis Summary ---")
    print(f"Total Log Entries: {sum(log_levels.values())}")
    print("\nBreakdown by Level:")
    for level, count in log_levels.items():
      print(f"  {level}: {count}")

    if error_messages:
      print("\nCaptured Errors:")
      for err in error_messages:
        print(f"  -> {err}")

  except IOError:
    print(f"Error: Could not read file '{filename}'.")


if __name__ == "__main__":
  log_filename = "server.log"
  create_sample_log(log_filename)
  analyze_log_file(log_filename)