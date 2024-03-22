def quick_sort(arr, start, end):

    # Don't do any operation and return once the two pointers meet or cross their positions
    if(end - start <= 0):
        return 
    
    # Initialize left and right pointer
    pivot = arr[end]
    left_pointer = start

    # Compare i with pivot and swap i with left_pointer. Increament left Pointer
    for i in range(start, end):
        if(arr[i] < pivot):
            temp = arr[i]
            arr[i] = arr[left_pointer]
            arr[left_pointer] = temp
            left_pointer+=1
    
    # Swap Left_Pointer value with Pivot
    arr[end] = arr[left_pointer]
    arr[left_pointer] = pivot
    
    # Break down Array into two from Left_pointer
    quick_sort(arr, start, left_pointer - 1)
    quick_sort(arr, left_pointer + 1, end)

    return arr
    




print(quick_sort([6, 2, 4, 1, 4], 0, 4))