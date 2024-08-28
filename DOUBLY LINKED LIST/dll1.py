class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyList:
    def __init__(self):
        self.head = None        

    
    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None            
            

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            #new_node.next = None
            self.head = new_node
        else:
            current = self.head
            new_node = Node(data)
            current.prev = new_node
            new_node.next = current
            new_node.prev = None
            self.head = new_node
            
 
    def add_after_node(self, key, data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.append(data)
                return
            elif current.data == key:
                new_node = Node(data)
                nxt = current.next
                current.next = new_node
                new_node.next = nxt
                new_node.prev = current
                if nxt:
                    nxt.prev = new_node   
                    return
            current = current.next


    def add_before_node(self, key, data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.prepend(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                current.prev = new_node
                new_node.next = current
                new_node.prev = prev
                prev.next = new_node
            current = current.next

    
    def delete(self,key):
        current = self.head
        while current:
            if current.data == key and current == self.head:
                #case 1
                if not current.next:
                    self.head = None
                    
                #case 2
                else:
                    nxt = current.next
                    nxt.prev = None
                    self.head = nxt
                    
                current.next = None
                current = None
                return True
                    
            elif current.data == key:
                #case 3
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current.prev = None
                    current = None
                    return True
                #case 4
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return True
                    
            current = current.next
        return False


    def printList(self):
        if self.head is None:
            return False
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next
                
            
dl2 = DoublyList()
dl2.append(23)
dl2.add_after_node(23, 12)
dl2.add_before_node(12, 98)
dl2.prepend(11)
dl2.append(0)
dl2.add_after_node(11, 98)
dl2.delete(12)
dl2.printList()
