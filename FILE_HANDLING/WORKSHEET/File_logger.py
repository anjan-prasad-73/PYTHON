import logging

logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("file_error_log.txt"),
        logging.StreamHandler()
    ]
)

filename = "missing_file.txt"  

try:
    with open(filename, "r") as f:
        content = f.read()
        print("File content:")
        print(content)

except FileNotFoundError:
    logging.error(f"Error: The file '{filename}' was not found.")
