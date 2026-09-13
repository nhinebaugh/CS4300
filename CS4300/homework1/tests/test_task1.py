import runpy

def test_task1_output(capsys):
    runpy.run_path("src/task1.py")

    captured = capsys.readouterr()

    assert captured.out == "Hello, World!\n"