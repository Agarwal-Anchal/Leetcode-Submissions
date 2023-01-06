class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total=0
        c=0
        for i in costs:
            if coins>total and (coins-total)>=i: 
                total+=i
                c+=1
        return c
