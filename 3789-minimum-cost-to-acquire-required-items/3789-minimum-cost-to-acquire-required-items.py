class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        ans = 0
        if cost1<=cost2:
            c1,c2 = cost1,cost2
            n1,n2 = need1,need2
        else:
            c1,c2 = cost2,cost1
            n1,n2 = need2,need1

        def f(a):
            if a >= 0:
                return a
            return 0

        m,M = min(n1,n2),max(n1,n2)

        if costBoth <= c1:
            return costBoth*M
        elif c1 < costBoth and costBoth <= c2:
            return c1*f(n1-n2)+costBoth*(n2)
        elif costBoth > c2 and costBoth < c1+c2:
            return c1*f(n1-n2) + c2*f(n2-n1) + costBoth*m
        else:
            return c1*n1+c2*n2