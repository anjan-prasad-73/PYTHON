filename = "D:\\Practice\\Python\\File_handling\\worksheet\\applicaiton_logs.txt"   

counts = {} 

try:
    with open(filename, "r") as file:
        for line in file:
            words = line.strip().lower().split()
            
            for word in words:
                word = word.strip(".,!?()[]{}'\"")
                
                if word:  
                    counts[word] = counts.get(word, 0) + 1   
    print(counts)

except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
