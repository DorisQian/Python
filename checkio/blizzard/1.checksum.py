'''
Errors during transcription are rather common. Unintentional keystrokes can cause characters to be rearranged, 
dropped or inserted in manually typed text.

Luckily for the robots, you have ways to solve problems like this. Your CheckSum helps to reduce the likelihood 
of errors by introducing a final character that is calculated from the previous characters. With the proper 
reasoning, the final character can always be calculated. This way, when inputs are entered, you can instantly 
verify that the final character matches the character predicted by CheckSum. If the two do not match, the input 
is rejected. The end result is that you would see fewer data entry errors.

How CheckSum Works:
CheckSum reasoning will need map points. This is a definition lookup for how to process the input necessary 
to generate the final character, which will be enable us instantly verify that our input is correct. In other 
words, for each sequence character of the input, we are confident there can only be one possible input, all 
thanks to this final character. 

The steps you must take to obtain the final character are as follows: 
From the rightmost input, traverse from right to left, and apply 'map point character lookup' for even-indexed characters.
Add map point results for even-indexed characters with the unchanged digits from the original number.
Find the remainder of this sum with 10. For an example sum of 67, the remainder is 7. ( 67 modulo 10 = 7 )
Your final character should be 0 if the sum is a multiple-of-10, but it should be 10 minus remainder if the sum 
is not a multiple-of-10.
To generate the 'map point character lookup' table: 
Double the value of a character.
If the product of this doubling operation is greater than 9 (e.g: 7 * 2 = 14), reduce it by summing the digits of 
the product. (i.e., find its digital root. e.g., 10: 1 + 0 = 1, 14: 1 + 4 = 5) Only do this once. Even if the sum 
is greater than 9, leave it alone.
Could you give me an example please?
Okay, take a look this example for a (pretend) account number: "7992739871". We will add final character to it, so 
it looks something like: "7992739871x," with x being the final character-to-be-found. 

Here is what a 'map point character lookup' table looks like for 0 through 9: 

Digits	:	0	1	2	3	4	5	6	7	8	9
Doubled	:	0	2	4	6	8	10	12	14	16	18
Reduced	:	0	2	4	6	8	1+0	1+2	1+4	1+6	1+8
Map Point	:	0	2	4	6	8	1	3	5	7	9

And here is how we will obtain final character: 

Index	:	0	1	2	3	4	5	6	7	8	9
Reversed	:	1	7	8	9	3	7	2	9	9	7
From table	:	2		7		6		4		9		Total: 67
Unchanged	:		7		9		7		9		7
Final Character	:	10 - ( 67 % 10 ) = 10 - 7 =	3

So, we can release the account number as follows: 799 273 9871 3 
Alphanumeric Input
To make this more interesting, we can use alphanumeric input, which is a possible combination of 10 digits and 26 capital letters. It means that we will have to upgrade our map point to support letters. How we achieve that? We use each character's ASCII value to help us determine the character sequence. For example: 'A' has an ASCII value 65. To determine its sequence in our map, we need to substract 48. 

For this example, 'A' is 7 since 65 - 48 = 17, 17 * 2 = 34 and 3 + 4 = 7. (Remember to only apply 'map point character lookup' to even-indexed characters. If 'A' is an odd-indexed character, its value is 17) 
Alphanumeric Example
Alright, we have another example here: "139MT". Let's see how we can obtain the final character... 

Reversed	:	T	M	9	3	1
Sum of digits	:	9	29	9	3	2	Total: 52
Final Character	:	10 - ( 52 % 10 ) = 10 - 2 =	8
Here is detail for how we do it:

T:  ASCII of 84, 84 - 48 = 36, 36 * 2 = 72, and 7 + 2 = 9
M:  ASCII of 77, and 77 - 48 = 29
9:  from map point is, 9, or ASCII of 57, 57 - 48 = 9, 9 * 2 = 18, and 1 + 8 = 9
3:  just 3, or ASCII of 51, and 51 - 48 = 3
1:  from map point is, 2, or ASCII of 49, 49 - 48 = 1, and 1 * 2 = 2
Sum of digits is 52, since 9 + 29 + 9 + 3 + 1 = 52
Final character is 8, since 10 - ( 52 % 10 ) = 10 - 2 = 8

Now it's time to test your CheckSum module!
Input: Unsanitized numeric or alphanumeric due to formatting purpose

Output: List of its final character and sum of digits

Example:

checkio("799 273 9871") == ["3", 67]
checkio("139-MT") == ["8", 52])
checkio("123") == ["0", 10])
checkio("999_999") == ["6", 54])
checkio("+61 820 9231 55") == ["3", 37])
checkio("VQ/WEWF/NY/8U") == ["9", 201])


转录过程中的错误相当普遍。无意的击键可能导致字符重新排列，丢弃或插入手动输入的文本中。

幸运的是，对于机器人，你有办法解决这样的问题。您的CheckSum通过引入从以前的字符计算出来的最终字符来帮助减少错误的可能性。
通过适当的推理，最终的角色总是可以计算出来的。这样，当输入输入时，您可以立即验证最终字符与由CheckSum预测的字符匹配。
如果两者不匹配，则输入被拒绝。最终的结果是您会看到更少的数据输入错误。

CheckSum如何工作：
CheckSum推理将需要地图点。这是一个定义查找如何处理生成最终字符所需的输入，这将使我们能够立即验证我们的输入是否正确。
换句话说，对于输入的每个序列字符，我们确信只能有一个可能的输入，这要归功于这个最终字符。

您必须采取的步骤来获得最终字符如下：
从最右侧的输入中，从右向左遍历，并将“地图点字符查找”应用于偶数索引字符。
添加偶数索引字符的地图点结果，其中原始数字的位数不变。
以10为单位查找余数。对于67的示例和，余数为7.（67模10 = 7）
如果总和为10的倍数，则最终字符应该为0，但如果总和不是10的倍数，则应该是10减去余数。
要生成'地图点字符查找'表：
加倍角色的价值。
如果这种倍增操作的结果大于9（例如：7 * 2 = 14），则通过将产品数字相加来减少它。 
（即找到它的数字根，例如，10：1 + 0 = 1,14：1 + 4 = 5）只做一次。即使总和大于9，也不要管它。
你能举个例子吗？
好的，看看这个例子（假装）帐号：“7992739871”。我们将添加最终字符，所以它看起来像：“7992739871x”，其中x是最终要找到的字符。

以下是0到9的“地图点字符查找”表：


所以，我们可以发布账号如下：799 273 9871 3
字母数字输入
为了使这更有趣，我们可以使用字母数字输入，这是一个可能的10位数字和26个大写字母的组合。 
这意味着我们必须将我们的地图点升级为支持信件。 我们如何做到这一点？ 我们使用每个字符的ASCII值来帮助我们确定字符序列。 
例如：'A'的ASCII值为65.为了确定它在地图上的顺序，我们需要减去48。

对于这个例子，'A'是7，因为65 - 48 = 17，17 * 2 = 34和3 + 4 = 7（记住只应用'地图点字符查找'到偶数索引字符。 
一个奇怪的索引字符，它的值是17）
字母数字例子
好的，我们在这里有另一个例子：“139MT”。 让我们看看我们如何才能获得最终的角色......

现在是时候测试您的CheckSum模块了！
输入：由于格式化目的，未加数字或字母数字

输出：最终字符和数字总和的列表
'''

def checkio(data):
	char = []
	for n in data:
		if n.isdigit():
			char.insert(0, int(n))
		elif n.isalpha():
			char.insert(0, n)
	change = []
	for i in range(0, len(char)):
		if type(char[i]) == int:
			k = char[i]
		else:
			k = ord(char[i]) - 48
		if i % 2 == 0:
			num = k * 2
			if int(num) > 9:
				change.append(sum(int(j) for j in str(num)))
			else:
				change.append(num)
		else:
			change.append(k)
	total = sum(change)
	final = 0 if total % 10 == 0 else 10 - (total % 10)
	return [str(final), total]
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert (checkio("799 273 9871") == ["3", 67]), "First Test"
    assert (checkio("139-MT") == ["8", 52]), "Second Test"
    assert (checkio("123") == ["0", 10]), "Test for zero"
    assert (checkio("999_999") == ["6", 54]), "Third Test"
    assert (checkio("+61 820 9231 55") == ["3", 37]), "Fourth Test"
    assert (checkio("VQ/WEWF/NY/8U") == ["9", 201]), "Fifth Test"

    print("OK, done!")
