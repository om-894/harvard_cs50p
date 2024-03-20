


import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level <= 0:
        continue

    num = random.randint(1, level)
    break

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            print("Too small!")
            continue
    except ValueError:
        continue

    if guess < num:
        print("too small!")
    elif guess > num:
        print("Too large!")
    else:
        print("Just right!")
        break



























"""import random

def main():
    try:
        n = int(input("Level: "))
        number = random.randint(0, n)
    except (EOFError, ValueError, NameError):
        pass

    while True:
        guess = input("Guess: ")

        if guess.isdigit():
            if guess == number:
                print("Just right!")
                break
            elif guess > number:
                print("Too large!")
            elif guess < number:
                print("Too small!")
        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()"""



