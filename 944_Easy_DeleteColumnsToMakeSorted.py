class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        flag=0
        vis=set()
        for i in range(len(strs)-1):
            flag=0
            for j in range(len(strs[0])):
                if ord(strs[i][j])>ord(strs[i+1][j]):
                    if j not in vis:
                        c+=1
                    vis.add(j)
        print(c)
        return c
