
import inflect

def bid_adieu(names):
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        farewell = ", ".join(names[:-1]) + f", and {names[-1]}" # [:-1] means "from the beginning of the list up to, but not including, the last element.
        print(f"Adieu, adieu, to {farewell}")




def main():
    names = []
    try:
        while True:
            name = str(input("Name: "))
            names.append(name)
    except EOFError:    # when you use ctrl-D
        pass

    p = inflect.engine()
    num_names = len(names)
    if num_names > 0:
        bid_adieu(names)


if __name__ == "__main__":
    main()


