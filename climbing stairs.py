class Solution:
    def climbStairs(self, n: int) -> int:
            a3=3
            a2=2
            if n<=3:
                return n
            else:
                for i in range(3,n,1):
                    k=a2+a3
                    a2=a3
                    a3=k
                return k
