def dayOfProgrammer(year):
    # Write your code here
    dayOfP = 256
    difference = 0
    mm = 0
    dd = 0
    i = 0
    monthsDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year in range(1700, 1917):
        print("Year lies in Julian Calender")
        if year % 4 == 0:
            monthsDays[1] = 29

    elif year in range(1919, 2700):
        print("Year lies in Gregorian Calender")
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            monthsDays[1] = 29

    elif year == 1918:
        dayOfP = dayOfP + 13

    while difference < dayOfP:
        difference = difference + monthsDays[i]
        print(difference)
        i += 1

    dd = dayOfP - difference + 30
    mm = i
    print("Date is : ", dd, "Month is :", mm)

    mm = str(mm).zfill(2)

    outputstring = str(dd) + "." + str(mm) + "." + str(year)

    return outputstring