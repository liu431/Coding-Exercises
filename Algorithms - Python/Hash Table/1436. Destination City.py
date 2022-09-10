class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        org = paths[0][0]
        g = {}
        for path in paths:
            g[path[0]] = path[1]
        while org in g:
            des = g[org]
            org = des
        return des        
