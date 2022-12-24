
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Stack:

    def __init__(self, node = None):
        self.head = node

    def push(self, value):
        # Create new node
        new_node = Node(value)
        # Point it to current head
        new_node.next = self.head
        # Move head, to the new node
        self.head = new_node

    def pop(self):
        # Move head to next item in the stack
        if self.head != None:
            self.head = self.head.next

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next




class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        if self.head != None:
            self.head = self.head.next
        else:
            self.tail = None

    def push(self, value):
        # create new node
        new_node = Node(value)

        # If no head, point head and tail to first node
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            # point tail's next to new node
            self.tail.next = new_node
            # point tail to new node
            self.tail = new_node



    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next



# queue = Queue()
# queue.push(4)
# queue.push(8)
# queue.push(16)
# queue.pop()
# queue.pop()
# queue.pop()
# queue.pop()
# queue.print()

# print(queue.tail)

# stack = Stack()
# stack.push(4)
# stack.push(8)
# stack.push(16)
# stack.pop() # 16
# stack.pop() # 8
# stack.pop() # 4
# stack.pop() # ???

# stack.print()


# head = Node(4, Node(8, Node(16, Node(32, Node(64, Node(128))))))

# current = head

# while current:
#     print(current.value)
#     current = current.next