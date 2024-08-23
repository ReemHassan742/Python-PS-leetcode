from fractions import Fraction
import re

class Solution:
    def fractionAddition(self, expression: str) -> str:
        total = Fraction(0)
        fractions = re.findall(r'[+-]?\\d+/\\d+', expression)
        for frac in fractions:
            total += Fraction(frac)
        if total.denominator == 1:
            return f\{total.numerator}/1\
        else:
            return f\{total.numerator}/{total.denominator}\
