
from twttr import shorten

def main():
    test_twttr()


def test_twttr():
    assert shorten("hello") == "hll"
    assert shorten("muppet") == "mppt"
    assert shorten("hello, WORLD") == "hll, WRLD"
    assert shorten("23") == "23"



if __name__ == "__main__":
    main()
