import re

filename = "D:\\Practice\\Python\\File_handling\\worksheet\\large_log.txt"

pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)\s+(\w+):\s+\[(.*?)\]\s+-\s+(.*)"

try:
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            match = re.match(pattern, line)
            if match:
                time_stamp, severity, section, message = match.groups()

                print(f"Timestamp: {time_stamp}")
                print(f"Severity : {severity}")
                print(f"Section  : {section}")
                print(f"Message  : {message}")

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
