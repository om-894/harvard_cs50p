def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dol = d.replace("$", "")
    dollar_float = float(dol)
    return dollar_float


def percent_to_float(p):
    perc = p.replace("%", "")
    percent_float = float(perc) / 100
    return percent_float

main()
