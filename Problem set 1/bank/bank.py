
greet = str(input("greet me! ").strip().lower())

if greet.startswith("hello") == True or greet == "hello":
    print("$0")
elif greet[0] == "h" and greet[0:4] != "hello":
    print("$20")
else:
    print("$100")
