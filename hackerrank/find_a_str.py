'''
In this challenge, the user enters a string and a substring. You have to print the number of times that the substring
occurs in the given string. String traversal will take place from left to right, not from right to left.
NOTE: String letters are case-sensitive.
'''


def count_substring(string, sub_string):
    l = sub_string[0]
    length = len(sub_string)
    c = 0
    for i in range(len(string) - length + 1):
        if string[i] == l:
            if string[i:i + length] == sub_string:
                c += 1

    return c


string = "ABCDCDC"
sub_string = "CDC"
print(count_substring(string, sub_string))
