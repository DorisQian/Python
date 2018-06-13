'''
For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, 
such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"}
 -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.
Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False
    
How it is used: Here you can learn about iterating through set type and string data type functions.

Precondition: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)


对于语言培训，我们的机器人想了解后缀。

在这个任务中，你会得到一组小写的单词。 检查是否有一对单词，
这样一个词就是另一个词的结尾（另一个词的后缀）。 例如：{“hi”，“hello”，“lo”}
  - “lo”是“hello”的结尾，所以结果是True。

输入：字作为一组字符串。
输出：True或False，作为布尔值。

它是如何使用的：在这里，您可以了解如何遍历集合类型和字符串数据类型函数。
'''