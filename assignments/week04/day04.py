def bSearch(array, target):
  return bSearchHelperRecursive(array, target, 0, len(array)-1 )
#   return bSearchHelperIterative(array, target, 0, len(array)-1 )

def bSearchHelperRecursive(array, target, left, right):
  if left > right:
    return -1
  
  middle = (left+right)//2
  potentialMatch = array[middle]

  if target == potentialMatch:
    return middle
  elif target < potentialMatch:
    return bSearchHelperRecursive(array, target, left, middle-1)
  elif target > potentialMatch:
    return bSearchHelperRecursive(array, target, middle+1, right)

def bSearchHelperIterative(array, target, left, right):
  while left <= right:

    middle = (left+right)//2
    potentialMatch = array[middle]

    if target == potentialMatch:
      return middle
    elif target < potentialMatch:
      right = middle-1      
    elif target > potentialMatch:
      left = middle+1
      

  return -1

# driver
arr = [1,2,3,4,5,6,7,8]
print(bSearch(arr, 8))