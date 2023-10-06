#Amy wanderi - sct211-0010/2021
year = int(input("Give me an year?"))
#calculate if it is a leap year
rem = year % 100
if rem % 4 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
