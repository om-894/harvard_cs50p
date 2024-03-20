def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(p):
    if len(p) <= 6 and len(p) >= 2 and p[0:2].isalpha() and p.isalnum():
        for i in p:
            if i.isdigit():
                index = p.index(i)
                if p[index:].isdigit() and i != '0':
                    return True
                else:
                    return False
        return True
    return False

if __name__ == "__main__":
    main()
