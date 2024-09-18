def depthFirstSearch(g, start, visited=None):
    if visited is None:
        visited = []

    if start not in visited:
        visited.append(start)
        
        for neighbour in sorted(g[start]):
            if neighbour not in visited:
                depthFirstSearch(g, neighbour, visited)
    return visited


start = "A"
g = eval(input())
print(depthFirstSearch(g, start))
