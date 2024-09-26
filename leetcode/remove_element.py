# My first solution

def remove_element(nums, val:int):
    r_nums=[]
    k=0
    for num in nums:
        if num != val:
            r_nums.append(num)
            k+=1
        else:
            r_nums.append('_')
    
    return f'key: {k}',f'nums:{r_nums}' 

nums=[3,2,2,3]
val=3
print(remove_element(nums,val))