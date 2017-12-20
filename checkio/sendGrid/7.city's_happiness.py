"""
Citizens of GridLand are sending emails to each other all the time. They send everything - what they just ate, a funny picture, questions or thoughts that are bothering them right now. All the citizens are happy because they have such a wonderful network that keeps them connected.

The main goal of the Mayor is to control the city's happiness. The city's happiness is a sum of all citizens happiness. And the happiness of each citizens is equal to the number of citizens (always including oneself) one can send emails to.

Because the city is growing, citizens decide the Mayor needs an assistant to focus on node protection.

Your mission is to figure out what will be the first nodes to investigate and protect for the new assistant. Remember, you should choose the most important node in the network. If several nodes have maximal importance, find all of them


Input: Two arguments. Network structure (as list of connections between nodes), users on each node (as dict where keys are node-name and values are amount of users).

Output: List of the most crusial nodes.

GridLand的市民们一直在互相发邮件。他们把所有的东西——他们刚刚吃的东西、有趣的图片、问题或想法——都发送给他们。所有的公民都很高兴，因为他们有这样一个让他们保持联系的绝妙网络。
市长的主要目标是控制城市的幸福。城市的幸福是所有公民幸福的总和。每个公民的幸福度等于公民的数量(包括自己)可以发送电子邮件到。
因为城市在增长，市民决定市长需要一个助手来关注节点保护。
你的任务是找出第一个节点来调查和保护新的助手。请记住，您应该选择网络中最重要的节点。如果几个节点具有最大的重要性，那么可以找到它们
输入:两个参数。网络结构(如节点之间的连接列表)，每个节点上的用户(作为命令，键节点名和值是用户数量)。
输出:最crusial节点的列表。
Example:

most_crucial([
    ['A', 'B'],
    ['B', 'C']
],{
    'A': 10,
    'B': 10,
    'C': 10
}) == ['B']

most_crucial([
    ['A', 'B']
],{
    'A': 20,
    'B': 10
}) == ['A']

most_crucial([
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'D'],
    ['A', 'E']
],{
    'A': 0,
    'B': 10,
    'C': 10,
    'D': 10,
    'E': 10
}) == ['A']

most_crucial([
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'D']
],{
    'A': 10,
    'B': 20,
    'C': 10,
    'D': 20
}) == ['B']
"""
def most_crucial(net, users):
    return ['B']

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')

