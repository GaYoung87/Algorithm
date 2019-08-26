def dfs(adj):
    visit = [False] * 100
    stack = []
    stack.append(0)
    while stack:
        n = stack.pop()
        if not visit[n]:
            visit[n] = True
        stack.extend(adj[n])
    return stack
