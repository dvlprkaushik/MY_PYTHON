name = input("Enter your name : ")
print("Your name is : ",name)

num1 = input("Enter num1 : ")
num2 = input("Enter num2 : ")
sum = int(num1)+int(num2)
# python cannot understand the input type
# so by default it takes the type as string
# so we need type conversion to int or type of our choice

print("The sum of ",num1," and ",num2,"is : ",sum)
