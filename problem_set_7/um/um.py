
import re


def main():
    print(count(input("Text: ")))


def count(s):
    word_count = re.findall(r"\b(um)\b", s, re.IGNORECASE)    # findall returns a list of lelemnts with um
    return len(word_count)

if __name__ == "__main__":
    main()
