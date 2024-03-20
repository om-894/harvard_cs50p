
from plates import is_valid

def main():
    test_valid1()
    test_valid2()
    test_valid3()
    test_valid4()

def test_valid1():
    assert is_valid("c") == False
    assert is_valid("hello, world") == False

def test_valid2():
    assert is_valid("46") == False
    assert is_valid("cs") == True

def test_valid3():
    assert is_valid("cs..fh") == False
    assert is_valid("cs60") == True

def test_valid4():
    assert is_valid("cs05") == False
    assert is_valid("cs50") == True


if __name__ == "__main__":
    main()
