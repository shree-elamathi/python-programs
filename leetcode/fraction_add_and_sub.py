'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation
result in string format.
The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a
fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.
'''
import re
from math import gcd
from functools import reduce

class Solution:
    def lcm(self, x, y):
        return abs(x * y) // gcd(x, y)

    def fractionAddition(self, expression: str) -> str:
        # Find all fractions in the expression
        fractions = re.findall(r'[+-]?\d+/\d+', expression)

        # Initialize numerators and denominators lists
        numerators = []
        denominators = []

        for frac in fractions:
            if frac[0] == '+':
                frac = frac[1:]
            num, den = map(int, frac.split('/'))
            numerators.append(num)
            denominators.append(den)

        # Calculate the least common denominator (LCD)
        lcd = reduce(self.lcm, denominators)

        # Adjust the numerators to the common denominator
        adjusted_numerators = [
            numerators[i] * (lcd // denominators[i]) for i in range(len(numerators))
        ]

        # Sum the adjusted numerators
        final_numerator = sum(adjusted_numerators)

        # Simplify the final result
        divisor = gcd(final_numerator, lcd)
        final_numerator //= divisor
        final_denominator = lcd // divisor

        # Handle integer results
        if final_denominator == 1:
            return f"{final_numerator}/1"
        else:
            return f"{final_numerator}/{final_denominator}"

# Example usage
solution = Solution()
expression = "1/2+1/3-1/4"
result = solution.fractionAddition(expression)
print(result)  # Output: "7/12"

