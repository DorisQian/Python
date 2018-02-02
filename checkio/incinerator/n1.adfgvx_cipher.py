'''
The ADFGVX Cipher was a field cipher used by the German Army on the Western 
Front during World War I. ADFGVX was in fact an extension of an earlier cipher 
called ADFGX. Invented by Colonel Fritz Nebel and introduced in March 1918, the 
cipher was a fractionating transposition cipher which combined a modified Polybius 
square with a single columnar transposition. The cipher is named after the six 
possible letters used in the ciphertext: A, D, F, G, V and X. These letters were 
chosen deliberately because they sound very different from each other when transmitted 
via Morse code. The intention was to reduce the possibility of operator error.

Let's examine the way cipher works using an example. Our message is "I am going." 
First we must clean and process the message: "iamgoing". It should contain only digits 
and latin letters in lowercase. All other characters (such as punctuation) are skipped. 
Then we fill the "adfgvx" table with our secret alphabet "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g".

\  A D F G V X
 \------------
A| d h x m u 4
D| p 3 j 6 a o
F| i b z v 9 w
G| 1 n 7 0 q k
V| f s l y c 8
X| t r 5 e 2 g

Using this square, the message is converted to fractionated form (row-column):

i  a  m  g  o  i  n  g
FA DV AG XX DX FA GD XX

Then, a new table is created with a key as the heading. Let's use 'cipher' as the key. 
If the key contains duplicated letters, the first one should be used. So, "checkio" becomes "chekio".

c i p h e r
-----------
F A D V A G
X X D X F A
G D X X

The columns are sorted alphabetically based on the keyword and the table changes to the new form.

c e h i p r
-----------
F A V A D G
X F X X D A
G   X D X

Then it is read off in columns, in keyword order and the result is "FXGAFVXXAXDDDXGA".

You should write two functions - "encode" and "decode". Each function receives a message 
(ciphered or opened), a secret alphabet and a keyword. The "encode" function processes and 
encrypts a message. The "decode" function decrypts the encoded message (of course in the processed version).

Input: Three arguments. A message, a secret alphabet and a keyword as strings.

Output: The processed message as a string.

Example:

encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'FXGAFVXXAXDDDXGA'
decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') == 'iamgoing'
    
How it is used: This mission gives you a little practice in working with data structures and 
positional ciphers. These ciphers could be used for your secret agent correspondence should you have no computer access.

Precondition:
re.match("[a-z]+\Z", keyword)
re.match("[a-z0-9]+\Z", secret_alphabet)
len(set(secret_alphabet)) == len(secret_alphabet)

ADFGVX密码是德军在西方使用的一种现场密码
第一次世界大战期间的阵线.ADFGVX实际上是早期密码的延伸
称为ADFGX。由Fritz Nebel上校发明，并于1918年3月推出
密码是一个分数转置密码，它结合了一个修改后的Polybius
正方形与一个唯一柱状调换。密码以六位命名
A，D，F，G，V和X中可能使用的字母
故意选择，因为它们在传输时听起来非常不同
通过莫尔斯电码。目的是为了减少操作员错误的可能性。

让我们用一个例子来看密码的工作方式。我们的信息是“我要去”。
首先，我们必须清理和处理信息：“iamgoing”。它应该只包含数字
和拉丁字母小写。所有其他字符（如标点符号）都会跳过。
然后我们用我们的秘密字母表“dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g”填充“adfgvx”表。

使用这个正方形，消息被转换成分割形式（行列）：

我要去
FA DV AG XX DX FA GD XX

然后，用一个键作为标题创建一个新表。让我们使用“密码”作为关键。
如果密钥包含重复的字母，则应使用第一个字母。所以，“checkio”变成了“chekio”。

根据关键字按字母顺序对列进行排序，并将表更改为新的表单。

然后按列关键字顺序读取结果为“FXGAFVXXAXDDDXGA”。

你应该写两个函数 - “编码”和“解码”。每个功能都收到一条消息
（加密或打开），秘密字母表和关键字。 “编码”功能处理和
加密一条消息。 “解码”功能解密编码的消息（当然在处理版本）。

输入：三个参数。一条消息，一个秘密字母表和一个关键字作为字符串。

输出：处理的消息作为字符串。
   
它是如何使用的：这个任务给你一些实践与数据结构和
位置密码。如果你没有电脑访问，这些密码可以用于你的特工通信。
'''