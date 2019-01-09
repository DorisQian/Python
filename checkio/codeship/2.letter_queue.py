'''
In computer science, a queue is a particular kind of data type in which the entities in the collection 
are kept in order and the principal operations on the collection are the addition of entities to the rear 
terminal position (enqueue or push), and removal of entities from the front terminal position (dequeue or pop). 
This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element
 added to the queue will be the first one to be removed. This is equivalent to the requirement that once a 
 new element is added, all elements that were added before have to be removed before the new element can be removed.

We will emulate the queue process with Python. You are given a sequence of commands:
- "PUSH X" -- enqueue X, where X is a letter in uppercase.
- "POP" -- dequeue the front position. if the queue is empty, then do nothing.
The queue can only contain letters.

You should process all commands and assemble letters which remain in the queue in one word from the front 
to the rear of the queue.

Let's look at an example, here’s the sequence of commands:
["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]

Command	Queue	Note
PUSH A	A	Added "A" in the empty queue
POP		Removed "A"
POP		The queue is empty already
PUSH Z	Z	
PUSH D	ZD	
PUSH O	ZDO	
POP	DO	
PUSH T	DOT	The result
Input: A sequence of commands as a list of strings.

Output: The queue remaining as a string.

Example:

letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT"
letter_queue(["POP", "POP"]) == ""
letter_queue(["PUSH H", "PUSH I"]) == "HI"
letter_queue([]) == ""
    
How it is used: Queues provide services in computer science, transportation, and operations research where 
various entities such as data, objects, persons, or events are stored and held to be processed later. In these 
contexts, the queue performs the function of a buffer.

Precondition:
0 ≤ len(commands) ≤ 30;
all(re.match("\APUSH [A-Z]\Z", c) or re.match("\APOP\Z", c) for c in commands)

在计算机科学中，队列是集合中实体的特定种类的数据类型保持秩序，收集的主要行动是增加实体到后方
终端位置（排队或推送），以及从前端终端位置（出队或弹出）中删除实体。
这使队列成为先进先出（FIFO）数据结构。在FIFO数据结构中，第一个元素添加到队列将是第一个被删除。这相当于一次的要求
 添加新元素，在删除新元素之前，必须删除之前添加的所有元素。

我们将用Python模拟队列过程。您会得到一系列命令：
- “PUSH X” - 入队X，其中X是大写字母。
- “POP” - 将前排位置出列。如果队列是空的，那么什么都不做。
队列只能包含字母。

您应该处理所有命令，并从前面一个字中组合保留在队列中的字母到队列的后面。

我们来看一个例子，下面是一系列命令：
[“PUSH A”，“POP”，“POP”，“PUSH Z”，“PUSH D”，“PUSH O”，“POP”，“PUSH T”]

命令队列注意事项
PUSH A A在空队列中添加“A”
POP删除了“A”
POP队列已经空了
PUSH Z Z
PUSH D ZD
PUSH O ZDO
POP DO
PUSH T DOT结果
输入：作为字符串列表的一系列命令。
输出：队列仍然是一个字符串。

它如何使用：队列提供计算机科学，交通和运营研究方面的服务
诸如数据，对象，人员或事件的各种实体被存储并保存以待以后处理。在这些
上下文中，队列执行缓冲区的功能。
'''

def letter_queue(commands):
	result_list = []
	if len(commands):
		for command_list in commands:
			c = command_list.split(' ')
			if c[0] == 'PUSH':
				result_list.append(c[1])
			if c[0] == 'POP':
				if len(result_list):
					result_list.pop(0)
		return ''.join(result_list)
	else:
		return ''
			

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"