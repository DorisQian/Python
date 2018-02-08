"""
Welcome to the GridLand. All the citizens here are connected through the global internal network because the main way for communication here is via email. Every new district of the city starts with building a node – center of the district. All the citizens will be connected to this node in order to send and receive emails. All nodes of GridLand are connected so one node can send emails between connected nodes. In such a way, no matter how big the city is all users can send messages between each other as long as all of the nodes are connected.

The Mayor of GridLand is using this network to quickly send emergency emails to all citizens when necessary. But the system is not perfect. When one of city nodes gets crushed it may leave the citizens of this node district disconnected from these emergency emails. It may also leave districts around the crushed node disconnected if their nodes do not have other ways to connect. To resolve this occurrence, the Mayor uses mail-pigeons – an old method of sending mail that was invented before the global internal network. All of the connected citizens still connected to the network received the emergency emails, but the disconnected citizens receive their from these pigeons.

Your mission is to figure out how many pigeons you need when some of the nodes are crushed.


Input: Four arguments. Network structure (as list of connections between nodes), users on each node (as dict where keys are node-name and values are amount of users), name of node that sends email, list of crashed nodes.

Output: Int. Amount of users that wouldn't receive an email.

Example:

disconnected_users([
    ['A', 'B'],
    ['B', 'C'],
    ['C', 'D']
], {
    'A': 10,
    'B': 20,
    'C': 30,
    'D': 40
},
    'A', ['C']) == 70

disconnected_users([
    ['A', 'B'],
    ['B', 'D'],
    ['A', 'C'],
    ['C', 'D']
], {
    'A': 10,
    'B': 0,
    'C': 0,
    'D': 40
},
    'A', ['B']) == 0

disconnected_users([
    ['A', 'B'],
    ['A', 'C'],
    ['A', 'D'],
    ['A', 'E'],
    ['A', 'F']
], {
    'A': 10,
    'B': 10,
    'C': 10,
    'D': 10,
    'E': 10,
    'F': 10
},
    'C', ['A']) == 50

欢迎来到GridLand。这里所有的公民都通过全球内部网络连接，因为这里沟通的主要方式是通过电子邮件。城市的每一个新区都以建立一个区域中心为起点。所有公民都将被连接到这个节点，以便发送和接收电子邮件。GridLand的所有节点都连接在一起，这样一个节点就可以在连接的节点之间发送邮件。在这种方式下，无论城市有多大，只要所有的节点都连接在一起，用户就可以彼此发送消息。
GridLand的市长正在利用这个网络迅速向所有公民发送紧急邮件。但是这个系统并不完美。当城市的一个节点被压碎时，这个节点区的居民就会离开这些紧急邮件。如果节点没有其他连接方式，它也可能使被压碎的节点周围的区域断开连接。为了解决这一问题，市长使用了邮件信鸽——这是一种老式的发送邮件的方法，它是在全球内部网络之前发明的。所有连接到网络的联网公民都收到了紧急电子邮件，但那些没有联系的公民收到了这些鸽子的信息。
你的任务是计算出当一些节点被压碎时需要多少鸽子。
输入:四个参数。网络结构(如节点之间的连接列表)，每个节点上的用户(如命令中键的节点名和值是用户数量)、发送电子邮件的节点名称、崩溃节点列表。
输出:Int .不接收电子邮件的用户数量。


"""

def disconnected_users(net, users, source, crushes):
    # net中将与每个节点有直接关系的节点存入字典中
    relation_dic = {}
    for net_node in net:
        dst_set = relation_dic.get(net_node[0], set())
        dst_set.add(net_node[1])
        relation_dic[net_node[0]] = dst_set

        dst_set = relation_dic.get(net_node[1], set())
        dst_set.add(net_node[0])
        relation_dic[net_node[1]] = dst_set

    # 所有市民的数量
    all_citizens = sum(users.values())

    # 计算所有与源有关的节点，直到遍历到最后的目的节点中，没有新的可达即全在历史和crush中
    dst_node = source
    history_nodes = []  
    no_effect_citizens = 0
    while dst_node:
        stop_index = 0
        final_flag = False
        for node in dst_node:
            if node in history_nodes or node in crushes:
                stop_index += 1
                if len(dst_node) == stop_index:
                    final_flag = True
                continue
            else:
                history_nodes.append(node)
            no_effect_citizens += users[node]
            dst_node = relation_dic[node]

        if final_flag:
            break
    return all_citizens - no_effect_citizens

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"
    
    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
