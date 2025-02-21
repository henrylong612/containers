'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the
functions in the BinaryTree and BST files,
but there are fewer of them.
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    AVLTree is currently not a subclass of BST.
    You should make the necessary changes in the class
    declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        Returns True if the avl tree satisfies that all
        nodes have a balance factor in [-1,0,1].
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        elif not node:
            return True
        else:
            left_satisfied = AVLTree._is_avl_satisfied(node.left)
            right_satisfied = AVLTree._is_avl_satisfied(node.right)
            return left_satisfied and right_satisfied

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their
        AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old_root = node
        if old_root.right:
            new_root = Node(old_root.right.value)
            new_root.left = Node(old_root.value)
            new_root.right = old_root.right.right
            new_root.left.left = old_root.left
            new_root.left.right = old_root.right.left
            return new_root
        return old_root

    @staticmethod
    def _right_rotate(node):

        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL
        tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
        old_root = node
        if old_root.left:
            new_root = Node(old_root.left.value)
            new_root.right = Node(old_root.value)
            new_root.left = old_root.left.left
            new_root.right.right = old_root.right
            new_root.right.left = old_root.left.right
            return new_root
        return old_root

    def insert(self, value):
        '''
        Implement this function.
        The lecture videos provide a high-level overview
        of how to insert into an AVL tree,
        and the textbook provides full python code.
        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code
        for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
        if self.root:
            self.root = AVLTree._insert(self.root, value)
        else:
            self.root = Node(value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        if not node:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)
        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
        return node
        '''
        if value <= node.value:
            if node.left:
                node.left.parent = node
                AVLTree._insert(node.left, value)
            else:
                node.left = Node(value)
                node.left.parent = node
        if value >= node.value:
            if node.right:
                node.right.parent = node
                AVLTree._insert(node.right, value)
            else:
                node.right = Node(value)
                node.right.parent = node
        try:
            node.parent = AVLTree._rebalance(node.parent)
        except AttributeError:
            pass
        return node
        while path:
            path.pop()
            if path:
                command = 'temp = node.' + '.'.join(path)
                exec(command)
                if AVLTree._balance_factor(temp) not in [-1, 0, 1]:
                    temp = AVLTree._rebalance(temp)
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            node = AVLTree._rebalance(node)
        return node
        '''

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
        if AVLTree._balance_factor(node) < 0:
            if AVLTree._balance_factor(node.right) > 0:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)
            else:
                return AVLTree._left_rotate(node)
        elif AVLTree._balance_factor(node) > 0:
            if AVLTree._balance_factor(node.right) < 0:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
            else:
                return AVLTree._right_rotate(node)
        else:
            return node
