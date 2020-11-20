def lca(p, graph):
    def dfs(node, path, res):
        if node == p:
            if len(res)<len(path):
                res = path
            return res
        for i in graph[node]:
            dfs(i, path+[i], res)

    for m in graph:
        dfs(m)