
def main():
    answer = input("What time is it? ")
    time = convert(answer)

    # breakfast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        print("not time for food!")


# convert the time into hours and minute variables
# conver the minute variable into actual minutes (/60)
def convert(time):
    hours, minutes = time.split(":")
    new_mins = float(minutes) / 60
    return float(hours) + new_mins

main()
