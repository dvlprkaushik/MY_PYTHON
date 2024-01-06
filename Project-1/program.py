import time
#importing time module

name = input("Enter tyour name : ")
current_time = time.strftime('%H:%M:%S')
print("Current time is : ", current_time)
timestamp_hour = int(time.strftime("%H"))

if (timestamp_hour > 24 and timestamp_hour < 12):
    print("Good Morning", name)
elif (timestamp_hour > 12 and timestamp_hour < 16):
    print("Good afternoon", name)
elif (timestamp_hour > 16 and timestamp_hour < 20):
    print("Good evening", name)
else:
    print("Good night ", name)

