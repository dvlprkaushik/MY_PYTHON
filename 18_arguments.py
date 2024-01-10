# default arguments:
def name_default(fname,mname = "Kumar",lname = "singh"):
    print("Hello,",fname,mname,lname)
    
name_default("Rahul") #it will take default arguments
name_default("john","jakie","williamson")

# required arguments :
def name_required(fname,mname,lname):
    print("Hello,",fname,mname,lname)
    
name_required("Kaushik","Kumar","Das")

# arbitary arguments : 
def average_arbi(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    return sum/len(numbers)
    
c = average_arbi(2,3,4)
print(c)