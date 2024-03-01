class student:
    r_num1=101
    r_num2=102
class eng(student):
    r_eng1=80
    r_eng2=90
class mat(student):
    r_mat1=80
    r_mat2=90
class avg(eng,mat):
    r_avg1=80
    r_avg2=90
c=avg()
print("student 1 roll number is",c.r_num1,"student 1 english mark is",c.r_eng1,"student 1 maths marks is",c.r_mat1,"student 1 average is",c.r_avg1)
print("student 2 roll number is",c.r_num2,"student 2 english mark is",c.r_eng2,"student 2 maths marks is",c.r_mat2,"student 2 average is",c.r_avg2)
