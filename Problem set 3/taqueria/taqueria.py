menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True:
    try:
        item = input("place your order: ").title()
    except (NameError, EOFError):    # could be any error. iff no need for except then skips to if statement.
        print() # prints nothing, then exits the while loop.
        break
    if item in menu:
        total = total + menu[item]
        print("$", f"{total:.2f}", sep = "")

# Keep as little as possible in try, only what could go wrong.

