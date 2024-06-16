from utils import get_input, get_input_gen
import time
from matplotlib import pyplot as plt  
import numpy as np
class UnionFind:
    def __init__(self,data):
        self.ids = [i for i in range(len(data)-1)]
        self.data = data
        self.counter = 0
    def connected(self,p,q):
        return self.ids[p] == self.ids[q]
    def union(self,p,q):
        if not self.connected(p,q):
            class_p = self.ids[p]
            class_q = self.ids[q]
            for i in range(len(self.ids)):
                if self.ids[i] == class_p:
                    self.ids[i] = class_q
        return self.ids
    def solve(self):
        for p,q in self.data:
            self.union(p,q)
        return self.ids


class QuickFind:
    def __init__(self,data):
        self.ids = [i for i in range(len(data)-1)]
        self.counter = 0
        self.data = data

    def connected(self,p,q):
        return self.find_root(p) == self.find_root(q)
    
    def find_root(self,p):
        while self.ids[p] != p:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
        return p
    
    def union(self,p,q):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        self.ids[p_root] = q_root
        
    def solve(self):
        for p,q in self.data:
            self.union(p,q)
        return self.ids


class WeightedQuickFind:
    def __init__(self,data):
        self.ids = [i for i in range(len(data)-1)]
        self.counter = 0
        self.data = data
        self.w = [1 for i in range(len(data) -1)]

    def connected(self,p,q):
        return self.find_root(p) == self.find_root(q)
    
    def find_root(self,p):
        while self.ids[p] != p:
            self.ids[p] = self.ids[self.ids[p]]
            p = self.ids[p]
        return p
    
    def union(self,p,q):
        p_root = self.find_root(p)
        q_root = self.find_root(q)
        if p_root != q_root:
            if self.w[q_root] <= self.w[p_root]:
                self.ids[q_root] = p_root
                self.w[p_root] += self.w[q_root]
            else:
                self.ids[p_root] = q_root
                self.w[q_root] += self.w[p_root]
        
    def solve(self):
        for p,q in self.data:
            self.union(p,q)

        return self.ids


class Grid:
    def __init__(self,n = 8,p = 0.3):
        rng = np.random.default_rng(1)
        grid = rng.random((n, n))
        self.grid = np.where(grid > p, 1, 0) 
        self.n = n
        self.total = n * n
        self.walls = self.grid.sum()
        self.open_sites = self.total - self.walls

    def visualize(self):
        plt.imshow(self.grid,cmap = 'binary')
        plt.title(f'{self.n} by {self.n}')
        plt.xlabel(f'open sites: {self.open_sites}')
        plt.ylabel(f'walls: {self.walls}')
        plt.show()

    def __str__(self):
        o = ''
        for line in self.grid:
            for i in line:
                o += f' {i} '
            o+='\n'
        return o

class percolation:
    def __init__(self,n):
        self.grid = np.ones((n,n))
        self.n = n

    def open(self,r,c):
        if self.isFull(r,c):
            self.grid[r,c] = 0

    def isOpen(self,r,c):
        return self.grid[r,c] == 0
    
    def isFull(self,r,c):
        return self.grid[r,c] == 1
    
    def numberOfOpenSites(self):
        return self.n * self.n - self.grid.sum()
    
    def visualize(self):
        plt.imshow(self.grid,cmap = 'binary')
        plt.title(f'{self.n} by {self.n}')
        plt.xlabel(f'open sites: {self.numberOfOpenSites()}')
        plt.ylabel(f'walls: {self.grid.sum()}')
        plt.show()

    def get_neighboors(self):
        data = [i for i in range(self.n*self.n)]
              

def compare():
    data = get_input('largeUF.txt')
    # QF = QuickFind(data)
    # print('quick union find :',QF.solve())
    #UF = UnionFind(data)
    #print("normal union find",UF.solve())
    start_time = time.time()
    WQF = WeightedQuickFind(data)
    WQF.solve()
    end_time = time.time()
    print(end_time - start_time)

def test():
    n = 5
    p = 0.5
    g = Grid(n,p)
    rng = np.random.default_rng(2)
    grid = rng.random((n, n))
    grid = np.where(grid > p, 1, 0)

    print(np.sum(grid))
    grid = Grid(n,p)
    print(grid)
    grid.visualize()






if __name__ == '__main__':

    # QuickFind(data).union(6,5)
    # QuickFind(data).union(9,4)
    test()