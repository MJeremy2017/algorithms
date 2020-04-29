class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class ListNode:
    def __init__(self):
        self.head = None
    
    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        # start from head
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        
    def reverse(self):
        if self.head is None:
            return
        
        prev_node = None
        curr_node = self.head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
        
    def insert(self, node, val):
        insert_node = Node(val)
        next_node = node.next
        node.next = insert_node
        insert_node.next = next_node
        
    def prepend(self, val):
        if self.head is None:
            return
        
        node = Node(val)
        node.next = self.head
        self.head = node
        
    def print_list(self):
        if self.head is None:
            return
        
        curr_node = self.head
        result = [curr_node.val]
        while curr_node.next:
            curr_node = curr_node.next
            result.append(curr_node.val)
        print(result)