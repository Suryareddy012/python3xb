
# a = 15
#
# if a==10 or a==15 or a==20:
#     print("Hi")
# else :
#     print("Hastala vista")



#Example 1: Print the first 10 natural numbers using for loop.
#
#
# for i in range(1,11):
#     print(i)
#
# #Example 2: Python program to print all the even numbers within the given range.
#
# n=11
# for i in range(1,n):
#     if i%2==0:
#         print(i)

#Example 3: Python program to calculate the sum of all numbers from 1 to a given number.
n=int(input("Enter the number"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
