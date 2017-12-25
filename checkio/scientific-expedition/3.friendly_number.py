"""
Long numbers can be made to look nicer, so let’s write some code to do just that.

You should write a function for converting a number to string using several rules. First of all, you will need to cut the number with a given base (base argument; default 1000). The value is a float number with decimal after the point (decimals argument; default 0). For the value, use the rounding towards zero rule (5.6⇒5, -5.6⇒-5) if the decimal = 0, otherwise use the standard rounding procedure. If the number of decimals is greater than the current number of digits after dot, trail value with zeroes. The number should be a value with letters designating the power. You will be given a list of power designations (powers argument; default ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']). If you are given suffix (suffix argument; default ‘’) , then you must append it. If you don’t have enough powers - stay at the maximum. And zero is always zero without powers, but with suffix.

Let's look at examples. It will be simpler.

n=102
result: "102", the base is default 1000 and 102 is lower this base.
n=10240
result: "10k", the base is default 1000 and rounding down.
n=12341234, decimals=1
result: "12.3M", one digit after the dot.
n=12000000, decimals=3
result: "12.000M", trailing zeros.
n=12461, decimals=1
result: "12.5k", standard rounding.
n=1024000000, base=1024, suffix='iB'
result: '976MiB', the different base and the suffix.
n=-150, base=100, powers=['', 'd', 'D']
result: '-1d', the negative number and rounding towards zero.
n=-155, base=100, decimals=1, powers=['', 'd', 'D']
result: '-1.6d', the negative number and standard rounding.
n=255000000000, powers=['', 'k', 'M']
result: '255000M', there is not enough powers.
Input: A number as an integer. The keyword argument "base" as an integer, default 1000. The keyword argument "decimals" as an integer, default 0. The keyword argument "powers" as a list of string, default ['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'].

Output: The converted number as a string.

Example:

friendly_number(102) == '102'
friendly_number(10240) == '10k'
friendly_number(12341234, decimals=1) == '12.3M'
friendly_number(12000000, decimals=3) == '12.000M'
friendly_number(12461, decimals=1) == '12.5k'
friendly_number(1024000000, base=1024, suffix='iB') == '976MiB'

How it is used: In the physics and IT we have a lot of various numbers. Sometimes we need to make them more simpler and easier to read. When you talk about gigabytes sometimes you don’t need to know the exact number bytes or kilobytes.

Precondition: 1 < base ≤ 1032
-1032 < number ≤ 1032
0 ≤ decimals ≤ 15
0 < len(powers) ≤ 32

可以让长数字看起来更好，所以让我们编写一些代码来做到这一点。
您应该编写一个函数，使用几个规则将一个数字转换为字符串。首先，你需要用给定的基数来减少数字(基本参数;默认的1000)。值是小数点后的浮点数(小数参数;默认0)值,用舍入为零法则(5.6⇒5,-5.6⇒5)如果小数点= 0,否则使用标准的舍入的过程。如果小数位数大于当前数字后面的数字，则带0的跟踪值。数字应该是一个值，字母表示权力。你将得到一份权力分配表(权力的论据;违约(”、“k”、“M”,‘G’,‘T’,‘P’,‘E’,' Z ',' Y '])。如果给定后缀(后缀参数;(默认)，然后你必须附加它。如果你没有足够的能力，那就呆在最高的地方。0总是零，没有幂，但有后缀。
让我们来看看例子。这将是更简单。

n = 102
结果:“102”，基数是默认的1000，而102则降低了这个基数。
n = 10240
结果:“10k”，基数为默认值1000，取整。
n = 12341234,小数= 1
结果:“12.3米”，小数点后一位数。
n = 12000000,小数= 3
结果:“12.000”,落后于0。
n = 12461,小数= 1
结果:“12.5 k”,标准的舍入。
= = 1024 n = 1024000000,基地,后缀“iB”
结果:976MiB，不同的碱基和后缀。
n=- 150，底数= 100，幂次=[' d '，' d ']
结果:“- 1d”，负数，四舍五入为零。
n = -155 = 100,小数= 1,权力=[",' d ',' d ']
结果:“- 1.6 d”，负数和标准四舍五入。
n = 255000000000,力量=[”、“k”、“M”)
结果:255000M，没有足够的能力。

输入:一个数字作为整数。关键字参数“base”作为一个整数，默认为1000。关键字参数“decimals”作为整数，默认为0。关键字参数“权力”作为一个字符串列表,默认["、“k”、‘米’,‘G’,‘T’,‘P’,‘E’,' Z ',' Y ']。
输出:将转换后的数字作为字符串。

它是如何使用的:在物理学中，我们有许多不同的数字。有时我们需要让他们更简单，更容易阅读。当你谈论字节数时，有时你不需要知道确切的字节数或千字节。
"""
def friendly_number(number, base=1000, decimals=0, suffix='',
                    powers=['', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y']):
    """
    Format a number as friendly text, using common suffixes.
    """
    return str(number)

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert friendly_number(102) == '102', '102'
    assert friendly_number(10240) == '10k', '10k'
    assert friendly_number(12341234, decimals=1) == '12.3M', '12.3M'
    assert friendly_number(12461, decimals=1) == '12.5k', '12.5k'
    assert friendly_number(1024000000, base=1024, suffix='iB') == '976MiB', '976MiB'