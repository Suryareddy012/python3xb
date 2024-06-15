
year = int(input("Enter a year: "))

if year % 4 == 0:
    print("It is a Leap year")
else :
    print("it is not leap year")

print("it is Leap year" if year % 4 == 0 else "it is not Leap year")
