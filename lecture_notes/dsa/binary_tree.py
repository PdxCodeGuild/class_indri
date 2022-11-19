class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class Tree:
    def __init__(self, node= None):
        self.root = node

    def push(self, node):
        if self.root == None:
            self.root = node
        
        current = self.root
        while current:
            if node.value <= current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    break
            elif node.value > current.value:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break

    def print(self):
        print("""
    *
   ***
  *****
    *
        """)

tree = Tree()
nodeA = Node(2)
nodeB = Node(7)
nodeC = Node(4)

tree.push(nodeA)
tree.push(nodeB)
tree.push(nodeC)
tree.print()