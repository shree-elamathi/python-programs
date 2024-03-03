#There is a collection of input strings and a collection of query strings. For each query string,
# determine how many times it occurs in the list of input strings. Return an array of the results.
def matchingstrings(s,q):
    val=[]
    for i in q:
        x=s.count(i)
        val.append(x)
    return val
s=['ab','ab','abc']
q=['ab','abc','bc']
print(matchingstrings(s,q))