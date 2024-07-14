'''
Given a string formula representing a chemical formula, return the count of each atom.
The atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the
name.
One or more digits representing that element's count may follow if the count is greater than 1. If the count is 1, no
digits will follow.
For example, "H2O" and "H2O2" are possible, but "H1O2" is impossible.
Two formulas are concatenated together to produce another formula.
For example, "H2O2He3Mg4" is also a formula.
A formula placed in parentheses, and a count (optionally added) is also a formula.
For example, "(H2O2)" and "(H2O2)3" are formulas.
Return the count of all elements as a string in the following form: the first name (in sorted order), followed by its
count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that
count is more than 1), and so on.
The test cases are generated so that all the values in the output fit in a 32-bit integer.
'''
def count_of_atoms(formula):
    from collections import defaultdict
    import re
    def parse_formula(formula):
        tokens = re.findall(r'([A-Z][a-z]*|\d+|[()])', formula)
        stack = [defaultdict(int)]
        i = 0
        while i < len(tokens):
            token = tokens[i]
            if token == '(':
                stack.append(defaultdict(int))
                i += 1
            elif token == ')':
                temp_dict = stack.pop()
                i += 1
                i = parse_multiplier(tokens, i, temp_dict, stack)
            elif token.isdigit():
                raise ValueError("Numbers should not appear alone")
            else:
                element = token
                i += 1
                i = parse_element_count(tokens, i, element, stack[-1])
        return stack.pop()
    def parse_multiplier(tokens, i, temp_dict, stack):
        multiplier = 1
        if i < len(tokens) and tokens[i].isdigit():
            multiplier = int(tokens[i])
            i += 1
        for elem, cnt in temp_dict.items():
            stack[-1][elem] += cnt * multiplier
        return i
    def parse_element_count(tokens, i, element, current_dict):
        count = 1
        if i < len(tokens) and tokens[i].isdigit():
            count = int(tokens[i])
            i += 1
        current_dict[element] += count
        return i

    parsed_dict = parse_formula(formula)

    result = []
    for elem in sorted(parsed_dict.keys()):
        count = parsed_dict[elem]
        if count == 1:
            result.append(elem)
        else:
            result.append(f"{elem}{count}")
    return ''.join(result)

formula="H2O"
print(count_of_atoms(formula))