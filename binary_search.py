'''
Simple use of binary search algorithm in python
'''


def binary_search(val,target,low=None,high=None):
    if low is None or high is None:
        low = 0
        high = len(val) - 1

    mid = (low + high) // 2
    if low > high:
        return -1

    if val[mid] == target:
        return mid
    elif target < val[mid]:
        return binary_search(val,target,low,mid-1)
    else:
        return binary_search(val,target,mid+1,high)


val_int = [1,5,23,78,8,9,76]  # this is a integer list
val_int.sort()
# target = 9


val_str = ['apple','ball','egg','ice','nice'] # this is a string list
val_str.sort(key=str.lower)


target = input('Enter the item you want to search: ').lower()


index_target = binary_search(val_str,target)
if index_target != -1:
    print(f"The target is at index: {index_target}")
else:
    print('Not found')