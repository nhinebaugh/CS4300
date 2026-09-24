#test to ensure task6 works correctly

import runpy
import pytest
from pathlib import Path

@pytest.mark.parametrize(
    "file_name, expected_count",
    [
        ("task6_read_me.txt", 127)
    ]
)

def test_word_count(file_name, expected_count):
    result = runpy.run_path("src/task6.py")

    count_words = result["count_words"]

    file_path = Path(file_name)

    assert count_words(file_path) == expected_count