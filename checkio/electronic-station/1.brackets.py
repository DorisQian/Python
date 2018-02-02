"""
“Great!” Exclaimed Sofia. “Now we have the password.”

“To what exactly?” Quipped Nikola.

“Untold treasures, vast riches beyond belief! Gold! Silver! Silicon! Hydraulic Fluid! Anything your heart desires!”

“And you’re going to do what with a password to absolutely nothing?” Nikola smirked.

“Oh... Right...”

Stephen spoke up. “Well, this door back here has a keypad. Only thing is the brackets look pretty busted up. We could try fixing it and then punching in the password?”

“YES! That!” Sofia exclaimed.

You are given an expression with numbers, brackets and operators. For this task only the brackets matter. Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression. If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket. In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.

Input: An expression with different of types brackets as a string (unicode).

Output: A verdict on the correctness of the expression in boolean (True or False).

Example:

checkio("((5+3)*2+1)") == True
checkio("{[(3+1)+2]+}") == True
checkio("(3+{1-1)}") == False
checkio("[1+1]+(2*2)-{3/3}") == True
checkio("(({[(((1)-2)+3)-3]/3}-3)") == False
checkio("2+3") == True

How it is used: When you write code or complex expressions in a mathematical package, you can get a huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.

Precondition: 
There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
0 < len(expression) < 103

“太好了!“索菲亚喊道。“现在我们有了密码。”
“什么?”尼古拉打趣地说。
“不为人知的珍宝，难以置信的巨大财富!”黄金!银!硅!液压油!你心中的欲望!”
你会用密码做什么都不做?”尼古拉傻笑。
“哦…对吧……”
史蒂芬说。这扇门后面有个小键盘。唯一的问题是支架看起来很坏。我们可以试着修复它然后输入密码?
“是啊!那!”索菲亚喊道。
你得到一个带有数字、括号和运算符的表达式。对于这个任务，只有括号很重要。括号里有三种味道:“{}””或“[]”。方括号用于确定范围或限制某些表达式。如果一个括号是打开的，那么它必须以相同类型的关闭括号结束。括号的范围不得与另一个括号相交。在这个任务中，你应该做一个决定，无论是否正确的表达或不基于括号。不要担心操作符和操作数。

输入:以字符串形式(unicode)的不同类型方括号的表达式。
输出:对布尔(真或假)表达式的正确性的判断。

如何使用:当您在一个数学包中编写代码或复杂表达式时，您可能会在出现过多或丢失的括号时感到非常头痛。这个概念可能对您自己的IDE有用。


"""

def checkio(expression):
    brackets = {'}':'{', ')':'(', ']':'['}
    bracketl, bracketr = brackets.values(), brackets.keys()
    arr = []
    for s in expression:
    	if s in bracketl:
    		arr.append(s)
    	elif s in bracketr:
    		if arr and arr[-1] == brackets[s]:
    			arr.pop()
    		else:
    			return False
    return not arr

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
