pat="aba"
str="ababdfergdfgdfgdfgdfgdfg"
LPS=[-1,-1,0,1,-1]
#for i in pat:
 #      patlist.append(i)
  #      LPS.append(-1)
   # else:
    #    LPS.append(pat.index(i))
#print(LPS)

aa

aaaa



i=0
j=-1
res=-1
while i<len(str):
    if str[i]==pat[j+1]:
        if j+1==len(pat)-1:
            res=i-(j+1)
        #     Append to a list
        #     Move i & j
        else:
            i=i+1
            j=j+1
    else:
        if j==-1:
            i=i+1
        else:
            j=LPS[j]
print(res)
print("Hello")
