class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        a={}
        c=0
        for i in tasks:
            if i in a: a[i]+=1
            else: a[i]=1
        for i in a.values():
            if i<2:
                return -1
            else:
                if i==2 or i==3: c+=1
                elif i==4: c+=2
                elif i>4 and i%3==0: c+=i//3
                else: c+=(i//3)+1
        return c
