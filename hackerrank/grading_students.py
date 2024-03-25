#HackerLand University has the following grading policy:
# Every student receives a grade in the inclusive range from 0 to 100.
# Any grade less than 40 is a failing grade.
#Sam is a professor at the university and likes to round each student's grade according to these rules:
#If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple
# of 5.
#If the value of grade is less than 40 , no rounding occurs as the result will still be a failing grade.
def grading(grades):
    val=[40,45,50,55,60,65,70,75,80,85,90,95,100]
    for i in range(0,len(grades)):
        if grades[i]>=38:
            for j in val:
                if j>grades[i] and j-grades[i]<3:
                    grades[i]=j
                    break
    return grades
grades=[73,67,38,33]
print(grading(grades))