def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:       
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
                
def selection_sort(nums):
    for i in range(len(nums)):  
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

