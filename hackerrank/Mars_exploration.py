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