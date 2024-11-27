import sys
import shutil
import os

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 create_template.py <year> <day>")
        sys.exit(1)
        
    year = sys.argv[1]
    day = sys.argv[2]
    
    os.makedirs(f"{year}/{day}", exist_ok=True)
    
    for i in range(1, 4):
        file = f"{year}/{day}/input{i}.txt"
        if not os.path.isfile(file):
            with open(file, "w") as f:
                pass
        
        file = f"{year}/{day}/testinput{i}.txt"
        if not os.path.isfile(file):
            with open(file, "w") as f:
                pass
            
    print(f"Input files successfully created for year 20{year} day {day}.")
    
    source = "template.py"
    dest = f"{year}/{day}/main.py"
    if not os.path.isfile(dest):
        shutil.copy(source, dest)
        print("Template file copied into folder.")
    else:
        print("Template file already exists.")