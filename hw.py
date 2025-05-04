class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLL:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def search(self, key):
        current = self.head
        position = 0
        while current:
            if current.data == key:
                return position  
            current = current.next
            position += 1
        return -1  

l = SinglyLL()
l.insert_at_end(10)
l.insert_at_end(20)
l.insert_at_end(30)

key_to_search = 20
result = l.search(key_to_search)

if result != -1:
    print(f"Node with value {key_to_search} found at position {result}.")
else:
    print(f"Node with value {key_to_search} not found.")
