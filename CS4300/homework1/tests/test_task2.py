import runpy

def test_int():
    result = runpy.run_path("src/task2.py")
    assert result["int_val"] == 10
    assert isinstance(result["int_val"], int)

def test_flt():
    result = runpy.run_path("src/task2.py")
    assert result["flt_val"] == 3.68
    assert isinstance(result["flt_val"], float)

def test_str():
    result = runpy.run_path("src/task2.py")
    assert result["str_val"] == "Hello World!"
    assert isinstance(result["str_val"], str)

def test_bool():
    result = runpy.run_path("src/task2.py")
    assert result["bool_val"] == True
    assert isinstance(result["bool_val"], bool)
