"""
For the mission "How to find friends" , it’s nice to have access to a specially made data structure. In this mission we will realize a data structure which we will use to store and work with a friend network.

The class "Friends" should contains names and the connections between them. Names are represented as strings and are case sensitive. Connections are undirected, so if "sophia" is connected with "nikola", then it's also correct in reverse.

class Friends(connections)

Returns a new Friends instance. "connections" is an iterable of sets with two elements in each. Each connection contains two names as strings. Connections can be repeated in the initial data, but inside it's stored once. Each connection has only two states - existing or not.

>>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
>>> Friends([{"1", "2"}, {"3", "1"}])

add(connection)

Add a connection in the instance. "connection" is a set of two names (strings). Returns True if this connection is new. Returns False if this connection exists already.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.add({"1", "3"})
False
>>> f.add({"4", "5"})
True

remove(connection)

Remove a connection from the instance. "connection" is a set of two names (strings). Returns True if this connection exists. Returns False if this connection is not in the instance.

>>> f = Friends([{"1", "2"}, {"3", "1"}])
>>> f.remove({"1", "3"})
True
>>> f.remove({"4", "5"})
False

names()

Returns a set of names. The set contains only names which are connected with somebody.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"}))
>>> f.names()
{"a", "b", "c", "d"}
>>> f.remove({"d", "c"})
True
>>> f.names()
{"a", "b", "c"}

connected(name)

Returns a set of names which is connected with the given "name". If "name" does not exist in the instance, then return an empty set.

>>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}))
>>> f.connected("a")
{"b", "c"}
>>> f.connected("d")
set()
>>> f.remove({"c", "a"})
True
>>> f.connected("c")
{"b"}
>>> f.remove({"c", "b"})
True
>>> f.connected("c")
set()

In this mission all data will be correct and you don't need to implement value checking.

Input: Statements and expression with the Friends class.

Output: The behaviour as described.

How it is used: Here you will implement a class with mutable states. This is not a simple structure with a couple of functions, but object representation with more complex structure.

Precondition: All data is correct.

对于“如何寻找朋友”的任务，可以访问一个专门的数据结构。在这次任务中，我们将实现一个数据结构，我们将用来存储和使用一个朋友网络。
类“好友”应该包含名称和它们之间的连接。名称以字符串形式表示，区分大小写。连接是无定向的，所以如果“sophia”与“nikola”连接，那么它的反向也是正确的。
返回一个新朋友实例。“连接”是一组具有两个元素的集合。每个连接包含两个名称作为字符串。连接可以在初始数据中重复，但在内部存储一次。每个连接只有两个状态——存在与否。
在实例中添加连接。“connection”是一组两个名称(字符串)。如果这个连接是新的，返回True。如果此连接已经存在，则返回False。
从实例中删除连接。“connection”是一组两个名称(字符串)。如果此连接存在，则返回True。如果该连接不在实例中，则返回False。
返回一组名称。该集合只包含与某人连接的名称。
返回与给定的“name”连接的一组名称。如果实例中不存在“name”，则返回空集。
在这个任务中，所有数据都是正确的，你不需要执行值检查。

输入:与朋友类的语句和表达式。
输出:描述的行为。

如何使用:在这里，您将实现一个具有可变状态的类。这不是一个简单的结构，有几个函数，但是对象表示结构更复杂。

先决条件:所有数据都是正确的。
"""

class Friends:
    def __init__(self, connections):
        raise NotImplementedError

    def add(self, connection):
        raise NotImplementedError

    def remove(self, connection):
        raise NotImplementedError

    def names(self):
        raise NotImplementedError

    def connected(self, name):
        raise NotImplementedError



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"
