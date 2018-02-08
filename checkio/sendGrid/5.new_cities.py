"""
Sometimes damaged nodes are unrecoverable. In that case, people that were connected to the crushed node must 
migrate to another district while administration attempts to fix the node.

But if a crushed node disconnects multiple districts from one another, then the network splits into two 
sub-networks and every sub-network should have their own Mayor. And Mayors must use pigeons for mailing between 
each other. In that case, when the network is split you don’t need hundreds of pigeons.

Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed. 
In other words, you need to figure out how many sub-networks will be formed after some nodes are crush and not 
recovered.


Input: Two arguments. Network structure (as list of connections between nodes) and list of crashed nodes

Output: Int. The amount of sub-networks after crushing nodes.

Example:

subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2
subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3
subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1

有时损坏的节点是不可恢复的。在这种情况下，连接到被压的节点的人必须迁移到另一个区域，而管理试图修复该节点。
但是如果一个被压碎的节点将多个地区分开，那么网络就会分裂成两个子网络，每个子网络都应该有自己的市长。市长们必须用鸽子来互相邮寄信
。在这种情况下，当网络分裂时，你不需要上百只鸽子。
你的任务是找出你需要多少市长来控制整个城市当一些节点被摧毁。换句话说，您需要计算出在某些节点被压碎而未恢复之后，会形成多少个子网络。
输入:两个参数。网络结构(如节点之间的连接列表)和崩溃节点列表
输出:Int .破碎节点后的子网络数量。
"""

def subnetworks(net, crushes):
    relation_dic = {}
    for node in net:
        node_set = relation_dic.get(node[0],list())
        node_set.append(node[1])
        relation_dic[node[0]] = node_set

        node_set = relation_dic.get(node[1], list())
        node_set.append(node[0]) 
        relation_dic[node[1]] = node_set

    crushes_node = crushes
    relation_node = [ ]
    num = 0
    # 取出crush节点在dict中的直接关联节点放到relation_node中
    for cru in crushes_node:
        for cru_relation in relation_dic[cru]:
            if cru_relation not in crushes_node:
                relation_node.append(cru_relation)
 #   print(relation_node)

    #如果与crush相关的直接节点只有一个，则直接返回1
    if len(relation_node) == 1:
        return 1
    else:
        for node in relation_node:
            valuelist = relation_dic[node]
            for value in valuelist:
                if value in relation_node and value not in crushes_node:
                    num += 1
        return len(relation_node) - num/2
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"    
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    assert subnetworks([
            ["A", "B"],
            ["A", "C"],
            ["A", "D"],
            ["D", "F"],
            ["B", "C"]
        ],["A"]) == 2, "Fourth"
    print('Done! Check button is waiting for you!')
    