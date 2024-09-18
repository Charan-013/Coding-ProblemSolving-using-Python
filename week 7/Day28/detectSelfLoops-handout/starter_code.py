def detect_self_loops(graph):
    for k, v in graph.items():
        if k in v:
            return True
    return False


d = dict(eval(input()))

print(detect_self_loops(d))
