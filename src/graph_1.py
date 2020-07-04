

def get_all_edges(graph): 
    for k in graph:
        for n in graph[k]: 
            print("{} -> {}".format(k, n))

def get_all_path(start_vertex, end_vertex, graph, path, visited): 
    path.append(start_vertex)
    #
    if start_vertex == end_vertex: 
        print(path)
        path.pop()
        return 
    if start_vertex not in graph: 
        path.pop()
        return  
    for n in graph[start_vertex]: 
        if n in path:
            continue
        r = get_all_path(n, end_vertex, graph, path, visited) 
    path.pop()


def get_path(start_vertex, end_vertex, graph, path, visited): 
    path.append(start_vertex)
    visited.append(start_vertex) 
    #
    if start_vertex == end_vertex: 
        print(path)
        return 1
    if start_vertex not in graph: 
        path.pop()
        return 0 
    for n in graph[start_vertex]: 
        if n in visited:
            continue
        r = get_path(n, end_vertex, graph, path, visited) 
        if r == 1: 
            return 1
    path.pop()
    return 0

graph = { "a" : ["d", "f"],
      "b" : ["c"],
      "c" : ["b", "c", "d", "e"],
      "d" : ["a", "c"],
      "e" : ["c"],
      "f" : ["d"]
    }

#get_all_edges(graph)
#get_path('a', 'b', graph, [], [])
get_all_path('a', 'b', graph, [], [])





