import runpy
import numpy as np

def test_numpy():
    result = runpy.run_path("src/task7.py")

    numbers = result["numbers"]
    average = result["average"]

    assert numbers == [10, 20, 30, 40, 50]
    assert average == np.mean(numbers)
    assert average == 30.0