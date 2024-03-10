#A pangram is a string that contains every letter of the alphabet. Given a sentence determine
# whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram
# as appropriate.
def pangram(s):
    up=[]
    low=[]
    if len(s)<26:
        return ("not pangram")
    for i in s:
        if i.islower() and i not in low:
            if i.upper() not in up:
                low.append(i)
        elif i.isupper() and i not in up:
            if i.lower() not in low:
                up.append(i)
        else:
            continue
    if len(up)+len(low)>=26:
        return "pangram"
    return "not pangram"
s='YaCoVaGAaXxrzUvZ ZaHyacbUZCZUbZxzAYb YefxAwV yyABAdVatYazC TuyYYedxSf aA XBvSg EvYcl badDxvaZXWCyCUAaZvJcyc YdVbDYAdObgc FeCyxpdXxffubDbGAbFBxnzzT WzZ WcBZAaYCgYzseZb PYXbswxchtYIedhyaXtvzVxZSwWBLxxEaAaYAfGzybZzQo AH tCBcszyXZaAgwzYB QdVZBvwzAYbwwAVysxCRdTTT bXzxtWwyXZebEBYNBaDCLbZbwsEAB YTFBAcD bybU axAZAhhay ZkWydfxyGAeAYaZlabazUZssGTBcCXBr dWs XzyZAEzAAZyclC bCGzPfXcCccAFyvazX ZzYAB zAbsuCZADkeWwUuAbaZ zWCtYzgZZBzXXD c VsrbEaG aYYFZJBUlW iXqZxxswaWTJvb Y xuwebj CF zyZYZVdYYdaRyZ bTatyzYZw wVfaZEZauyZ A yo afJeCBAyVDXWBbAxYBzYyiNuWxBbexEcbeVaAqYz XAjawBzEqDzaafz bTaUaAzWYBxXWZzbazbUwYhqCdV DdzyWafztJajczbt CtYVVfzBgdtvXEGyBxy bdZz C xtczZ SZVfW ZCAx aZYDaa cCyZuVUEBGZ ACbawWXdxxLXa EawAgzOABYFbzTf TszVYaDc fACydzZYdAazSaaygBAYbGzdz yyYBYa Vasay xAz A AVWeYXY aTdYCcZIVxxHcWazZyaWaeYZybYUVZ Bu zXwgACWwzXzBaCwAVddb YB aYBBoGXUAcBZPbzVUGtX DeVduXZGXXtOBwagbXZAcDZIDZvTzA yyuUb AZ'
print(pangram(s))