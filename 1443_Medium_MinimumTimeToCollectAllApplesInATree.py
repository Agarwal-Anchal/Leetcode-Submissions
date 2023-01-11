from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        visited=set()
        graph = defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        def dfs(root):
            visited.add(root)
            ans = sum (dfs(n) for n in graph[root] if n not in visited)
            if not ans and not hasApple[root]: return 0
            return ans+2
        return max(0,dfs(0)-2)
