"""
Ever tried to send a secret message to someone without using the postal service? You could use newspapers to tell your secret. Even if someone finds your message, it's easy to brush them off and that its paranoia and a bogus conspiracy theory. One of the simplest ways to hide a secret message is to use capital letters. Let's find some of these secret messages.

You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.

给你一个文本块。按照出现在文本中的顺序将所有大写字母收集在一个单词中。

例如：文本=“How are you? Eh, ok. Low or Lower? Ohhh.”，如果我们收集所有的大写字母，我们得到的消息“HELLO”。

输入：文本为字符串（unicode）。

输出：秘密消息作为字符串或空字符串。

例：

find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
find_message("hello world!") == ""
    

它是如何使用的： 这是一个使用字符串的简单练习：迭代，识别和连接。


先决条件： 
0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)

"""

def find_message(text):
    """Find a secret message"""
    final = ""
    for up in text:
    	if up.isupper():
    		final += up
    return final


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

