class Graph:
    def __init__(self,path):
        with open(path,'r') as file:
            v = file.readline()
            e = file.readline()
            vertices = [[] for i in range(int(v))]
            for line in file:
                a,b = line[:-1].split(' ')
                a,b = int(a),int(b)
                vertices[a].append(b)
                vertices[b].append(a)
        self.vertices =  vertices
        self.v = int(v)

    def add_edge(self,a,b):
        self.vertices[a].append(b)
        self.vertices[b].append(a)

    def printer(self):
        for i,v in enumerate(self.vertices):
            print(i,'-',v)
class Digraph:
    def __init__(self,path):
        with open(path,'r') as file:
            v = file.readline()
            e = file.readline()
            vertices = [[] for i in range(int(v))]
            for line in file:
                a,b = line[:-1].split(' ')
                a,b = int(a),int(b)
                vertices[a].append(b)
        self.vertices =  vertices
        self.v = int(v)

    def add_edge(self,a,b):
        self.vertices[a].append(b)

    def printer(self):
        for i,v in enumerate(self.vertices):
            print(i,'-',v)
class Search:
    def __init__(self,Graph):
        self.graph = Graph
        self.visited = [False for i in range(Graph.v)]
        self.edgeTo = [None for i in range(Graph.v)]
        self.frontier = []
        self.id_ = [None for i in range(Graph.v)]
        self.count = 1

    def dfs(self,s):
        self.visited[s] = True
        self.frontier.append(s)
        while self.frontier:
            node = self.frontier.pop()
            for w in self.graph.vertices[node]:
                if self.visited[w] == False:
                    self.edgeTo[w] = node
                    self.visited[w] = True
                    self.frontier.append(w)

    def get_clusters(self):
        for i in range(self.graph.v):
            self.dfs(i)
            self.count += 1

    def bfs(self,s):
        self.visited[s] = True
        self.frontier.append(s)
        while self.frontier:
            node = self.frontier.pop(0)
            for w in self.graph.vertices[node]:
                if self.visited[w] == False:
                    self.edgeTo[w] = node
                    self.visited[w] = True
                    self.frontier.append(w)
                  
    def dfs_r(self,s):
        self.visited[s] = True
        for w in self.graph.vertices[s]:
            if self.visited[w] == False:
                self.dfs_r(w)
                self.edgeTo[w] = s
            
    def get_path(self,s,t):
        i = self.edgeTo[t]
        ans = [t]
        while i is not None:
            ans.append(i)
            i = self.edgeTo[i]
        return ans[::-1]


if __name__ == "__main__":
    g = Digraph('digraph.txt')
    g.printer()
    print()

    # bfs_search = Search(g)
    # bfs_search.bfs(0)
    # print(bfs_search.get_path(0,3))

    # dfs_search = Search(g)
    # #dfs_search.dfs(0)
    # #print(dfs_search.get_path(0,3))
    # dfs_search.get_clusters()
    # print(dfs_search.edgeTo)
    # print(dfs_search.id_)

    search = Search(g)
    search.dfs(0)
    print(search.edgeTo)
    print(search.get_path(0,2))

   

 
