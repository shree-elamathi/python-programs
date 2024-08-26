'''
Given two strings pattern and str which may be of different size, You have to return 1 if the wildcard pattern
i.e. pattern, matches with str else return 0. All characters of the string str and pattern always belong to the
Alphanumeric characters.
The wildcard pattern can include the characters ? and *
‘?’ – matches any single character.
‘*’ – Matches any sequence of characters (including the empty sequence).
Note: The matching should cover the entire str (not partial str).
'''
class Solution:
    def wildCard(self, pattern: str, string: str) -> int:
        def match(p_idx, s_idx):
            # Base cases
            if p_idx == len(pattern) and s_idx == len(string):
                return 1
            if p_idx == len(pattern):
                return 0
            if s_idx == len(string):
                return 1 if all(x == '*' for x in pattern[p_idx:]) else 0

            # Recursive cases
            if pattern[p_idx] == '*':
                # Two recursive calls:
                # 1. '*' matches zero characters (move to next pattern character)
                # 2. '*' matches one or more characters (move to next string character)
                return match(p_idx + 1, s_idx) or match(p_idx, s_idx + 1)
            elif pattern[p_idx] == '?' or pattern[p_idx] == string[s_idx]:
                # '?' matches one character or exact match
                return match(p_idx + 1, s_idx + 1)
            else:
                return 0

        # Initial call with the start of both pattern and string
        return match(0, 0)

pattern = "ba*a?"
str = "baaabab"
print(Solution().wildCard(pattern,str))

#fun 1
'''
*a?
abab
1a-> a? , abab
1aa -> ? , bab
1aaa -> null , ab
1aaaa -> False
1b -> a? , bab
1ba -> False
1c -> *a? , bab
1ca -> a? , bab
1caa -> Flase
1cb -> a? , ab
1cba -> ? , b, True 
1cc -> *a? , ab
1cca -> a? , ab
1ccb -> a? , b
1ccc -> a? , ab
fun 2
a?
abab

fun 3
a?
aabab
'''