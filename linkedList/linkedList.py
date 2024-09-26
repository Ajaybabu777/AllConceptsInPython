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
                


    def displayLL(self):
        current = self.head
        while current is not None:
            print(current.data, end="-->")
            current = current.next
        print('None')

ll = LinkedList()
ll.append("Avinash")
ll.append("Venkateshwar")


ll.displayLL()

