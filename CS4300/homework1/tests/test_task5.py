#import dependencies
import runpy
#functions for books
def test_books():
    result = runpy.run_path("src/task5.py")

    fav_books = result["fav_books"]

    assert len(fav_books) == 5
    assert fav_books[0] == "The Lord of The Rings - J.R.R. Tolkien"
#function for dict slicing
def test_slicing():
    result = runpy.run_path("src/task5.py")

    first_three = result["first_three"]
    assert first_three == [
        "The Lord of The Rings - J.R.R. Tolkien",
        "Eragon - Christopher Paolini",
        "Dune - Frank Herbert"
    ]
#funct for dict print
def test_student_dictionary():
    result = runpy.run_path("src/task5.py")

    students = result["students"]

    assert students[1001] == "Nathan Hinebaugh"
    assert students[1002] == "Billy Bob"
    assert students[1003] == "Bobbie Joe"