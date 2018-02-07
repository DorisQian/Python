"""
In mathematics and mathematical logic, Boolean algebra is a sub-area of algebra in 
which the values of the variables are true or false, typically denoted with 1 or 0 
respectively. Instead of elementary algebra where the values of the variables are 
numbers and the main operations are addition and multiplication, the main operations 
of Boolean algebra are the conjunction (denoted ∧), the disjunction (denoted ∨) and 
the negation (denoted ¬).

In this mission you should implement some boolean operations:
- "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1 and x ∧ y = 0 otherwise.
- "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0 and x ∨ y = 1 otherwise.
- "implication" (material implication) denoted x→y and can be described as ¬ x ∨ y. If x 
is true then the value of x → y is taken to be that of y. But if x is false then the value
 of y can be ignored; however the operation must return some truth value and there are only 
 two choices, so the return value is the one that entails less, namely true.
- "exclusive" (exclusive or) denoted x ⊕ y and can be described as (x ∨ y)∧ ¬ (x ∧ y). It 
excludes the possibility of both x and y. Defined in terms of arithmetic it is addition mod 
2 where 1 + 1 = 0.
- "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y). It's true just when x and
 y have the same value.
Here you can see the truth table for these operations:

 x | y | x∧y | x∨y | x→y | x⊕y | x≡y |
--------------------------------------
 0 | 0 |  0  |  0  |  1  |  0  |  1  |
 1 | 0 |  0  |  1  |  0  |  1  |  0  |
 0 | 1 |  0  |  1  |  1  |  1  |  0  |
 1 | 1 |  1  |  1  |  1  |  0  |  1  |
--------------------------------------
You are given two boolean values x and y as 1 or 0 and you are given an operation name as 
described earlier. You should calculate the value and return it as 1 or 0.

Input: Three arguments. X and Y as 0 or 1. An operation name as a string.

Output: The result as 1 or 0.

Example:

boolean(1, 0, "conjunction") == 0
boolean(0, 1, "exclusive") == 1

How it is used: Here you will learn how to work with boolean values and operators. You even 
get to think about numbers as booleans.

Precondition: x in (0, 1)
y in (0, 1)
operation in ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

在数学和数学逻辑中，布尔代数是代数的一个子领域，其中变量的值为真或假，通常表示为1或0。相反的初
等代数变量的值是数字和主要的操作是加法和乘法,布尔代数的主要操作是连词(∧)表示,脱节(∨表示)和否定(¬)表示。

在这个任务中，您应该实现一些布尔操作:
——“连词”表示x∧y,满足x∧y = 1如果x = y = 1,x∧y = 0。
——“析取”表示x∨y,满足x∨y = 0如果x = y = 0,x∨y = 1。
——“暗示”(实质蕴涵)表示x→y和可以被描述为¬x y∨。如果是真的,那么x的值→y,y的。但是,如果x是假的那么
y的值可以忽略;但是操作必须返回一些真值，只有两个选择，所以返回值是需要更少的值，也就是true。
——“独家”(异或)表示x⊕y和可以被描述为(x∨y)∧¬(x∧y)。它不包括两个x和y的可能性。定义在算术方面除了
国防部2 1 + 1 = 0。
——“等价”表示x≡y,可以被描述为¬(x⊕y)。这是真的只是当x和y都包含相同的值。
在这里你可以看到这些操作的真值表:
给定两个布尔值x和y为1或0，并给出一个操作名称，如前面所述。您应该计算值并将其返回为1或0。

输入:三个参数。X和Y为0或1。一个操作名称作为字符串。
输出:结果为1或0。

如何使用:这里您将学习如何使用布尔值和操作符。你甚至可以把数字当作布尔值。
"""

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
	def conjunction(operation):
		if x == y == 1:
			return 1
		else:
			return 0
	def disjunction(operation):
		if x == y == 0:
			return 0
		else:
			return 1
	if operation == 'conjunction':
		return conjunction('conjunction')
	if operation == 'disjunction':
		return disjunction('disjunction')
	if operation == 'implication':
		if x == 1:
			return y
		else:
			return 1
	if operation == 'exclusive':
		a = disjunction(disjunction)
		b = conjunction(conjunction)
		x , y = a, not b
		return conjunction('conjunction')
	if operation == 'equivalence':
		if x == y :
			return 1
		else:
			return 0

	
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert boolean(1, 0, "conjunction") == 0, "and"
    assert boolean(1, 0, "disjunction") == 1, "or"
    assert boolean(1, 1, "implication") == 1, "material"
    assert boolean(0, 1, "exclusive") == 1, "xor"
    assert boolean(0, 1, "equivalence") == 0, "same?"
