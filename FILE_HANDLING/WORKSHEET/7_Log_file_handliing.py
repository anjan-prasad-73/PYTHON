import re

filename = "D:\\Practice\\Python\\File_handling\\worksheet\\large_log.txt"

pattern = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+\s+(\w+):"

def group_by_severity(filename, pattern):
    severity_dict = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                match = re.match(pattern, line.strip())
                if match:
                    severity = match.group(1)  
                    severity_dict.setdefault(severity, []).append(line.strip())

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return severity_dict

logs_by_severity = group_by_severity(filename, pattern)

print("Log distribution by severity:\n")
for severity, entries in logs_by_severity.items():
    print(f"{severity}: {len(entries)} logs")

print("\nUnique severities found:", set(logs_by_severity.keys()))
