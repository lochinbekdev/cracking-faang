"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

def sortedArray(list):
    if(len(list) < 2):
        return list
    else:
        pivot = list[0]
        less=[i for i in list[1:] if i <= pivot]
        high=[i for i in list[1:] if i > pivot]
        return sortedArray(less) + [pivot] + sortedArray(high)

def merge_two_list(list1,list2):
    if len(list1) | len(list2) < 0:
        return []
    else:
        merge_arr=list1 + list2
        return sortedArray(merge_arr)
    

list1=[]
list2=[0]
result=merge_two_list(list1,list2)
print(result)
