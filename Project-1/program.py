import time

timestamp = int(time.strftime('%H:%M:%S'))
print(timestamp)
timestamp_hour = int(time.strftime('%H'))
print(timestamp_hour)
timestamp_minute = int(time.strftime('%M'))
print(timestamp_minute)
timestamp_second = int(time.strftime('%S'))
print(timestamp_second)

if (timestamp > int(time.strftime('23:59:59'))):
    print("It is morning now")
elif (timestamp >= int(time.strftime('11:59:59')) and (timestamp <= int(time.strftime('15:59:59')))):
    print("It is afternoon")
elif (timestamp >= int(time.strftime('17:59:59')) and (timestamp <= int(time.strftime('19:59:59')))):
    print("It is good evening")
else:
    print("Good night :)")
