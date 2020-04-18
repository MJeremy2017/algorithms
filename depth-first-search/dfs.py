class Graph:
    def __init__(self):
        self.graph = dict()
        self.path_all = []
        self.n = 0
        
    def add_edge(self, u, v):
        if u not in self.graph.keys():
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)
                
    def dfs2(self, start, end, path=[]):
        path.append(start)

        if start == end:
            print("find solution path", path)
            self.path_all.append(path)
            self.n += 1
            return 
        
        if start not in self.graph.keys():
            return
        
        neighbors = self.graph[start]
        for node in neighbors:
            if node not in path:
                self.dfs2(node, end, path.copy())  # need copy the list otherwise list would persist