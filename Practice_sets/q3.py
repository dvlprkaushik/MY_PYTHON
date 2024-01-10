my_String = "KAUSHIK"
start = 0
size = len(my_String)
step = 2
print("Printing only even index chars")
for i in range(start, size, step):
    print("Index [",i,"]", my_String[i])

