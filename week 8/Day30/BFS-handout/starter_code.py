def breadthFirstSearch(g, start):
    visited = []
    queue = [start]

    while queue:
        first = queue.pop(0)

        if first not in visited:
            visited.append(first)

            for neighbor in sorted(g[first]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited


print(breadthFirstSearch(eval(input()), "A"))

