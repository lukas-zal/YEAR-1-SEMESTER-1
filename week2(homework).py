def leap():
    year = int(input("Enter a year: "))
    if year % 4 != 0:
        print(f"{year} Not a leap year.")
    elif year % 4 != 0 and year % 100 != 0:
        print(f"{year} It is a leap year.")
    elif year % 4 != 0 and year % 100 != 0 and year % 400 == 0:
        print(f"{year} NOT a leap year.")
    else:
        print(f"{year} Is a Leap Year.") 
leap()
