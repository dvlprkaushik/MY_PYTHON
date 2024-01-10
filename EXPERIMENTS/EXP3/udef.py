def _mathoperations_(a, b, ope):
    match ope:
        case 1:
            print("Addition of {a} and {b} is : ", a+b)
        case 2:
            print("Substraction of {a} and {b} is : ", a-b)
        case 3:
            print("Division of {a} and {b} is : ", a/b)
        case 4:
            print("Multiplication of {a} and {b} is : ", a*b)
        case _:
            print("Invalid!!!")


statement = """Enter 1 for addition :
Enter 2 for substraction :
Enter 3 for Division :
Enter 4 for Multiplication : """
print(statement)
operator = int(input("Input the operator of your choice : "))
var_one = int(input("Enter value of a : "))
var_two = int(input("Enter value of b : "))
_mathoperations_(var_one, var_two, operator)
