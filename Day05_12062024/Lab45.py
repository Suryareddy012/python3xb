# i=0
# while i < 5:
#     print(i)
#     i=i+1

score = int(input("Enter your score"))

if score >=90 and score <= 100:
    print("A")
elif score >=80 and score <= 89:
    print("B")
elif score >=70 and score <= 79:
    print("C")
elif score >=60 and score <= 69:
    print("D")
elif score <=59 and score >= 35:
    print("E")
else:
    print("F")