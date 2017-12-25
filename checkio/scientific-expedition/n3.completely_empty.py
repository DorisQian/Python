"""
You need to figure if a wellfounded and wellsized iterable is completely empty.

An iterable x0 is wellfounded if there is no infinite sequence

x1,x2,x3... such that  ... in x3 in x2 in x1 in x0 (where in is meant iteratively,  x(n+1) will be encountered while iterating through xn).
A wellfounded iterable is wellsized if it has only finitely many iterable elements, and all of them are wellsized.

A wellfounded iterable is completely empty when all its elements are completely empty.

Some consequences of the above definitions:

any empty iterable is completely empty
a non-iterable is never completely empty
the only wellfounded string is '', and it is completely empty
bytes, and (possibly nested) tuples/frozensets of them are always wellfounded and wellsized
{'': 'Nonempty'} is a wellfounded and completely empty iterable
after c=[];c.append(c), c is a non-wellfounded iterable
itertools.repeat(()) is wellfounded but not wellsized
itertools.repeat(5) is wellfounded and wellsized
Input: A wellfounded and wellsized iterable.

Output: A bool.

Example:

completely_empty([]) == True
completely_empty([1]) == False
completely_empty([[]]) == True
completely_empty([[],[]]) == True
completely_empty([[[]]]) == True
completely_empty(['']) == True
completely_empty([[],[{'':'No WAY'}]]) == True


您需要了解一个良好的、良好的迭代是否完全是空的。
如果没有无限序列，则可以使用iterable x0
x1,x2,x3……这样的……在x0中的x1 x2中(在这里是迭代的，x(n + 1)在迭代xn时将会遇到)。
如果一个well创建的iterable只有有限的许多可迭代元素，那么它的大小是非常大的。
当所有元素都是完全空的时候，一个创建好的iterable是完全空的。
以上定义的一些后果:
任何空迭代都是完全空的
不可迭代的永远不会是完全空的
唯一的well创建的字符串是“，它是完全空的”
字节，以及(可能嵌套的)tuple / frozensets总是很好且很好
{“非空”}是一个创建良好且完全空的迭代
c=[];c. append(c)，c是一个非well创建的iterable
重复(())是有根据的，但不是很好
重复(5)是很好的，也很好
输入:一个创建良好且大小可重复的迭代。
输出:一个布尔值。
"""