#read text file and count number of words then print how many words
from pathlib import Path

def count_words(file_path):
    path = Path(file_path)

    with path.open("r", encoding="utf-8") as file:
        text = file.read()

    return len(text.split())

file_path = Path(__file__).parent.parent / "task6_read_me.txt"
word_count = count_words(file_path)

print("Word Count: ", word_count)