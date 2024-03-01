class calculator:
    @staticmethod
    def concat(a,b,*c):
        result=a+b
        for val in c:
            result+=val
        return result

#main program
print(calculator.concat(10,20,40,50,60,80))
print(calculator.concat('ram','raja','rajesh'))
print(calculator.concat([1,2],[3,4],[5,6]))
