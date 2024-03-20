
import sys

if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":     # [-2:] means last two indexes from the end in list/string
        try:
            with open(sys.argv[1]) as file:
                linecount = 0
                for line in file:
                    if not line.lstrip().startswith("#") and line.lstrip() != '':
                        linecount +=1
            print(linecount)
        except FileNotFoundError:
            sys.exit("File not found")
    elif sys.argv[1][-2:] != "py":
        sys.exit("Not a python file")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")






