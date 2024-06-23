#Polindrome of string

s=input("Enter the string")
s1=s[::-1]
if(s==s1):
    print("palindrome")
else:
    print("not palindrome")
