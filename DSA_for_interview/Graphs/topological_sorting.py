'''
perform topological sorting
'''


class Solution:
    def topologicalsortUtil(self,v,adj,visited,st):
        visited[v] = True

        for i in adj[v]:
            if not visited[i]:
                self.topologicalsortUtil(i,adj,visited,st)

        st.append(v)
    def topologicalSort(self, adj):
        v = len(adj)
        st = []
        visited = [False] * v

        for i in range(v):
            if not visited[i]:
                self.topologicalsortUtil(i,adj,visited,st)

        return st[::-1]