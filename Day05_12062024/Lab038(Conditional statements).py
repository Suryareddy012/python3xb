
#There are three types of conditional statements
#1. if
#2. if-else
#3. elif

# age=28
#
# if age>=18:
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


age1 = int(input("Enter the Eligible age of men for the Marriage"))
age2 = int(input("Enter the Eligible age of women for the Marriage"))

print ("you're eligible for marriage" if age1>=21 and age2>=18 else "you're not eligible for marriage")

#or

if age1>=21 and age2>=18:
    print("you are eligible to get married")
else:
    print("you are not eligible to get married")

#or
if age1>=21 :
    print("Men is eligible for marriage")
else:
    print("Men is not eligible for marriage")
if age2>=18 :
    print("Women is eligible for marriage")
else:
    print("Women is not eligible for marriage")

