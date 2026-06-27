#Strings
#Immutable - can't be changed, | concatenation | len | index letters

#Write a python program which takes input of someones name and prints first character, last character 
# and total length of name
name = input("Enter your name:")
print(f"First letter of name is: {name[0]}")
print(f"Last letter of name is: {name[-1]}")
print(f"Length of name is: {len(name)}")

#SLicing [start:End]
print(f"Part of name is: {name[0:3]}") #End index is excluded

#Write a program that takes favorite food item as input and prints:
#The middle 3 characters | The last two characters
fav_food=input("Enter your favourite food:")
Middle_fav_food=len(fav_food)//2
print(f"The middle three charcters are: {fav_food[Middle_fav_food-1:Middle_fav_food+2]}")
print(f"The last two characters are {fav_food[-2:]}")

#Take a sentence as input and covert it into lowercase, Replace all " " with "_" and Print the new string
str = input("Enter the sentence:")
str_lower = str.lower() # all characters to lowercase
str_replace = str.replace(" " , "_")
print("The sentence in lower form is:", str_lower)
print("The sentence replace is:", str_replace)
print(str.capitalize()) #first letter of the first word only capitalize
print(str.title()) # all first letters of each words gets capitalized
print(str.find("or"))
print(str.count("a"))

