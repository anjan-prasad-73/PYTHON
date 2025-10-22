import re

filename = "D:\\Practice\\Python\\File_handling\\worksheet\\large_log.txt"
pattern = r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d+)\s+(\w+):\s+\[(.*?)\]\s+-\s+(.*)"


def parse_line(line,pattern):
    match = re.match(pattern, line.strip())
    if match:
        return match.groups()
    else:
        return None
    
def parse_file(filename,pattern):
    parsed_lines = []
    parsed_result = []

    try:
        with open(filename, 'r') as file:
            for line in file:
                parsed_lines = parse_line(line, pattern)
                if parsed_lines:
                    time_stamp, severity, section, message = parsed_lines
                    parsed_result.append({
                        'time_stamp': time_stamp,
                        'severity': severity,
                        'section': section,
                        'message': message
                    })
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    return parsed_result


logs = parse_file(filename, pattern)

for log in logs:
    print(log)