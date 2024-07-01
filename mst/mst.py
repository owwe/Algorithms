class Edge:
    def __init__(self,v,w,weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v
    
    def other(self,v):
        if v == self.v:
            return self.w
        else:
            return self.v      
    def __lt__(self,that):
        if isinstance(that,Edge):
            return self.weight < that.weight
    def __gt__(self,that):
        if isinstance(that,Edge):
            return self.weight > that.weight
    def __eq__(self,that):
        if isinstance(that,Edge):
            condition1 = (self.v == that.v) and (self.w == that.w)
            condition2 = (self.v == that.w) and (self.w == that.v)
            condition3 = self.weight == that.weight
            return (condition1 or condition2) and condition3
    def __str__(self):
        return f'{self.v}-{self.w} {self.weight}'
        
class EdgeWeigthedGraph:
    def __init__(self,path):
        with open(path,'r') as file:
            v_ = file.readline()
            e_ = file.readline()
            vertices = [[] for i in range(int(v_))]
            edges = []
            for line in file:
                v,w,weight = line[:-1].split(' ')
                v = int(v)
                w = int(w)
                weight = float(weight)
                edge = Edge(v,w,weight)
                edges.append(edge)
                vertices[v].append(edge)
                vertices[w].append(edge)
        self.vertices = vertices
        self.edges = edges
        self.v = int(v_)

    def add_edge(self,that):
        v,w = that.either, that.other
        self.vertices[v].append(that)
        self.vertices[w].append(that)

    def printer(self):
        for i,edges in enumerate(self.vertices):
            for edge in edges:
                v = edge.other(i)
                print(f'{i}-{v} {edge.weight}', end = '| ')
            print()

    def __str__(self):
        o = ''
        for i,edges in enumerate(self.vertices):
            for edge in edges:
                v = edge.other(i)
                o += f'{i}-{v} {edge.weight} | '
            o+= '\n'
        return o


class MinPQ:
    def __init__(self):
        self.queue = [0]

    def swim(self):
        n = len(self.queue) -1
        while n //2 >= 1 and self.queue[n] < self.queue[n//2]:
            self.queue[n],self.queue[n//2] = self.queue[n//2],self.queue[n]
            n //= 2

    def sink(self):
        n = len(self.queue) -1
        i = 1
        while i * 2  < n:
            j = i * 2
            if self.queue[j] > self.queue[j+1]:
                j += 1
            if self.queue[i] < self.queue[j]:
                break
            self.queue[i],self.queue[j] = self.queue[j],self.queue[i]
            i = j

    def pop_min(self):
        if len(self.queue) >= 2:
            min = self.queue.pop(1)
            self.sink()
            return min

    def insert(self,i):
        self.queue.append(i)
        self.swim()

    def isEmpty(self):
        return len(self.queue) == 1
    
    def __str__(self):
        o = ''
        for i in self.queue:
            o += str(i)
            o += ' '
        return o

class UnionFind:
    def __init__(self,v):
        self.ids = [i for i in range(v)]
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

    def solve(self,data):
        for edge in data:
            self.union(edge.v,edge.w)

class KruskalMST:
    def __init__(self,G):
        self.mst = []
        pq = MinPQ()
        for edge in G.edges:
            pq.insert(edge)
        Uf = UnionFind(G.v)
        while pq.isEmpty() == False and len(self.mst) < G.v - 1:
            e = pq.pop_min()
            v ,w = e.v, e.w
            if Uf.connected(v, w) == False:
                Uf.union(v, w)
                self.mst.append(e)

    def __str__(self):
        o = ''
        for edge in self.mst:
            v = edge.v
            w = edge.w
            o += f'{v}-{w} {edge.weight} | '
        return o
    
class PrimsMST:
    def __init__(self,G):
        self.mst = []
        Uf = UnionFind(G.v)
        self.pq = MinPQ()
        self.marked = [False for i in range(G.v)]
        self.visit(G,0)
        while (self.pq.isEmpty() == False):
            min_edge = self.pq.pop_min()
            v = min_edge.either()
            w = min_edge.other(v)
            if self.marked[v] and self.marked[w]:
                continue
            self.mst.append(min_edge)
            if self.marked[v] == False:
                self.visit(G,v)
            if self.marked[w] == False:
                self.visit(G,w)
    
    def visit(self,G,v):
        self.marked[v] = True
        for edge in G.vertices[v]:
            if self.marked[edge.other(v)] == False:
                self.pq.insert(edge)

    def __str__(self):
        o = ''
        for edge in self.mst:
            v = edge.v
            w = edge.w
            o += f'{v}-{w} {edge.weight} | '
        return o
  
if __name__ == "__main__":
    graph = EdgeWeigthedGraph('tiny.txt')

    #graph.printer()
    print('minimum spanning tree')
    # kruskalMST = KruskalMST(graph)
    # print(kruskalMST)
    prims = PrimsMST(graph)
    print(prims)


    

