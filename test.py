# Time: 0(2^(n + m)), Space: 0(n + m)
def dfs(s1, s2):
    return dfsHelper (s1, s2, 0, 0)
def dfsHelper (s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2) :
        return 0
    if s1[i1] == s2[i2]:
        return 1 + dfsHelper (s1, s2, i1 + 1, i2 + 1) 
    else:
        return max(dfsHelper (s1, s2, i1 + 1, i2),
        dfsHelper (s1, s2, i1, i2 + 1))


print(dfs(["a", "d", "c" , "b"], ["a", "b", "c"]))