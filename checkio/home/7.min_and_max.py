"""
We have prepared a set of Editor's Choice Solutions. You will see them first after you solve the mission. In order to see all other solutions you should change the filter.
In this mission you should write you own py3 implementation (but you can use py2 for this) of the built-in functions min and max. Some builtin functions are closed here: import, eval, exec, globals. Don't forget you should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.

The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.

Example:

max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
    
How it is used: This task will help you understand how some of the built-in functions work on a more precise level.

Precondition: All test cases are correct and functions don't have to raise exceptions.

我们已经准备了一套编辑器的选择方案。在你解决了任务之后，你将会看到他们。为了看到所有其他的解决方案，你应该改变过滤器。
在这个任务中，您应该编写您自己的py3实现(但是您可以使用py2来实现)的内置函数min和max。这里关闭了一些构建函数:导入、eval、exec、全局变量。不要忘记在代码中应该实现两个函数。
max(iterable，*[，key])或min(iterable，*[，key])

max(arg1,arg2，* args[，key])或min(arg1,arg2，* args[，key])
返回可迭代的最大(最小)项或两个或多个参数的最大(最小)项。
如果提供了一个位置参数，则它应该是可迭代的。在iterable中最大的(最小的)项返回。如果提供了两个或多个位置参数，则返回最大(最小)的位置参数。
可选的关键字关键参数指定了一个参数的函数，该参数用于从每个列表元素提取比较键(例如，key = str.lower)。
如果多个项是极大值(最小值)，则函数返回第一个遇到的项。

——Python文档(内置函数)
输入:一个可迭代或两个或多个位置参数的位置参数。可选的关键字参数作为一个函数。
输出:“max”函数的最大项，最小值为“min”函数。
如何使用:这个任务将帮助您了解一些内置函数如何在更精确的级别上工作。

先决条件:所有测试用例都是正确的，功能不需要引发异常。
"""
#i think my thought is right ,but still need simplify the code like this
def sor(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key = key, reverse= reverse)[0]

def min(*args, key = None):
    return sor(args, key, False)


def max(*args, key = None):
    return sor(args, key, True)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

