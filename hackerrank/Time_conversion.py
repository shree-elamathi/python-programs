#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
#Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
#- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
def converttime(s):
    if s[-2:]=='AM':
        if int(s[:2])==12:
            return ("00"+s[2:8])
        else:
            return (s[:8])
    else:
        if int(s[:2]) == 12:
            return (s[:8])
        else:
            x=str(int(s[:2])+12)
            return (x+s[2:8])

s='07:05:45PM'
print(converttime(s))