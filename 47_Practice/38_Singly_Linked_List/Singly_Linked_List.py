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
        return self

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

    def shift(self):
        if not self.head:
            return None

        currNode = self.head
        self.head = currNode.next

        self.length -= 1
        if self.length == 0:
            self.tail = None

        return currNode.val

    def unshift(self, val):
        newNode = Node(val)

        if self.length == 0:
            self.head = newNode
            self.tail = newNode

        if self.length >= 1:
            newNode.next = self.head
            self.head = newNode

        self.length += 1

        return self

    def get(self, idx):
        if idx < 0 or idx >= self.length:
            return None
        count = 0
        currNode = self.head
        while count != idx:
            currNode = currNode.next
            count += 1
        return currNode

    def set(self, idx, val):
        """ Update the Val at the Given Index"""
        foundNode = self.get(idx)
        if foundNode:
            foundNode.val = val
            return True
        return False

    def insert(self, idx, val):
        """ Adding a Node to the Linked List at a Specific Position"""
        newNode = Node(val)
        prevNodeFound = self.get(idx - 1)
        nextNodeFound = prevNodeFound.next
        if prevNodeFound:
            prevNodeFound.next = newNode
            newNode.next = nextNodeFound
            return True
        return False

    def remove(self, idx):
        # Remove Node by Index
        if idx < 0 and idx > self.length:
            return None
        if idx == self.length - 1:
            return self.pop()
        if idx == 0:
            return self.shift()
        prevNodeFound = self.get(idx - 1)
        removed = prevNodeFound.next
        prevNodeFound.next = removed.next
        self.length -= 1
        return removed

    def reverse(self):
        # Reversing the Linked List in Place
        currNode = self.head
        self.head, self.tail = self.tail, self.head
        prevNode = None
        while currNode is not None:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
        return self

    def rotate(self, pos):
        if pos < 0 or pos > self.length - 1:
            return None
        count = 0
        while pos != count:
            currNode = self.head
            self.head = currNode.next
            currNode.next = None
            self.tail.next = currNode
            self.tail = currNode
            count += 1
        return self

newNode = SLL()
newNode.push(1).push(2).push(3).push(4)
# newNode.traverse()
# newNode.pop()
# newNode.pop()
# newNode.traverse()
# newNode.shift()
# newNode.traverse()
# newNode.shift()
# newNode.traverse()
# newNode.shift()
# newNode.unshift(56).unshift(67)
# newNode.traverse()
# print(newNode.get(3)) # 4
# print(newNode.get(0)) # 1
# print(newNode.get(-1)) # None
# newNode.set(2, 29)
# newNode.insert(2, 1990)
# newNode.traverse()
# newNode.remove(2)
# newNode.reverse()
newNode.rotate(2)
newNode.traverse()
