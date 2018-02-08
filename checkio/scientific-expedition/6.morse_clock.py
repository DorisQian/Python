"""
"di-dah di-di-di-dit di-dah-dah di-dah-dah-dah dah-di-dit dah-di-di-dah", sound of 
Morszelizer clanked out loud.

"What're you doing?" Nikola asked curiously.

"I'm sending our time logs for the last expedition to headquarters, but it's
 not an easy task..." Stephen grumbled, "Can you imagine that with all the 
 computer power at our disposal, I STILL have to convert this message to 
 Morse-code with only an on/off button... Hrmph... what a pain." He grumbled 
 at the inconvenience.

"Let me look at it." Nikola offered his help, "It looks like a pretty easy 
solution, we could automate the process."

"Oh.. you hero of my day." Stephen started excitedly. "So, how do we start it?"

"With Python!" Nikola exclaimed.

Help Stephen to create a module for converting a normal time string to a morse 
time string. As you can see in the illustration, a gray circle means on, while 
a white circle means off. Every digit in the time string contains a different 
number of slots. The first digit for the hours has a length of 2 while the second 
digit for the hour has a length of 4. The first digits for the minutes and seconds 
have a length of 3 while the second digits for the minutes and seconds have a length 
of 4. Every digit in the time is converted to binary representation. You will convert 
every on (or 1) signal to dash ("-") and every off (or 0) signal to dot (".").

example source: Wikipedia

An time string could be in the follow formats: "hh:mm:ss", "h:m:s" or "hh:m:ss". The 
"missing" digits are zeroes. For example, "1:2:3" is the same as "01:02:03".

The result will be a morse time string with specific format:
"h h : m m : s s"
where each digits represented as sequence of "." and "-"

Input: A normal time string as a string (unicode).

Output: The morse time string as a string.

Example:

checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"

How it is used: Did you see the binary clocks task earlier? This is can be a 
fun gift for any geek. We tried to combine the old good Morse code with a binary 
clock in this task, and now you can create the new more complex binary clock, which 
doesn't show time -- but makes morse style bips and beeps. ;-)

Precondition: 
time_string contains correct time.

“迪-达-迪-达-达-达-达-达-达-达-达-德-达-达-达-达-达-达-达-达-达-德-达-达-德-达-达-德-
达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达-达
“你在做什么?”尼古拉好奇地问道。
“我把我们的时间记录发给了总部的最后一次探险，但这不是一件容易的事……”斯蒂芬抱怨道，
“你能想象，在我们所有的计算机能力下，我仍然需要把这个信息转换成morse - code，
只需要一个on / off按钮……”Hrmph……什么是痛苦。他对不便表示抱怨。
“让我看看。”Nikola提供了他的帮助，“这看起来是一个非常简单的解决方案，我们可以自动化这个过程。”
“哦. .你是我今天的英雄。“斯蒂芬开始兴奋地。“那么，我们该如何开始呢?”
“与Python !”尼古拉喊道。
帮助Stephen创建一个模块，用于将一个正常的时间字符串转换为莫尔斯时间字符串。
正如您在插图中看到的，一个灰色的圆圈表示，而白色的圆圈表示关闭。小时的第一个数字的长度是2，
而这个小时的第二个数字的长度是4。分钟和秒的第一个数字的长度为3，而分钟和秒的第
二个数字的长度为4。时间中的每一个数字都转换成二进制表示形式。你将把每一个(或1)
个信号转换为dash(“-”)，并将每一个(或0)信号转换为点(“。”)。

例子来源:维基百科
一个时间字符串可以是以下格式:“hh:mm:ss”，“h:m:s”或“hh:m:ss”。“缺失”的数字是零。
例如，“1:2:3”和“01:02:03”是一样的。
其结果将是一个具有特定格式的摩尔斯时间字符串:
h:m m:s s
其中每个数字表示为“序列”。”和“-”

输入:一个普通的时间字符串作为字符串(unicode)。
输出:莫尔斯时间字符串作为字符串。

如何使用:您是否看到了前面的二进制时钟任务?这对任何一个极客来说都是一件有趣的礼物。
我们尝试将旧的好莫尔斯码与一个二进制时钟结合在这个任务中，现在你可以创建新的更复
杂的二进制时钟，它不显示时间，但会制造莫尔斯风格的哔哔声和哔哔声。:-)


先决条件:

time_string包含正确的时间。
"""

def checkio(time_string):

    time_list = time_string.split(':')
    
    for i in range(len(time_list)):
    	if len(time_list[i]) != 2:
    		time_list[i] = '0' + time_list[i]
    print(time_list)
    result = ''
    count = 1
    for time in time_list:
    	bin_time = ''

    	bint1 = bin(int(time[0])).replace('b', '0')[-4:]
    	if count == 1:
    		bint1 = bint1[:len(bint1) -2].replace('0', '') + bint1[-2:]
    	else:
    		bint1 = bint1[:len(bint1) -3].replace('0', '') + bint1[-3:]
    	print(bint1)
    	bint2 = bin(int(time[1])).replace('b', '0')[-4:]

    	if len(bint2) != 4:
    		bint2 = '0' * (4 - len(bint2)) + bint2

    	bin_time = bint1 + ' ' + bint2
    	#print(bin_time)
    	result += bin_time.replace('0', '.').replace('1', '-') + ' : '
    	print(result.strip(' :'))

    	count += 1
    return(result.strip(' :'))



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"