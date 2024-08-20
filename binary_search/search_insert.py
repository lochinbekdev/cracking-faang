""" Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. """

#Runtime complexity: 0(log n)

# incomplate solution

def sortedArray(array):
    if len(array) < 2:
        return array
    else:
        pivot=array[0]
        less=[i for i in array[1:] if i <= pivot]
        high=[i for i in array[1:] if i > pivot]
        return sortedArray(less) + [pivot] + sortedArray(high)

def searchInsert(nums,target:int)->int:
        low, high = 0, len(nums)-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        nums.append(target)
        nums = sortedArray(nums)
        return nums.index(target)

nums=[1,3,5,6]
print(searchInsert(nums,7))