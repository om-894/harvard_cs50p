

# x = int(input("Input a number: "))
# z = int(input("Input a number: "))
# y = str(input("What operator would you like to use?"))

expression = input("give me a sum: ")
x_str, y, z_str = expression.split(" ")
x = int(x_str)
z = int(z_str)

if y == "+":
    print(float(x + z))
elif y == "-":
    print(float(x - z))
elif y == "*":
    print(float(x * z))
elif y == "/":
    print(float(x / z))
else:
    print(".")

