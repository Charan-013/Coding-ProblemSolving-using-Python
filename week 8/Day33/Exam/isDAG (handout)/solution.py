def is_dag(graph: dict) -> bool:
    def dfs(node):
        if state[node] == 'VISITING':
            return False
        if state[node] == 'VISITED':
            return True
        
        state[node] = 'VISITING'
        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False
        
        state[node] = 'VISITED'
        return True
    
    state = {node: 'UNVISITED' for node in graph}
    
    for node in graph:
        if state[node] == 'UNVISITED':
            if not dfs(node):
                return False
    
    return True



d = eval(input())
print(is_dag(d))