"""
We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to see all other solutions you should change the filter.

Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. The first ten Roman numerals are:

I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:

Numeral	Value
I	1 (unus)
V	5 (quinque)
X	10 (decem)
L	50 (quinquaginta)
C	100 (centum)
D	500 (quingenti)
M	1,000 (mille)
More additional information about roman numerals can be found on the Wikipedia article.

For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.

Example:

checkio(6) == 'VI'
  checkio(76) == 'LXXVI'
  checkio(13) == 'XIII'
  checkio(44) == 'XLIV'
  checkio(3999) == 'MMMCMXCIX'
  

How it is used: This is an educational task that allows you to explore different numbering systems. Since roman numerals are often used in the typography, it can alternatively be used for text generation. The year of construction on building faces and cornerstones is most often written by Roman numerals. These numerals have many other uses in the modern world and you read about it here... Or maybe you will have a customer from Ancient Rome ;-)

Precondition: 0 < number < 4000

我们已经准备了一套编辑器的选择方案。在你解决了任务之后，你将会看到他们。为了看到所有其他的解决方案，你应该改变过滤器。
罗马数字来自古罗马的编号系统。它们是根据字母表中的特定字母组合而成的，这些字母组合起来表示它们的值的和(或在某些情况下是不同的)。前十个罗马数字是:
I,II,III,IV,V,VI,VII,VIII,IX和X。
罗马数字系统是十进制的，但不是直接的位置，也不包括零。罗马数字是基于这七个符号的组合:
数值

I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)
关于罗马数字的更多信息可以在维基百科上找到。
对于这个任务，您应该使用从1到3999的指定整数值返回一个罗马数字。

输入:一个数字作为整数。
输出:罗马数字作为字符串。

如何使用:这是一个教育任务，允许您探索不同的编号系统。由于罗马数字经常用于印刷，它也可以用于文本生成。建筑在建筑物的表面和基石上的年份通常是罗马数字。这些数字在现代世界有很多其他用途，你在这里读到过……或者你可能会有一个来自古罗马的客户;
"""

def checkio(data):

  ro_dic = { 
      1 : 'I', 
      5 : 'V',
      10 : 'X',
      50 : 'L',
      100 : 'C',
      500 : 'D',
      1000 : 'M'
  }
  li = [1000, 100, 10, 1]
  num = data
  roman = ''
  for n in li:
    tu = divmod(num, n)
    if tu[0] >= 5 and tu[0] != 9:
      roman += ro_dic[5*n] + ro_dic[n] * (tu[0] - 5)
    if tu[0] == 4:
      roman += ro_dic[n] + ro_dic[5*n]
    if tu[0] == 9:
      roman += ro_dic[n] + ro_dic[10*n]
    if tu[0] < 4:
      roman += ro_dic[n] * tu[0]
    num = tu[1]
  print(roman)
  return roman
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'