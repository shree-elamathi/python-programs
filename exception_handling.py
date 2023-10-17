try:
    a=int(input("Enter the numerator: "))
    b=int(input("Enter the denominator: "))
    result=a/b
    print("The result=",result)
except ZeroDivisionError:
    print("Denominator should not be zero")
except ValueError:
    print("Enter a valid number")
except:
    print("Unknown error occured")
finally:
    print("Thank You")
