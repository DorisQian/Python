'''
Let's look at the AMSCO cipher. This is a positional cipher with exchanges. 
You can easily encode or decode a message with a pen and paper, that is of 
course, if you know the key.

The key is represented as a number that consist of unique digits from 1 to 
N. N is a length of the key. To encode message we should write a message in 
a matrix with N columns. The matrix is written row by row. In this process, 
one or two characters are alternately recorded in a field. One or two characters 
alternate in rows and in columns too (like a chessboard). The first element is 
single letter field (this is the arrangement for this mission). The last field 
can have single characters if there are not enough. Columns are then numbered 
with digits from the key in order. For example: using the key 312, the first 
column will be 3, the second is 1 and the third is 2. Lastly, you will write 
all characters in the columns as they were numbered in the most recent step. 
All white spaces and punctuation symbols are excluded while letters are in lowercase.

Let's look at this with an example. The message "Lorem ipsum dolor sit amet". 
And the key is 4123. The cut message is "loremipsumdolorsitamet". In matrix form it will be:

   4   1   2   3
   l  or   e  mi
  ps   u  md   o
   l  or   s  it
  am   e   t

Now write the columns as they are numbered in the ascending order - "oruore", 
"emdst", "mioit", "lpslam". The encoded message is "oruoreemdstmioitlpslam".

You are given an encoded message and the key. Your mission is to decode the 
message. Of course in the cut version.

Input: Two arguments. A message as a string (unicode) and a key as an integer.

Output: The decoded message as a string.

Example:

decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet"


How it is used: For any cipher, it is important to realize both parts - encoding 
and decoding. This way, even if you know only one part of the cipher, you can finalize an implementation.

Precondition: 4 ≤ len(str(key))
int(len(str(key)) * 1.5) ≤ len(message)
re.match("\w+$", message)

让我们看看AMSCO密码。这是一个交换的位置密码。
你可以用笔和纸很容易地编码或解码信息，这是
当然，如果你知道的关键。

密钥表示为由1到的唯一数字组成的数字
N. N是密钥的长度。为了编码消息，我们应该写一条消息一个有N列的矩阵。矩阵逐行写入。在这个过程中，
一个或两个字符交替记录在一个字段中。一个或两个字符
在行和列中交替（如棋盘）。第一个元素是单个字母字段（这是这个任务的安排）。最后一场
如果没有足够的话可以有单个字符。列然后编号
与按键中的数字顺序。例如：使用键312，第一个列将是3，第二个是1，第三个是2.最后，你会写
在最近的步骤中编号的列中的所有字符。所有的空格和标点符号被排除在外，而字母是小写的。

我们来看一个例子。消息“Lorem ipsum dolor sit amet”。
关键是4123.剪切的消息是“loremipsumdolorsitamet”。矩阵形式将是：

现在按升序编号列 - “oruore”，
“emdst”，“mioit”，“lpslam”。 编码的消息是“oruoreemdstmioitlpslam”。

给你一个编码信息和密钥。 你的任务是解码信息。 当然在剪切版本。

输入：两个参数。 作为字符串（unicode）的消息和作为整数的密钥。
输出：解码的消息作为一个字符串。


如何使用：对于任何密码，重要的是要实现两个部分 - 编码
和解码。 这样，即使只知道密码的一部分，也可以最终确定一个实现。
'''