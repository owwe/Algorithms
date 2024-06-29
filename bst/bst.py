class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)
    
class binary_search_tree:
    def __init__(self):
        self.root = None
    def insert(self,x):
        ptr = self.root
        if ptr is None:
            self.root = Node(x)
            return True
        while ptr is not None:
            if x < ptr.data:
                if ptr.left is None :
                    ptr.left = Node(x)
                    break
                ptr = ptr.left
            else:
                if ptr.right is None:
                    ptr.right = Node(x)
                    break
                ptr = ptr.right
    def get(x):
        ptr = self.root
        while ptr :
            if ptr.data < ptr.left.data:
                return 1

        

if __name__ == "__main__":
    bst = binary_search_tree()
    bst.insert(10)
    bst.insert(4)
    bst.insert(11)
    bst.insert(5)
    bst.insert(14)
    print(bst.root)
    print(bst.root.left)
    print(bst.root.right)
    print(5 < None)


