
def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        
        vi = set()
        hm = {}
        
        def dfs(node, vi, hm):
            vi.add(node)
            copyNode = Node(node.val, [])
            hm[node] = copyNode
            
            for dest in node.neighbors:
                if dest not in vi:
                    dfs(dest, vi, hm)
                
                copyNode.neighbors.append(hm[dest])
        
        dfs(node, vi, hm)
        
        return hm[node]
"
