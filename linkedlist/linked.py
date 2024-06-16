class Node:
    def __init__(self,data=-1):
        self.data = data
        self.next = None
    def __str__(self):
        print(self.data)

class Linkedlist:
    def __init__(self):
        self.head = Node()
    
    def push(self,node):
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = node

    def insert(self,x,i):
        if i >= self.length():
            self.push(x)
        else:
            ptr = self.head
            for j in range(i):
                ptr = ptr.next
            rest = ptr.next.next
            ptr.next = Node(x) 
            ptr = ptr.next
            ptr.next = rest
            
    def length(self):
        i = 0
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
            i+=1
        return i

    def pop(self):
        ptr = self.head
        if self.is_empty():
            raise IndexError ("list is empty can't pop")
        while ptr.next.next is not None:
            ptr = ptr.next
        ptr.next = None
    
    def dequeu(self):
        if self.is_empty():
            raise IndexError("list is empty")
        ptr = self.head
        ptr.next = ptr.next.next

    def remove(self,x):
        ptr = self.head
        while ptr.next is not None and ptr.next.data != x:
            ptr = ptr.next
        ptr.next = ptr.next.next
    
    def is_empty(self):
        return self.head.next is None

    def __str__(self):
        o = ''
        ptr = self.head
        while ptr is not None:
            o += str(ptr.data)
            o += ' -> '
            ptr = ptr.next
        o += 'None'
        return o


if __name__ == '__main__':
    linked_list = Linkedlist()
    for i in range(10):
        linked_list.push(Node(i))
    print(linked_list)
    linked_list.insert(1111,2)
    print(linked_list)


    

        


