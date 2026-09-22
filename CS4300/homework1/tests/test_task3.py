import runpy

def test_if_state():
    result = runpy.run_path("src/task3.py")
    assert result ["number"] == -7
    assert result ["num_result"] == "Neg"

def test_for_loop():
    result = runpy.run_path("src/task3.py")
    assert result["prime_numbers"] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_while_loop():
    result = runpy.run_path("src/task3.py")
    assert result["total"] == 5050