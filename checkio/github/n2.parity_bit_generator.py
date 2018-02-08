'''
During the last I3E Industrial Conference in Robo-city, a new version of the communication protocol R2HI 2.0 (Robot-to-Human Interface) was adopted. A new version of the R2HI interface extends the existing one by adding an error detection feature. This feature allows us to send data to robots located a long distance away near some human settlements with higher level of reliability. During the data transmission some bits can be substituted due to external events (radiation impact, different noises etc.). In R2HI 2.0 simple parity bit check technique is proposed.

R2HI 2.0 interface specification:
1. Data packages (message) are represented as a list of int numbers (0 ≤ number ≤ 255):
[d1, d2, d3, ..., dn], where d1 is the first letter in message
2. Each decimal number is an ASCII-code of respective characters in binary + parity bit
Example:
    Chr | Dec  |   Bin   |P|  Bin + P | Dec
    ---------------------------------------
    'P' |  80  | 1010000 |0| 10100000 | 160
    'y' | 121  | 1111001 |1| 11110011 | 243
    't' | 116  | 1110100 |0| 11101000 | 232
    'h' | 104  | 1101000 |1| 11010001 | 209
    'o' | 111  | 1101111 |0| 11011110 | 222
    'n' | 110  | 1101110 |1| 11011101 | 221

        Message = [160, 243, 232, 209, 222, 221]
    
You have to implement an "R2HI 2.0 translator/analyzer" that translates a received data package (list of int) into a string message. Before the translation, erroneous numbers must be removed from the package (list). Erroneous means the decimal value contains a wrong (odd) number of '1' in a binary form:

'P' → 80 → 1010000 + 0 → 10100000 → ...10110000... → 10110000 (Erroneous, 4-th bit was inverted)
Notice: During the data transmission one bit can be wrong (substituted) at most.

How it Works:
Input message: [144, 16, 210, 214]
Remove erroneous characters (binary): [10010000, 00010000, 11010010, 11010110]
Binary result (remove parity bit): [10010000, 11010010]
Decimal: [72, 105]
Message string (ASCII): "Hi"

Input: A list of int numbers

Output: Message as a string

Example:

checkio([135, 134, 124, 233, 209, 81,
         42,  202, 198, 194, 229, 215,
         230, 146, 28, 210, 145, 137,
         222, 158, 49, 81, 214, 157]) == "Checkio"
checkio([144, 100, 200, 202, 216, 152,
         164, 88,  216, 222, 65,  218,
         175, 217, 248, 222, 171, 228,
         216, 205, 254, 201, 193, 220]) == "Hello World"
    
How it is used: Parity bits are used as the simplest form of error detecting code. They allow you to detect odd numbers of bit substitutions in data.

Precondition: 1 ≤ len(message) < 100
all(m for m in message if i.isprintable())
0 ≤ number ≤ 255

在Robo-City举行的最后一次I3E工业会议上，采用了新版本的通信协议R2HI 2.0（Robot-to-Human Interface）。 R2HI接口的新版本通过添加错误检测功能来扩展现有的版本。这个功能使我们能够将数据发送到距离人类住区较远的较远距离的机器人，并具有更高的可靠性。在数据传输期间，由于外部事件（辐射影响，不同的噪声等），一些位可以被替换。在R2HI 2.0中提出了简单的奇偶校验位检测技术。

R2HI 2.0接口规格：
1.数据包（消息）被表示为一个int数字列表（0≤number≤255）：
[d1，d2，d3，...，dn]，其中d1是消息中的第一个字母
2.每个十进制数字是二进制+奇偶校验位中相应字符的ASCII码

    
您必须实现一个“R2HI 2.0翻译器/分析器”，将接收到的数据包（int列表）转换为字符串消息。在翻译之前，必须从包裹（清单）中删除错误的号码。错误的意思是十进制值包含一个二进制形式的错误（奇数）数字“1”：

'P'→80→1010000 + 0→10100000→... 10110000 ...→10110000（错误，第4位被反转）
注意：在数据传输过程中，一位最多可能是错误的（替代）。

怎么运行的：
输入消息：[144，16，210，214]
删除错误的字符（二进制）：[10010000，00010000，11010010，11010110]
二进制结果（去除奇偶位）：[10010000，11010010]
十进制：[72，105]
消息字符串（ASCII）：“嗨”

输入：一个int数字列表
输出：消息作为字符串

如何使用：奇偶校验位被用作错误检测代码的最简单形式。它们允许您检测数据中的奇数位替换。
'''