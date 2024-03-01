a=[10,20,30,40,50,60]
print(a)
search=eval(input("Enter the number:"))
for i in range(0,len(a),1):
    if(search==a[i]):
        print("Element found",i)
        break
else:
    print("Element not found")
