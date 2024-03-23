def rob(nums, total, i):
    if(i > len(nums) - 1):
        return total

    print(nums[i])
    
    total =  rob(nums, nums[i] + total, i + 2)

    return total


 
nums = [1,3,1]
i = 0
total = 0

print(max(rob(nums, total, 0), rob(nums, total, i + 1))
)
