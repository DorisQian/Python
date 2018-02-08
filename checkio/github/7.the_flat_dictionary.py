'''
The mission is in Reviewing Mode. You can't see the solutions Leader Board, but you can see other user solutions through the Random Review after you solve the mission.

Nikola likes to categorize everything in sight. One time Stephan gave him a label maker for his birthday, and the robots were peeling labels off of every surface in the ship for weeks. He has since categorized all the reagents in his laboratory, books in the library and notes on the desk. But then he learned about python dictionaries, and categorized all the possible configurations for Sophia’s drones. Now the files are organized in a deep nested structure, but Sophia doesn’t like this. Let's help Sophia to flatten these dictionaries.

Python dictionaries are a convenient data type to store and process configurations. They allow you to store data by keys to create nested structures. You are given a dictionary where the keys are strings and the values are strings or dictionaries. The goal is flatten the dictionary, but save the structures in the keys. The result should be the a dictionary without the nested dictionaries. The keys should contain paths that contain the parent keys from the original dictionary. The keys in the path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty string (""). Let's look at an example:

{
    "name": {
        "first": "One",
        "last": "Drone"
    },
    "job": "scout",
    "recent": {},
    "additional": {
        "place": {
            "zone": "1",
            "cell": "2"}
    }
}

The result will be:

{"name/first": "One",           #one parent
 "name/last": "Drone",
 "job": "scout",                #root key
 "recent": "",                  #empty dict
 "additional/place/zone": "1",  #third level
 "additional/place/cell": "2"}

Input: An original dictionary as a dict.

Output: The flattened dictionary as a dict.

Example:

flatten({"key": "value"}) == {"key": "value"}
flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}
flatten({"empty": {}}) == {"empty": ""}
    
How it is used: This concept can be useful if you need to parse config files and simplify structures for grandfathered systems and file structures. You can easily modify this idea for your own specifications. Besides that, it's a useful skill to be able to read code and search for bugs.

Precondition:
Keys in a dictionary are non-empty strings.
Values in a dictionary are strings or dicts.
root_dictionary != {}

任务处于审阅模式。你看不到解决方案领袖委员会，但你可以在解决任务后通过随机审查看到其他用户解决方案。

尼古拉喜欢把所有的东西都归类在眼前。有一次斯蒂芬为他的生日给了他一个标签制造商，机器人在船上的每一个表面都剥下了几个星期的标签。此后，他将实验室中的所有试剂，图书馆的书籍和书桌上的笔记分类。但后来他学习了python字典，并对索菲亚无人机的所有可能配置进行了分类。现在这些文件被组织在一个深层嵌套的结构中，但是索菲亚不喜欢这个。让我们来帮助索菲亚把这些字典弄平。

Python字典是一种方便的数据类型来存储和处理配置。它们允许您通过键存储数据来创建嵌套结构。给你一个字典，其中的键是字符串，值是字符串或字典。目标是扁平字典，但保存在键中的结构。结果应该是没有嵌套字典的字典。密钥应该包含包含原始字典中的父密钥的路径。路径中的键由“/”分隔。如果一个值是一个空的字典，那么它应该被一个空字符串（“”）替换。我们来看一个例子：

输入：作为字典的原始字典。
输出：扁平字典作为字典。

如何使用：如果您需要解析配置文件并简化祖先系统和文件结构的结构，则此概念可能非常有用。您可以根据自己的规格轻松修改这个想法。除此之外，能够阅读代码并搜索错误是一项非常有用的技能。

前提：
字典中的键是非空字符串。
字典中的值是字符串或字符串。
root_dictionary！= {}
'''


def flatten(dictionary):
    # your code here
    return {}


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
                        "first": "One",
                        "last": "Drone"},
                    "job": "scout",
                    "recent": {},
                    "additional": {
                        "place": {
                            "zone": "1",
                            "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')
