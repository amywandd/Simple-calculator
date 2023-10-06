#Amy Wanderi - sct211-0010/2021
#Get the necessary measurements to calculate BMI
height = int(input("What is your height?"))
weight = int(input("What is your weight?"))
#Calculate BMI
BMI = weight / (height * height)
if BMI < 18.5:
    print("You are underweight")
elif BMI >= 25:
    print("You are overweight")
else:
    print("You have normal weight")
