Num = int(input("Enter number: "))
n = 1
for i in range(1, Num + 1):
    Fact1 = n * i
    print(i, end=' ')
    if i < Num:
        print("*", end=' ')
print("\nFactorial: ", n)