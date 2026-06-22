#implicit conversion
a = 1
b = 4.2
c= a+b
print(type(a),type(b), c, type(c))

#Explicit conversion
print("Explicit converison")
a=1
b=6
print(type(a),type(b))
a=float(a)
b=float(b)
c=a+b
print(type(a),type(b), type(c))

#Take input in celsius and convert to fahrenheit and kelvin
#f = (C * 9/5) + 32
#K = C + 273.15

C = float(input("Enter temperature in celsius:\n"))
F = (C * 9/5) + 32
K = C + 273.15
print(f"The temperature in Fahrenheit is {F}\nThe temperature in Kelvin is {K}")

# Takes bill and splits into number of friends
bill = float(input("Enter the total amount of the bill:"))
friends = int(input("Enter the number of friends:"))
Split = bill / friends
print(f"The Bill amount: {bill} is split among {friends} friends and each has to pay {Split}. Thank You")


