#A space explorer's ship crashed on Mars! They send a series of SOS messages to Earth for help.
#Letters in some of the SOS messages are altered by cosmic radiation during transmission.
# Given the signal received by Earth as a string,s, determine how many letters of the SOS
# message have been changed by radiation.

def convert(s):
    val=0
    let="SOS"
    i=0
    j=0
    while i<len(s) and j<=len(let):
        if j==len(let):
            j=0
        if s[i]!=let[j]:
            val+=1
            i+=1
            j+=1
        else:
            i+=1
            j+=1
    return val

s="SOSOSOSOSDSDSKWOSDOSDOASDOASDFAFJDFDOSOSOWNSOSOSNDSKDDOSOSOSJDSDSOOSOSDSDOSASSOASDSAOSOSODSDSOASDWS"
print(convert(s))