'''
The Vigenère cipher is a method of encrypting alphabetic text by using a series of 
different Caesar ciphers based on the letters of a keyword. It is a simple form of polyalphabetic substitution.

In the Vigenère cipher each letter of a message is shifted along some number of places 
with different shift values. To encrypt, a table of alphabets can be used, termed a 
tabula recta, Vigenère square, or Vigenère table. It consists of the alphabet written 
out 26 times in different rows, each version of the alphabet is shifted cyclically to 
the left compared to the previous alphabet. At different points in the encryption process, 
the cipher uses a different alphabet from one of the rows. The alphabet used at each point 
depends on a repeating keyword.

\  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
 \----------------------------------------------------
A| A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
B| B C D E F G H I J K L M N O P Q R S T U V W X Y Z A
C| C D E F G H I J K L M N O P Q R S T U V W X Y Z A B
D| D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
E| E F G H I J K L M N O P Q R S T U V W X Y Z A B C D
F| F G H I J K L M N O P Q R S T U V W X Y Z A B C D E
G| G H I J K L M N O P Q R S T U V W X Y Z A B C D E F
H| H I J K L M N O P Q R S T U V W X Y Z A B C D E F G
I| I J K L M N O P Q R S T U V W X Y Z A B C D E F G H
J| J K L M N O P Q R S T U V W X Y Z A B C D E F G H I
K| K L M N O P Q R S T U V W X Y Z A B C D E F G H I J
L| L M N O P Q R S T U V W X Y Z A B C D E F G H I J K
M| M N O P Q R S T U V W X Y Z A B C D E F G H I J K L
N| N O P Q R S T U V W X Y Z A B C D E F G H I J K L M
O| O P Q R S T U V W X Y Z A B C D E F G H I J K L M N
P| P Q R S T U V W X Y Z A B C D E F G H I J K L M N O
Q| Q R S T U V W X Y Z A B C D E F G H I J K L M N O P
R| R S T U V W X Y Z A B C D E F G H I J K L M N O P Q
S| S T U V W X Y Z A B C D E F G H I J K L M N O P Q R
T| T U V W X Y Z A B C D E F G H I J K L M N O P Q R S
U| U V W X Y Z A B C D E F G H I J K L M N O P Q R S T
V| V W X Y Z A B C D E F G H I J K L M N O P Q R S T U
W| W X Y Z A B C D E F G H I J K L M N O P Q R S T U V
X| X Y Z A B C D E F G H I J K L M N O P Q R S T U V W
Y| Y Z A B C D E F G H I J K L M N O P Q R S T U V W X
Z| Z A B C D E F G H I J K L M N O P Q R S T U V W X Y

To see how this works, lets take, the message "DONTWORRYBEHAPPY" and the keyword "CHECKIO". 
Write the message and the keyword below, then shift each letter in the message related by 
corresponded letter in the repeating keyword.

Message:   DONTWORRYBEHAPPY
Key:       CHECKIOCHECKIOCH
Encrypted: FVRVGWFTFFGRIDRF

Vigenère can also be viewed algebraically. If the letters A–Z are taken to be the numbers 0–25, 
and addition is performed modulo 26, then Vigenère encryption E using the key K can be written as:
Ci = Ek(Mi) = (Mi + Ki) % 26

Now, consider the following scenario: you and your friend use that cipher for correspondence and 
you've forgot the key. But, to your luck, you have an archive with encrypted and decrypted message. 
With that you can find the key and decrypt the new fresh message from your friend.

Input: Three arguments. An old decrypted message, an old encrypted message and a new encrypted 
message as strings (unicode for py2).

Output: The new decrypted message as a string.

Example:

decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE"
    
How it is used: This is a simple cipher which had widespread usage in olden times. As we can see, 
the key is can be easily calculated if you know a little bit about the content of the message.

Precondition:
all(re.match("[A-Z]+\Z", text) for text in args)
len(key) ≤ len(old_encrypted)
2 * len(key) <= len(old_encrypted) < len(new_encrypted) or len(new_encrypted) <= len(old_encrypted)

Vigenère密码是一种通过使用一系列字符来加密字母文本的方法
基于关键字字母的不同凯撒密码。 它是一种简单的多肽替代形式。

在Vigenère密码中，消息的每个字母都沿着一些位置移动
具有不同的移位值。 要加密，可以使用一个字母表，称为a
tabula recta，Vigenère广场或Vigenère表。 它由书写的字母组成
在不同的行中出26次，每个版本的字母都循环移动到
与以前的字母表相比较。 在加密过程的不同点上，
密码使用一行中的不同字母。 每个点使用的字母表
取决于重复的关键字。

要看看它是如何工作的，让我们看看“DONTWORRYBEHAPPY”和关键字“CHECKIO”。
在下面写下消息和关键字，然后移动消息中的每个字母
在重复关键字中对应的字母。

消息：DONTWORRYBEHAPPY
密钥：CHECKIOCHECKIOCH
加密：FVRVGWFTFFGRIDRF

Vigenère也可以代数形式查看。如果字母A-Z被认为是数字0-25，
并且以模26执行加法，则使用密钥K的Vigenère加密E可以写为：
Ci = Ek（Mi）=（Mi + Ki）％26

现在，考虑以下情况：你和你的朋友使用密码进行通信和
你忘了钥匙。但是，为了您的运气，您拥有加密和解密邮件的存档。
有了这个，你可以找到密钥并解密来自朋友的新鲜新消息。

输入：三个参数。旧的解密消息，旧的加密消息和新的加密消息
消息作为字符串（py2的unicode）。

输出：新的解密消息作为一个字符串。

例：

decode_vigenere（'HELLO'，'OIWWC'，'ICP'）==“BYE”
    
它是如何使用的：这是一个简单的密码，在古代有广泛的使用。我们可以看到，
如果您知道一些关于消息内容的信息，则可以轻松计算出关键字。
'''