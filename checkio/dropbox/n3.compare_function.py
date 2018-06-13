'''
Okay, I guess we have to turn to plan B.
What's plan B?
Why wasn't that plan A?

- The Big Band Theory : "The Lizard-Spock Expansion"

doveryai no proveryai (trust, but verify)

- Russian proverb adopted as signature phrase by Ronald Reagan

Two functions f and g are provided as inputs to checkio. The first function f is the primary 
function and the second function g is the backup. Use your coding skills to return a third function 
h which returns the same output as f unless f raises an exception or returns None. In this case h 
should return the same output as g. If both f and g raise exceptions or return None, then h should return None.

As a second output, h should return a status string indicating whether the function values are 
the same and if either function erred. A function errs if it raises an exception or returns a null value (None).

The status string should be set to: "same" if f and g return the same output and neither errs, 
"different" if f and g return different outputs and neither errs, "f_error" if f errs but not g, 
"g_error" if g errs but not f, or "both_error" if both err.

Input: Two functions: f (primary) and g (backup).

Output: A function h which takes arbitrary inputs and returns a two-tuple.

Example:

        f = lambda x,y: x+y
        g = lambda x,y: (x**2 - y**2)/(x-y)
        checkio(f,g)(1,3) == (4,"same")
        checkio(f,g)(1,1.01) == (2.01,"different") # numerical precision difference
        checkio(f,g)(1,1) == (2,"g_error") # g divides by zero

How it is used: This is an exercise in working with functions as first class objects.

Precondition: hasattr(f,'__call__');
hasattr(g,'__call__')


好的，我想我们必须转向计划B.
什么是B计划？
为什么不是那个计划？

- 大乐队理论：“蜥蜴 - Spock扩张”

doveryai没有proveryai（信任，但验证）

- 俄罗斯谚语被罗纳德里根用作签名短语

提供两个函数f和g作为checkio的输入。第一个函数f是主要的
功能，第二个功能g是备份。使用您的编码技能返回第三个函数
h返回与f相同的输出，除非f引发异常或返回None。在这种情况下，h
应该返回与g相同的输出。如果f和g都引发异常或返回None，那么h应该返回None。

作为第二个输出，h应返回一个状态字符串，指示函数值是否为
相同，如果任一功能出错。如果引发异常或返回空值（无），则函数会发生错误。

状态字符串应该设置为：“相同”如果f和g返回相同的输出并且都不errs，
如果f和g返回不同的输出并且都不是错误，则“不同”，如果错误但不是g，则返回“f_error”
“g_error”如果是er而不是f，或者“both_error”，如果err。

输入：两个功能：f（主）和g（备份）。
输出：一个函数h，它接受任意输入并返回一个二元组。

它是如何使用的：这是一个使用函数作为第一类对象的练习。
'''