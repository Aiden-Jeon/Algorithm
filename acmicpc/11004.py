import sys
n,k = list(map(int,sys.stdin.readline().strip().split()))
nums = sys.stdin.readline().split(' ')
for i in range(len(nums)):
    nums[i] = int(nums[i])

def quick_selection(arr, kth):
    pivot = arr[(len(arr)+1)//2 - 1]
    left, mid, right = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            mid.append(arr[i])
    
    if kth < len(left):
        return quick_selection(left, kth)
    elif kth < len(left) + len(mid):
        return mid[0]
    else:
        return quick_selection(right, kth - len(left) - len(mid))

print(quick_selection(nums,k-1))
