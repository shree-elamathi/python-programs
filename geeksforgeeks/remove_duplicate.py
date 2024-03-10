#Given a string str which may contain lowercase and uppercase characters. The task is to remove
# all duplicate characters from the string and find the resultant string. The order of remaining
# characters in the output should be same as in the original string.
def removeduplicate(str):
    val=[]
    s=""
    for i in str:
        if i not in val:
            val.append(i)
            s+=i
    return s
str="geEksforGEeks"
print(removeduplicate(str))