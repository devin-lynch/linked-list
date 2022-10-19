class Node:
    '''
        singly linked list node
    '''
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

node_one = Node(1, None)
# print(node_one)
# manually inserting nodes
node_two = Node(2, None)
node_one.next = node_two
print(f'first node: {node_one} seccond node: {node_one.next}')

class Linkedlist:
    '''
        singly linked list manager class
    '''
   