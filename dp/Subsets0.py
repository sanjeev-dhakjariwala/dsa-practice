class Solution:
    def generateSubSets(self, s):
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                print(s[i: j + 1])
        
sol = Solution()
print(sol.generateSubSets("abc"))
