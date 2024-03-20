
def convert(f):
    x, y = f.split("/")
    x, y = int(x), int(y)
    return float(x / y)


while True:
    fraction = input("Enter a fraction: ")

    try:
        percent = convert(fraction)
        if percent <= 1:
            break

    except (ValueError, ZeroDivisionError):
        pass

percent = percent * 100
percent = round(percent)

if percent <= 1:
    print("E")
elif percent >= 99:
    print("F")
else:
    print(str(percent) + "%")



