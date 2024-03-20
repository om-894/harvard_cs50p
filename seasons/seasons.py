
import inflect
from datetime import date
import sys
# YYYY-MM-DD

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid date")

    print(minutes_lived(year, month, day))



def minutes_lived(year, month, day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid date"
    today = date.today()
    diff = today - dt
    # print(type(diff))                           # look for data type using type()
    minutes = int(diff.total_seconds() / 60)      # returned class as date.timedelta
    msg = p.number_to_words(minutes, andword="") + " minutes"
    return msg.capitalize()





if __name__ == "__main__":
    main()
