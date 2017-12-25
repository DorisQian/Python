"""
Over six years ago, in December 1989, I was looking for a "hobby" programming project that would keep me occupied during the week around Christmas. My office (a government-run research lab in Amsterdam) would be closed, but I had a home computer, and not much else on my hands. I decided to write an interpreter for the new scripting language I had been thinking about lately: a descendant of ABC that would appeal to Unix/C hackers. I chose Python as a working title for the project, being in a slightly irreverent mood (and a big fan of Monty Python's Flying Circus).

Today, I can safely say that Python has changed my life. I have moved to a different continent. I spend my working days developing large systems in Python, when I'm not hacking on Python or answering Python-related email. There are Python T-shirts, workshops, mailing lists, a newsgroup, and now a book. Frankly, my only unfulfilled wish is to have my picture on the front page of the New York Times.

-- Guido van Rossum, Foreword for "Programming Python", Reston, VA, May 1996

This mission is simple to solve. You are given a function called "i_love_python" which will only return the phrase - "I love Python!"

Let's write an essay in python code which will explain why you love python (if you don't love it, when we will make an additional mission special for the haters). Publishing the default solution will only earn you 0 points as the goal is to earn points through votes for your code essay.

Input: Nothing.

Output: The string "I love Python!".

Example:

i_love_python() == "I love Python!"
    
How it is used: This mission revolves around code literacy.

六年前，在1989年12月，我正在寻找一个“业余爱好”编程项目，这个项目能让我在圣诞节前后的一周内保持忙碌。我的办公室(位于阿姆斯特丹的一个政府办的研究实验室)将被关闭，但我有一台家用电脑，而且我手头没有太多其他的东西。我决定为我最近一直在思考的新脚本语言编写一个解释器:一个会吸引Unix / C黑客的ABC的后代。我选择Python作为这个项目的一个工作标题，它的心情有点不那么虔诚(同时也是Monty Python的飞行马戏团的超级粉丝)。
今天，我可以有把握地说，Python已经改变了我的生活。我搬到了另一个大陆。我的工作天是在Python中开发大型系统，而不是在Python或与Python相关的电子邮件上进行黑客攻击。有Python t恤、研讨会、邮件列表、新闻组，现在有一本书。坦率地说，我唯一未实现的愿望就是在《纽约时报》的头版刊登我的照片。
——Guido van Rossum，“编程Python”的前言，Reston,VA,1996年5月
这个任务很容易解决。您将得到一个名为“i_love_python”的函数，该函数只返回一个短语——“我喜欢Python !”
让我们写一篇关于python代码的文章，这篇文章将解释为什么你喜欢python(如果你不喜欢它的话，当我们为那些讨厌的人做额外的任务时)。发布默认的解决方案只会让你获得0分，因为你的目标是通过你的代码文章获得分数。

输入:没有。
输出:字符串“我喜欢Python !”

如何使用:这个任务围绕着代码素养。
"""
def i_love_python():
    """
        Let's explain why do we love Python.
    """
    return "I love Python"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
