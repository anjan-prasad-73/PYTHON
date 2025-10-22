filename = "D:\\Practice\\Python\\File_handling\\worksheet\\complex_log.txt"
logfile = "D:\\Practice\\Python\\File_handling\\worksheet\\error_log.txt"

try:
    with open(filename, "r") as file, open(logfile, "w") as log:
        for line in file:
            if "ERROR" in line.upper():
                log.write(line)
            
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")