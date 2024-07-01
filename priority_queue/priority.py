class heap:
    def __init__(self):
        self.tree = [0]

    def insert(self,x):
        self.tree.append(x)
        self.swim()
    
    def swim(self):
        n = len(self.tree) -1 
        while n//2 >= 1 and self.tree[n] > self.tree[n//2]:
            self.tree[n],self.tree[n//2] = self.tree[n//2], self.tree[n]
            n //= 2

    def sink(self):
        n = len(self.tree)-1 
        i = 1
        while i*2 <= n :
            j = 2*i
            if self.tree[j] < self.tree[j+1]:
                j+= 1
            print(self.tree[i], self.tree[j])
            if self.tree[i] > self.tree[j]:
                break
            self.tree[i],self.tree[j] = self.tree[j],self.tree[i]
            #print(self.tree)
            i = j

    def del_max(self):
        self.tree.pop(1)
        self.sink()

    def get_max(self):
        if len(self.tree) > 2:
            return self.tree[1]
    
    def __str__(self):
        o = ''
        for i in self.tree:
            o += str(i)
            o += ' '
        return o

if __name__ == '__main__':
    h = heap()
    l = [22,33,45,40,44,45,48,51,53,56,65]
    for i in l:
        h.insert(i)
    for i in range(14):
        print(i,end = '  ')
    print()
    print(h)
    h.tree[1] = 43
    h.sink()
    print(h)
   


    
    
