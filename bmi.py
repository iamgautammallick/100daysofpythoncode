print("Welcome to BMI calculator !! \n")
weight = float(input("What is your weight in kg ?eg: 60 70 80: "))
height = float(input("What is your height in meter?eg: 1.56 1.75: "))
bmi = round(weight / (height ** 2),2)

if bmi < 18.5:
    print (f"Your BMI is: {bmi} - Underweight")
elif bmi < 25:
    print (f"Your BMI is: {bmi} -  Normal")
else:
    print(f"Your BMI is: {bmi} - Overweight \n START WORKINGOUT !!")
