import collections

def minScore(n, roads):
    m = collections.defaultdict(list)
    
    for a,b,value in roads:
        m[a].append([b, value])
        m[b].append([a, value])
    res = 1000000000
    
    visit = set()
    
    def dfs(node):
        visit.add(node)
        nonlocal res

        for nei, cost in m[node]:
            res = min(res, cost)
            
            if nei in visit:
                continue
            dfs(nei)
            
    dfs(1)
    
    return res

n = 4
roads = [[1,2,2],[1,3,4],[3,4,7]]

minScore(n, roads)