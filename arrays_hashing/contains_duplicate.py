def containsDuplicate(nums):
        entries = set()
        for num in nums:
            if(num in entries):
                return True
            else:
                entries.add(num)
        
        return False
        
                
                
    
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
