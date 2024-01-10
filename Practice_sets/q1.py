# Exercise 1: Calculate the multiplication and sum of two numbers
number1 = int(input("Enter number 1 : "))
number2 = int(input("Enter number 2 : "))

print("number1 : ",number1)
print("number2 : ",number2)

result_mul = number1*number2

if(result_mul<=1000):
    print("The result is : ",result_mul)
else:
    result_add = number1+number2
    print("The result is : ",result_add)
    

