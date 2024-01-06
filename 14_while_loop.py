# i = 0
# while (i < 3):
#     print(i)
#     i = i+1

from itertools import count


k = int(input("Enter the number : "))
while (k <= 38):
    k = int(input("Enter the number : "))
    print(k)

print("Done with the loop")

count = 5
while(count>0):
    print(count)
    count = count - 1
else:
    print("Im inside else")
