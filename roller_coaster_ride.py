print("\n Welcome to the Roller Coaster !\n")
print("\n Ticket price for age less than or equal to 12 is 5$ \n Ticket price for age less than or equal to 18 is 7$ \n Ticket price of ticket age more than 18 is: 12$ \n Price for per photo is extra $3 \n ")
height = int(input("What is your height in cm? eg. 150 120 180: "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? 8 5 30: "))
    if age <= 12:
        bill = 5
        print(f"Please pay {bill}.")
    elif age <= 18:
        bill = 7
        print(f"Please pay {bill}.")
    else:
        bill = 12
        print(f"Please pay {bill}.")

    wants_photo = input("Do you wish to get a memorable photo in roller-coaster. It just costs $3 extra ? Press 'y' for Yes or 'n' for No.")
    if wants_photo == "y" or wants_photo == "Y":
        bill += 3

    print(f"Your final bill is : {bill}")

else:
    print("Sorry !! you have to grow taller before you can ride...")
