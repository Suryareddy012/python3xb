var1 = 10
var2 = 5
var3 = 7

# Compare the variables using greater than and less than conditions
if var1 > var2 and var1 > var3:
    print("var1 is greater than var2 and var3")
elif var2 > var1 and var2 > var3:
    print("var2 is greater than var1 and var3")
elif var3 > var1 and var3 > var2:
    print("var3 is greater than var1 and var2")
else:
    print("Variables are not distinct in terms of greater than and less than relationships")