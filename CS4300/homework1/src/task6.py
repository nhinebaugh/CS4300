#read text file and count number of words then print how many words
from pathlib import Path

file_path = Path(__file__).parent.parent/"task6_read_me.txt"

with open(file_path, "r") as file:
    text = file.read()

word_count = len(text.split())

print("Count: ", word_count)