# Merge sort
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array) // 2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArrays(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    k = i = j = 0
    while i < len(leftHalf) and j < len(rightHalf):
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1
        k += 1
    while i < len(leftHalf):
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf):
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1
    return sortedArray


# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays/0
T=int(input())
for i in range(T):
    n=list(map(int,input().split()))
    x=n[0]
    y=n[1]
    arr1= list(map(int,input().strip().split()))[:x]
    arr2= list(map(int,input().strip().split()))[:y]
    arr1.extend(arr2)
    print(*sorted(arr1))

# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
t = int(input())
for i in range (t):
    n = int(input())
    a = list(map(int, input().split()))
    c0=c1=c2 = 0
    for i in range(len(a)):
      if a[i]==0:
        c0 += 1
      elif a[i]==1:
        c1 += 1
      else : c2 +=1
    
    i = 0
    
    while c0 != 0:
      a[i] = 0
      c0 -= 1
      i += 1
    while c1 != 0:
      a[i]= 1
      c1 -= 1
      i += 1
    while c2 != 0:
      a[i]= 2
      c2 -= 1
      i += 1
    
    print(*a)