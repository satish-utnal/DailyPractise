class Solution:

    def solve(self, A):
        self.A = A
        if A % 400 == 0:
            return 1
        elif (A % 4 == 0) and (A % 100 != 0):
            return 1
        else:
            return 0


x = int(input())
p1 = Solution()
print(p1.solve(x))
