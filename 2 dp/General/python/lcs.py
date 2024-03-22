# LCS

# Time: 0(2^(n + m)), Space: 0(n + m)
# Where n and m are the number of items in array 1 and array 2 respectively.


def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    return dfs(text1, text2, 0, 0)


def dfs(text1, text2, i1, i2):
    
    if(i1 == len(text1) or i2 == len(text2)):
        return 0

    

    if(text1[i1] == text2[i2]):
        return 1 + dfs(text1, text2, i1 + 1, i2 + 1)
    else:
        return max(dfs(text1, text2, i1 + 1, i2), dfs(text1, text2, i1, i2 + 1))

