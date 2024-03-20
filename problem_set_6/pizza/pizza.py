
import tabulate # makes csv into a table
import sys
import csv

if len(sys.argv) == 2:
    if sys.argv[1][-3:] == "csv": # slicing the last 3 characters
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("not a csv file")
elif len(sys.argv) < 2:
    sys.exit("Too few command line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command line arguments")





