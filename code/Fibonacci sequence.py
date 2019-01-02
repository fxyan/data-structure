class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        if n >= 2:
            s = []
            print(s)
            s.append(1)
            s.append(1)
            for i in range(2, n):
                s.append(s[i-1] + s[i-2])
            return s[n-1]


p = Solution()
print(p.Fibonacci(2))