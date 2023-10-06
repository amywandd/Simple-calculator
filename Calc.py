# Amy Njeri Wanderi - sct211-0010/2021
name = input("What is your name?")
print("Welcome ", name)
num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
total = num1 + num2
print("The addition of ", num1, "and ", num2, "is ", total)
#Find out birth year
birth_year = int(input("Which year were you born?"))
#Finds current year
current_year = int(input("What is the current year?"))
#calculates age in terms of years
age = current_year - birth_year
#finds date user was born
birth_date = int(input("Which date were you born?"))
#finds current date
current_date = int(input("What is the current date?"))
#calculates age in term of dates
if birth_date > current_date:
    age - 1
    print("You are", age, "years old", current_date, "days old")
elif current_date > birth_date:
    real_date = current_date - birth_date
    print("You are", age , "years old", real_date, "days old")
