# for i in range(2,10): #here it starts iterating from 2 and ends at 9 i.e n-1(10-1=9)
#     print(i)
#
# for i in range(1,100,3):
#     print(i)
#
# n=-3
#
# if n>=0:
#     print("Positive")
# else:
#     print("Negative")

#largest of 3 numbers

# a=3
# b=5
# c=10
#
# if a>b and a>c:
#     print(a)
# elif b>a and b>c:
#     print(b)
# else:
#     print(c)


week_day = int(input("Enter the week number: "))
week_name = (week_day % 7)

if week_name == 1:
    print("Sunday")
elif week_name == 2:
    print("Monday")
elif week_name == 3:
    print("Tuesday")
elif week_name == 4:
    print("Wednesday")
elif week_name == 5:
    print("Thursday")
elif week_name == 6:
    print("Friday")
elif week_name == 7:
    print("Saturday")
else:
    print("Invalid week number")