class Head:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # also we can say we have initialised empty LL

    def append(self, data):
        newHead = Head(data)
        if self.head == None:
            self.head = newHead
            return
        else:
            current = self.head # obj avinash avi-->None
            while current.next is not None:
                current = current.next
            else:
                current.next = newHead

    def prepend(self,data):
        newHead = Head(data)
        newHead.next = self.head
        self.head = newHead

    def delete(self, data): # nav->ven->manisha->None
        
        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            current = self.head # obj Naveen
            while current.next is not None:
                if current.next.data == data:
                    current.next = current.next.next
                    return
                
                current=current.next

    def addingElementAnywhere(self, data, element):
        newHead = Head(data)
        current = self.head
        while current is not None:
            if current.data==element:
                newHead.next = current.next
                current.next = newHead
                return
            current = current.next

    
    

    def displayLL(self):
        current = self.head
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print('None')

ll = LinkedList()
ll.append("Avinash")
ll.append("Venkateshwar")
ll.append("Manisha")
ll.prepend("Naveen")

ll.delete('Avinash')

ll.addingElementAnywhere("Nihar", "Venkateshwar")
ll.displayLL()

