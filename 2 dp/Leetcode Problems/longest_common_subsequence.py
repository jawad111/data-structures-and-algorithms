class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        rows = len(text1)
        colums = len(text2)

        cache = [[-1] * colums for _ in range(rows)]
        return self.dfs(text1, text2, 0, 0, cache)

    
    def dfs(self, text1, text2, i1, i2, cache):

        if(i1 == len(text1) or i2 == len(text2)):
            return 0

        if(cache[i1][i2] != -1):
            return cache[i1][i2]

        
        if(text1[i1] == text2[i2]):
            cache[i1][i2] = 1 + self.dfs(text1, text2, i1 + 1, i2 + 1, cache)
        else:
            cache[i1][i2] = max(self.dfs(text1, text2, i1 + 1, i2, cache), self.dfs(text1, text2, i1, i2 + 1, cache))

        return cache[i1][i2]

        