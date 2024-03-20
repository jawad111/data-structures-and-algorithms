
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    characterCountA = {}
    characterCountB = {}

    for a in s:
        if(a in characterCountA):
            characterCountA[a] = characterCountA[a] + 1
        else:
            characterCountA[a] = 0
    
    for b in t:
        if(b in characterCountB):
            characterCountB[b] = characterCountB[b] + 1
        else:
            characterCountB[b] = 0
    print(characterCountA , characterCountB)
    
    for a in s:
        
        if((a in characterCountA and a in characterCountB) and characterCountA[a] == characterCountB[a]):
            continue
        else:
            return False
        
    return True


    
print(isAnagram("rca", "car"))