
def main():
    num = input("Enter a fraction: ")
    percentage = convert(num)
    gauge(percentage)


def convert(num):
    while True:
        index = num.find("/")
        try:
            x = int(num[:index])
            y = int(num[index+1:])
            fraction = x / y
            if x > y:
                num = input("Fraction: ")
                continue
            else:
                percentage = int(fraction * 100)
                return percentage
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()

