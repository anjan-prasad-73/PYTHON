import re

filename = "D:\\Practice\\Python\\File_handling\\worksheet\\large_log.txt"

grouped_logs = {}

pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)\s+(\w+):\s+\[(.*?)\]\s+-\s+(.*)"

try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                timestamp, severity, section, message = match.groups()

                if severity not in grouped_logs:
                    grouped_logs[severity] = []
                grouped_logs[severity].append((timestamp, section, message))

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

for severity, entries in grouped_logs.items():
    print(f"\n--- {severity} Logs ---")
    for timestamp, section, message in entries:
        print(f"[{timestamp}] [{section}] {message}")
    print("-" * 40)
