import random

def main():
    l = get_level()
    generate_integer(l)

def get_level():
    while True:
        level = input("Level: ")
        if level not in ["1", "2", "3"]:
            continue    # starts again
        return level

def generate_integer(level):
    score = 0
    for i in range(10): # for the 10 problems for each different level
        trials = 0
        if level == "1":
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == "2":
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        else:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        while True: # want to reprompt user
            print(f"{x} + {y} = ", end="") # need end so the answer isnt in the new line.
            answer = input()
            if answer == str(x + y):
                score += 1      # keep track of the score.
                break
            elif answer != str(x + y) and trials != 2:      # means user tried three times.
                print("EEE")
                trials += 1
                continue
            else:
                print("EEE")
                print(f"{x} + {y} = {x+y}")
                break
    print(score)

if __name__ == "__main__":
    main()
