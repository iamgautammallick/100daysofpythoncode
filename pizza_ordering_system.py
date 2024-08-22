print("Welcome to Python Pizza Deliveries! \n")
print("RATE CARD !! \n Small pizza (S): $15 \n Medium pizza (M): $20 \n Large pizza (L): $25 \n")
print("EXTRAS !!! \n Add pepperoni for small pizza : +$2 \n Add pepperoni for medium or large pizza : +$3 \n Add extra cheese for any size pizza: +$1 \n \n")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
if size.upper() == "S":
    bill += 15
elif size.upper() == "M":
    bill+= 20
elif size.upper() == "L":
    bill+=25
else:
    print("You have chosen wrong input. Please choose from S, M, L only")

if pepperoni.upper() == "Y":
    if size.upper() == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese.upper() == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
