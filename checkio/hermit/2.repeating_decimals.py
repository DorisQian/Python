'''
In mathematics, a repeating decimal is a way of representing a rational number. A decimal representation of a number is called a repeating decimal if at some point there is some finite sequence of digits that is repeated infinitely. For example: the decimal representation of 1/3 = 0.3333333… or 0.(3) becomes periodic just after the decimal point, repeating the single-digit sequence "3" infinitely. Here is another example is 27/26 = 1.0384615384615385… or 1.0(384615), where the decimal becomes periodic after the second digit past the decimal point, repeating the sequence "384615" infinitely. Rational numbers are numbers which can be expressed in the form a/b where a and b are integers and b is not zero. This form is known as a common fraction. Read more about this at Wikipedia.

You should write a function for the converting a fraction into decimal representation. If the decimal is repeating, you should represent it using the brackets format seen above. You are given two integers, the first is the fractions numerator and the second is its denominator. For this task, you will need to return the fraction in decimal representation as a string. The integer results (as 0 or 2) must be ended with a dot.

Fraction	Ellipsis			Brackets
1/3			0.333333...			0.(3)
5/3			1.666666...			1.(6)
3/8			0.375				0.375
7/11		0.636363...			0.(63)
29/12		2.41666666...		2.41(6)
11/7		1.571428571428...	1.(571428)

Input: Two arguments. A numerator and a denominator as integers.

Output: The decimal representation of the fraction in the bracket format as a string.

Example:

convert(1, 3) == "0.(3)"
convert(5, 3) == "1.(6)"
convert(3, 8) == "0.375"
convert(7, 11) == "0.(63)"
convert(29, 12) == "2.41(6)"
convert(11, 7) == "1.(571428)"
convert(0, 117) == "0."
convert(4, 2) == "2."

How it is used: This is the important part for mathematical software. And of you need to help your children with homework.

Precondition: 
0 ≤ numerator ≤ 1000
1 ≤ denominator ≤ 1000
'''

def convert(numerator, denominator):
    return "0.(3)"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert convert(1, 3) == "0.(3)", "1/3 Classic"
    assert convert(5, 3) == "1.(6)", "5/3 The same, but bigger"
    assert convert(3, 8) == "0.375", "3/8 without repeating part"
    assert convert(7, 11) == "0.(63)", "7/11 prime/prime"
    assert convert(29, 12) == "2.41(6)", "29/12 not and repeating part"
    assert convert(11, 7) == "1.(571428)", "11/7 six digits"
    assert convert(0, 117) == "0.", "Zero"
