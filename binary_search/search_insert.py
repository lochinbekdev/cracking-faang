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
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        elif nums[i] > target:
            array = nums + [target]
            sortedArr= sortedArray(array)
            return searchInsert(sortedArr,target)


