import runpy
import pytest

@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("5", "Positive"),
        ("-5", "Negative"),
        ("0", "Zero"),
    ],
)

def test_num_check(monkeypatch, user_input, expected):
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    result = runpy.run_path("src/task3.py")
    check_num = result["check_num"]
    number = result["number"]

    assert check_num(number) == expected

def test_prime(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    result = runpy.run_path("src/task3.py")
    first_ten_primes = result["first_ten_primes"]

    assert first_ten_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def test_sum(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "5")

    result = runpy.run_path("src/task3.py")
    sum_one_to_one_hundred = result["sum_one_to_one_hundred"]

    assert sum_one_to_one_hundred() == 5050