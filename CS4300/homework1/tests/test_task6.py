#test to ensure task6 works correctly

import runpy

def test_word_count():
    result = runpy.run_path("src/task6.py")

    word_count = result["word_count"]

    with open("task6_read_me.txt", "r") as file:
        expected_count = len(file.read().split())

    assert word_count == expected_count