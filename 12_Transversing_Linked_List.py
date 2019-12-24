# Implementing and Traversing a Linked List
#   2  ->   1   ->  4   ->  3   ->  5   -> None
#  Head


class SLLNode:
    def __init__(self, value):
        self.data = value
        self.next = None

    def __repr__(self):
        return f"SLLNode Object :: DATA -> {self.data}"

    def set_data(self, newData):
       """Replace the existing value of self.data attribute with newData parameter"""
       self.data = newData

    def get_data(self):
        """Returns the self.data attribute"""
        return self.data

    def set_next(self, newNext):
        """Replace the existing value of self.next attribute with newNext parameter"""
        self.next = newNext

    def get_next(self):
        """Returns the self.next attribute"""
        return self.next

# head = Node(2)
# head.next = Node(1)
# print(head.value) # 2
# print(head.next.value) # 1

# At this point, linked list look like this:
# 2     ->   1
# Head

# Our Goal is to extend the list until it look like this:
#   2  ->   1   ->  4   ->  3   ->  5   -> None


class SLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        return f"SLL Object :: HEAD -> {self.head} : TAIL -> {self.tail} : LENGTH -> {self.length}"

#===========================CREATE LINKED LIST============================#

    def create_linked_list(self, li):
        self.head = SLLNode(li.pop(0))
        self.tail = self.head  # When we only have 1 node, head and tail refer to the same node
        self.length = 1
        try:
            while len(li) > 0:
                # Attach the new node to the `next` of tail
                self.tail.next = SLLNode(li.pop(0))
                self.tail = self.tail.next  # Update the tail
                self.length += 1
        except IndexError:
            self.head = None
        return self

#===========================TO PRINT LINKED LIST============================#
    # Traversing the list
    def traverse_list(self):
        """Print Every Item in the List"""
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

#===========================TO CHECK IF LINKED LIST IS EMPTY============================#

    def is_empty(self):
        """Returns True if SLL is Empty, else it will return False"""
        return self.head is None

#===========================SEARCH ELEMENT FROM LINKED LIST============================#

    def get(self, index):
        """Returns Data by Index"""
        if index < 0 or index > self.length:
            return None
        count = 0
        current = self.head
        while count != index:
            current = current.next
            count += 1
        return current

#===========================ADDING ELEMENTS TO LINKED LIST============================#
    def prepend(self, newData):
        newNode = SLLNode(newData)
        if self.is_empty():
            self.head = newNode
            self.tail = self.head
        else:
            newNode.set_next(self.head)
            self.head = newNode
        self.length += 1
        return self

    def append(self, newData):
        """ Append a value to the end of the list. """
        newNode = SLLNode(newData)
        if self.is_empty():
            self.head = newNode
            self.tail = self.head
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return self

    def insert(self, index, newData):
        if index < 0 or index > self.length:
            return None
        if index == self.length:
            self.append(newData)
            return True
        if index == 0:
            self.prepend(newData)
            return True
        newNode = SLLNode(newData)
        prev = self.get(index-1)
        temp = prev.get_next()  # This Command is used to avoid breaking of Linked List
        prev.set_next(newNode)
        newNode.set_next(temp)
        self.length += 1
        return self

#===========================CONVERTING LINKED LIST TO LIST============================#

    def to_list(self):
        node_values = []
        node = self.head
        while node:
            node_values.append(node.data)
            node = node.next
        return node_values

    def search(self, searchValue):
        """ Search the linked list for a node with the requested value and return the node. """
        position_tail = self.head
        while position_tail.next:
            if position_tail.data == searchValue:
                return position_tail
            position_tail = position_tail.next
        return None 

    def size(self):
        position_tail = self.head
        ll_length = 0
        while position_tail is not None:
            position_tail = position_tail.next
            ll_length += 1
        return ll_length

sll = SLL()
print(sll.is_empty())  # True
sll.create_linked_list([2, 1, 4, 3, 5])
######   OUTPUT     ######
# SLLNode Object :: DATA -> 2
# SLLNode Object :: DATA -> 1
# SLLNode Object :: DATA -> 4
# SLLNode Object :: DATA -> 3
# SLLNode Object :: DATA -> 5
# None
print(sll.is_empty())  # False
print(sll.traverse_list())
print(sll.is_empty())  # False
# SLL Object :: HEAD -> SLLNode Object :: DATA -> 2 : TAIL -> SLLNode Object :: DATA -> 6 : LENGTH -> 6
print(sll.append(6))
print(sll.length)  # 6
print(sll.to_list())  # [2, 1, 4, 3, 5, 6]
# SLL Object :: HEAD -> SLLNode Object :: DATA -> 8 : TAIL -> SLLNode Object :: DATA -> 6 : LENGTH -> 7
print(sll.prepend(8))
# SLL Object :: HEAD -> SLLNode Object :: DATA -> 10 : TAIL -> SLLNode Object :: DATA -> 6 : LENGTH -> 8
print(sll.prepend(10))
print(sll.to_list())  # [10, 8, 2, 1, 4, 3, 5, 6]
print(sll.insert(2, 9))
print(sll.to_list())  # [10, 8, 9, 2, 1, 4, 3, 5, 6]
print(sll.search(13)) # None
print(sll.size()) # 9