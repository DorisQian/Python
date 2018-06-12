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
            print(tree, end='')
        else:
            print(tree.node, end='')
            font_traversal(tree.left)
            font_traversal(tree.right)
    else:
        return


def mid_traversal(tree):
    if tree:
        if type(tree) == str:
            print(tree, end='')
        else:
            mid_traversal(tree.left)
            print(tree.node, end='')
            mid_traversal(tree.right)
    else:
        return


def later_tarversal(tree):
    if tree:
        if type(tree) == str:
            print(tree, end='')
        else:
            later_tarversal(tree.left)
            later_tarversal(tree.right)
            print(tree.node, end='')
    else:
        return

if __name__ == '__main__':
    tree = node('A', node('B', 'C', 'D'), node('E', 'F', node('G', 'H')))
    print('the font')
    font_traversal(tree)
    print('\nthe mid')
    mid_traversal(tree)
    print('\nthe later')
    later_tarversal(tree)


