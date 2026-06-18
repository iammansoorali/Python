print("''''Welcome''''")
print("Cicle's Area Calculator")

#Giving user the opiton to select radius or diameter
sel = int(input("Enter 1 to input radius or 2 to input diameter:\n"))
if sel == 1:
    radius = float(input("Please enter the radius:\n"))
    Area = round(3.1415 * radius * radius,2)
    print(f"The Area of the Circle is : {Area}")
elif sel == 2:
    dia = float(input("Please enter the diameter:\n"))
    Area = round(3.1415 * ((dia/2)**2),2)
    print(f"The Area of the Circle is {Area}")
else:
    print("You have entered the wrong input. Quitting")
print("Thank You.")