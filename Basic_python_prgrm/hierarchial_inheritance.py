class student:
    r_num1=101
    r_num2=102
class name(student):
    r_name1="Rajesh"
    r_name2="Ranju"
class avg(student):
    avg1=80
    avg2=90 
c=name()
d=avg()
print("student 1 roll number is",c.r_num1,",student 1 name is",c.r_name1,",student 1 average is",d.avg1)
print("student 2 roll number is",c.r_num2,",student 2 name is",c.r_name2,",student 2 average is",d.avg2)
