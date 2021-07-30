


class BST:
    def __init__(self):
        self.root = None

    class Node:
        def __init__(self, value):
            self.left = None
            self.value = value
            self.right = None


    #~ Outer function
    def add(self, value): #! value is part of __closure__ i.e closure
        
        #~ Inner function
        def add_node(node):
            #$ if we hae reached the leaf node
            if None == node:
                return BST.Node(value)

            if value > node.value:
                node.right = add_node(node.right)
            else:
                node.left = add_node(node.left)
            
            return node

        self.root = add_node(self.root)

    def print(self):

        def print_tree(node):
            if None != node:
                print_tree(node.left)
                print(node.value)
                print_tree(node.right)

        print_tree(self.root)

        
bst = BST()
bst.no

bst.add(10)
bst.add(20)
bst.add(30)
bst.add(40)
bst.add(12)
bst.add(5)
bst.add(99)


bst.print()