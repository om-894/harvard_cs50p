

def value(greeting):
    greeting = greeting.lower().strip()

    if greeting[:5] == "hello":
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

def main():
    greeting = input("Greeting: ")
    val = value(greeting)
    print("$" + str(val))


if __name__ == "__main__":
    main()
