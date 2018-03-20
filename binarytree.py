# !/usr/bin/env python3
# -*- coding = utf-8 -*-


class node(object):
    def __init__(self, node, left=None, right=None):
        self.node = node
        self.left = left
        self.right = right


def font_traversal(tree):
    if tree:
        if type(tree) == str:
            print(tree)
        else:
            print(tree.node)
            font_traversal(tree.left)
            font_traversal(tree.right)
    else:
        return


def mid_traversal(tree):
    if tree:
        mid_traversal(tree.left)
        print(tree.node)
        mid_traversal(tree.right)
    else:
        return


def later_tarversal(tree):
    if node:
        later_tarversal(left)
        later_tarversal(right)
        print(node)
    else:
        return

if __name__ == '__main__':
    tree = node('A', node('B', 'C', 'D'), node('E', 'F', node('G', ' H')))
    print('the font')
    font_traversal(tree)
    mid_traversal(tree)
    later_tarversal(tree)


