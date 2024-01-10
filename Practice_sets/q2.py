from multiprocessing import current_process
curr = 0
prev = 0
for i in range(0,10):
        curr = i
        sum = prev+curr
        print("Current Number ",i," Previous Number",prev ,"Sum :",sum)
        prev = curr