class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph=defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        res=[0]*len(labels)

        def dfs(node, par):
            nonlocal res
            count = Counter()

            for nei in graph[node]:
                if nei != par:
                    count += dfs(nei, node)

            count[labels[node]] += 1
            res[node] = count[labels[node]]
            return count
            
        dfs(0,-1)
        return res
