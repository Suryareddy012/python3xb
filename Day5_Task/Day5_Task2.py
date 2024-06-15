
side_1=int(input("Enter side 1 angle"))
side_2=int(input("Enter side 2 angle"))
side_3=int(input("Enter side 3 angle"))

if side_1 == side_2 == side_3:
    print("It is an equilateral triangle")
elif side_1 == side_2 or side_1==side_3 or side_2==side_3:
    print("It is an isosceles triangle")
else:
    print("It is a scalene triangle")

