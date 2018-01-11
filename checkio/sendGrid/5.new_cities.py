"""
Sometimes damaged nodes are unrecoverable. In that case, people that were connected to the crushed node must migrate to another district while administration attempts to fix the node.

But if a crushed node disconnects multiple districts from one another, then the network splits into two sub-networks and every sub-network should have their own Mayor. And Mayors must use pigeons for mailing between each other. In that case, when the network is split you don’t need hundreds of pigeons.

Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed. In other words, you need to figure out how many sub-networks will be formed after some nodes are crush and not recovered.


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
但是如果一个被压碎的节点将多个地区分开，那么网络就会分裂成两个子网络，每个子网络都应该有自己的市长。市长们必须用鸽子来互相邮寄信件。在这种情况下，当网络分裂时，你不需要上百只鸽子。
你的任务是找出你需要多少市长来控制整个城市当一些节点被摧毁。换句话说，您需要计算出在某些节点被压碎而未恢复之后，会形成多少个子网络。
输入:两个参数。网络结构(如节点之间的连接列表)和崩溃节点列表
输出:Int .破碎节点后的子网络数量。
"""

def subnetworks(net, crushes):
    a = ''
    for nets in net:
        for node in nets:
            if node not in a:
                a += node
    b = 0
    for n1, n2 in net:
        if n1 not in crushes and n2 not in crushes:
            b += 1
    return len(a) - len(crushes) - b

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
    print('Done! Check button is waiting for you!')