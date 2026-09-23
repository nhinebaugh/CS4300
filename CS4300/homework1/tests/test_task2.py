import runpy
import pytest

@pytest.mark.parametrize(
    "var_name, exp_val, exp_type",
    [
        ("int_val", 10, int),
        ("flt_val", 3.68, float),
        ("str_val", "Hello World!", str),
        ("bool_val", True, bool),
    ],
)
def test_data_types(var_name, exp_val, exp_type):
    result = runpy.run_path("src/task2.py")
    assert result[var_name] == exp_val
    assert isinstance(result[var_name], exp_type)