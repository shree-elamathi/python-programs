list=eval(input("enter array?\n"))
largest=list[0]
for x in list:
    if x > largest:
        largest=x
print("The largest in the list is: ",largest)
