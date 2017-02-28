graph = {'a': {'b':3, 'c':2},
             'b': {'c':4, 'd':4},
             'c': {'d':4},
             'd': {'c':6},
             'e': {'f':1},
             'f': {'c':1}}

def find_path(graph, src, dest, path=[]):
    path = path + [src]
    if src == dest:
        return [path]
    if src not in graph:
        return None
    for node in graph[src]:
        if node not in path:
            newpath = find_path(graph, node, dest, path)
            if newpath: return newpath
    return None

def find_all_path(graph, src, dest, path=[]):
    path = path + [src]
    if src == dest:
        return [path]
    if src not in graph:
        return None
    paths = []
    for node in graph[src]:
        if not node in path:
            newpath = find_all_path(graph, node, dest, path)
            for new in newpath:
                paths.append(new)
    return paths

def length(graph, path=[]):
    sum = 0
    for i in range(0, len(path) - 1):
        sum = sum + graph[path[i]][path[i + 1]]
    return sum

def find_shortest_path(graph, src, dest, path=[]):
    path = path + [src]
    if src == dest:
        return path
    if not src in graph:
        return None
    shortest = None
    for node in graph[src]:
        if node not in path:
            newpath = find_shortest_path(graph, node, dest, path)
            if newpath:
                if not shortest or length(graph, newpath) < length(graph, shortest):
                    shortest = newpath
    return shortest

print(find_shortest_path(graph, 'a', 'd'))
print(length(graph, find_shortest_path(graph,'a', 'd'))/60)