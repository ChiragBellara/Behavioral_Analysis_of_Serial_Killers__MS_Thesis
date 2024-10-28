import glob
import os

for file_path in glob.glob("links/*.csv"):
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        content = content.replace(',', '')
        with open(file_path, 'w') as file:
            file.write(content)