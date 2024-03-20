'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

'''
import time


def search(nums, target):
    low = 0
    high = len(nums) - 1
    

    while low <= high:
        mid = (high + low) // 2
        print(low, high)
        time.sleep(1)
        if(target > nums[mid]):
            low  = mid + 1
        elif(target < nums[mid]):
            high = mid - 1
        else:
            return mid
        
    return -1


print(search([-1,0,3,5,9,12], 12))


