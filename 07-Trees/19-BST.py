# BINARY SEARCH TREES
from unittest import result


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True     # returning cause we dont want to continue
        temp = self.root
        while (True):
            if new_node.value == temp.value:        #  Case for identical values
                return False
            if new_node.value < temp.value:         # Case for the insertion on the left side of the tree.
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:                                   # Case for the insertion on the right of the tree.
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def deleteNode(self, current_node, value):  # also called remove
        if current_node is None:
            return None
        elif value < current_node.value:
            current_node.left = self.deleteNode(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.deleteNode(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                current_node = None
            elif current_node.left == None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                temp = self.min_value_node(current_node.right)
                current_node.value = temp.value
                current_node.right = self.deleteNode(current_node.right, temp.value)
        return current_node
            

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
            
    def min_value_node(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


    # BREADTH FIRST SEARCH - ALGORITHMS : TREE TRAVERSAL
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue):
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results

    # DEPTH FIRST SEARCH (PREORDER)
    def DFS_preorder(self):
        results = []
        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    # DEPTH FIRST SEARCH (POSTORDER)
    def DFS_postorder(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
            results.append(current_node.value)
        traverse(self.root)
        return results

    # DEPTH FIRST SEARCH (INORDER)
    def DFS_inorder(self):
        results = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return results



##########  MAIN PROGRAM ##########
bts = BinarySearchTree()
bts.insert(47)
bts.insert(21)
bts.insert(76)
bts.insert(18)
bts.insert(27)
bts.insert(52)
bts.insert(82)

#print(bts.BFS())
#print(bts.DFS_preorder())
#print(bts.DFS_postorder())
print(bts.DFS_inorder())

#print(bts.min_value_node(bts.root))             # we expect the 18 node
#print(bts.min_value_node(bts.root.right))       # we expect the 52 node

#print(bts.contains(27))
#print(bts.contains(17))

#print(bts.root.value)
#print(bts.root.left.value)
#print(bts.root.right.value)

