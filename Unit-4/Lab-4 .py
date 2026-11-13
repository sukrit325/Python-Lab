from collections import Counter, defaultdict
import json
import os


def create_sample_json_logs(filename="app_logs.json"):
  """Generates a sample JSON log dataset."""
  logs = [
      {
          "timestamp": "2026-06-01T08:30:00Z",
          "level": "INFO",
          "module": "auth",
          "message": "User logged in",
      },
      {
          "timestamp": "2026-06-01T08:35:12Z",
          "level": "ERROR",
          "module": "database",
          "message": "Connection refused",
      },
      {
          "timestamp": "2026-06-01T09:00:22Z",
          "level": "WARNING",
          "module": "payment",
          "message": "Gateway timeout warning",
      },
      {
          "timestamp": "2026-06-01T09:15:05Z",
          "level": "ERROR",
          "module": "auth",
          "message": "Invalid credentials",
      },
      {
          "timestamp": "2026-06-01T09:30:44Z",
          "level": "ERROR",
          "module": "database",
          "message": "Connection refused",
      },
      {
          "timestamp": "2026-06-01T10:00:00Z",
          "level": "INFO",
          "module": "payment",
          "message": "Transaction completed",
      },
  ]
  with open(filename, "w") as f:
    json.dump(logs, f, indent=4)


def analyze_json_logs(input_file="app_logs.json", output_file="log_report.json"):
  """Analyzes JSON logs and generates a structured summary file."""
  if not os.path.exists(input_file):
    print(f"Error: {input_file} not found.")
    return

  with open(input_file, "r") as f:
    logs = json.load(f)

  total_logs = len(logs)
  level_counts = Counter()
  module_error_counts = defaultdict(int)
  frequent_errors = Counter()

  for entry in logs:
    level = entry.get("level", "UNKNOWN")
    module = entry.get("module", "general")
    message = entry.get("message", "")

    level_counts[level] += 1

    if level == "ERROR":
      module_error_counts[module] += 1
      frequent_errors[message] += 1

  # Construct summary report
  report = {
      "total_logs": total_logs,
      "severity_breakdown": dict(level_counts),
      "errors_by_module": dict(module_error_counts),
      "top_error_messages": frequent_errors.most_common(3),
  }

  with open(output_file, "w") as f:
    json.dump(report, f, indent=4)

  print("--- JSON Log Analyzer Report Generated ---")
  print(json.dumps(report, indent=4))
  print(f"\nReport successfully saved to {output_file}")


if __name__ == "__main__":
  input_log_file = "app_logs.json"
  output_report_file = "log_report.json"

  create_sample_json_logs(input_log_file)
  analyze_json_logs(input_log_file, output_report_file)