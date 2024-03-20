def main(x):
    if x == "42" or x == "forty two" or x == "forty-two":
        print("Yes")
    else:
        print("No")

q = input("what is the great question of Life, the universe and everything?").lower().strip()
main(q)
