class Node:
    def __init__(self, data):
        self.data= data
        self.next= None #address of the next node
        
        
class SinglyLL:
    def __init__(self):
        self.head= None
        
    def insert_beg(self, data):
        nb= Node(data)
        nb.next= self.head
        self.head= nb
        
    def insert_end(self, data):
        ne= Node(data)
        temp= self.head
        while temp.next:
            temp= temp.next
        temp.next= ne
        
    def display(self):
        if self.head== None:
            print("List is Empty")
        else:
            temp= self.head
            while temp:
                print(temp.data, '-->', end= " ")
                temp= temp.next
                
                
l= SinglyLL()
n= Node(10)
l.head= n
n1= Node(20)
n.next= n1
n2= Node(30)
n1.next= n2
l.display()
print(end= '\n')
l.insert_beg(100)
l.display()
print(end= '\n')
l.insert_end(200)
l.display()
        
        