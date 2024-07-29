# populate list of experiments file :3
import os

files = os.listdir()
python_files = [f for f in files if f.endswith(".py")]
# print(python_files)

with open("001-listOfExperiments.md", "a") as write_file: 
    for index, file in enumerate(python_files):   
        with open(file, "r") as f:
            t = f.readlines()
            t = t[2]
            t = t.strip()
            print(t)
            write_file.write(f"{index + 1}. {t}\n")