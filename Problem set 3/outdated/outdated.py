
# 9/8/1636 or September 8, 1636
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("date: ")
    if "/" in date:
        month, day, year = date.split("/")

    elif "," in date:
        date = date.replace(",", "") # removes the comma from the string
        month, day, year = date.split(" ") # splits at the space
        if month in months:     # want to reassign month to index
            month = months.index(month) + 1    # index() says the index in the list

    else:
        continue # if neither format provided, reprompt user for a date.


    try:
        if int(month) > 12 or int(day) > 31:
            continue
        else:
            break
    except ValueError:
        continue


print(f"{int(year)}" + '-' + f"{int(month):02}" + '-' + f"{int(day):02}")
