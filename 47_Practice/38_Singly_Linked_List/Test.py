class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


class SLL:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def traverse(self):
        if self.head is None:
            return None
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.val)
            currentNode = currentNode.next

    def pop(self):
        if self.length == 0:
            return None

        currentNode = self.head
        prevNode = currentNode

        while currentNode.next is not None:
            prevNode = currentNode
            currentNode = currentNode.next

        prevNode.next = None
        self.tail = prevNode

        if self.length == 1:
            self.head = None
            self.tail = None

        self.length -= 1

        return currentNode
