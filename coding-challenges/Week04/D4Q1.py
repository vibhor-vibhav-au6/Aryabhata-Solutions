#Bubble Sort

# https://www.geeksforgeeks.org/bubble-sort/

# Python program for implementation of Bubble Sort 
  
def bubbleSort(arr): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n-1): 
    # range(n) also work but outer loop will repeat one time more than needed. 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
res=[]
print('Original array is:',arr) 
bubbleSort(arr) 
  
for i in range(len(arr)):
    res.insert(i,arr[i])  

print ("Sorted array is:",res) 

#--------------------------------------------------------------------------------------
# Optimized Bubble

# The above function always runs O(n^2) time even if the array is sorted. It can be optimized by stopping the algorithm if inner loop didn’t cause any swap.

# Worst and Average Case Time Complexity: O(n*n). Worst case occurs when array is reverse sorted.

# Best Case Time Complexity: O(n). Best case occurs when array is already sorted.

# Auxiliary Space: O(1)

# Boundary Cases: Bubble sort takes minimum time (Order of n) when elements are already sorted.

# Sorting In Place: Yes

# Stable: Yes

# Python3 Optimized implementation 
# of Bubble sort 
  
# An optimized version of Bubble Sort this one is O(n) 
def bubbleSort(arr): 
    n = len(arr) 
   
    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break

# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
res=[]
print('Original array is:',arr) 
bubbleSort(arr) 
  
for i in range(len(arr)):
    res.insert(i,arr[i])  

print ("Sorted array is:",res) 

#-------------------------------------------------------------------------
# Insertion Sort

# https://www.geeksforgeeks.org/insertion-sort/

# Time Complexity: O(n*2)

# Auxiliary Space: O(1)

# Boundary Cases: Insertion sort takes maximum time to sort if elements are sorted in reverse order. And it takes minimum time (Order of n) when elements are already sorted.

# Algorithmic Paradigm: Incremental Approach

# Sorting In Place: Yes

# Stable: Yes

# Online: Yes

# Uses: Insertion sort is used when number of elements is small. It can also be useful when input array is almost sorted, only few elements are misplaced in complete big array.

# What is Binary Insertion Sort?
# We can use binary search to reduce the number of comparisons in normal insertion sort. Binary Insertion Sort
# uses binary search to find the proper location to insert the selected item at each iteration.
# In normal insertion, sorting takes O(i)
# (at ith iteration) in worst case. We can reduce it to O(logi) by using binary search. The algorithm, as a whole,
#  still has a running worst case running time of O(n2) because of the series of swaps required for each insertion.

# Python program for implementation of Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >= 0 and key < arr[j] : 
                arr[j + 1] = arr[j] 
                j -= 1
        arr[j + 1] = key 
  
  
# Driver code to test above 
arr = [64, 34, 25, 12, 22, 11, 90] 
res=[]
print('Original array is:',arr) 
insertionSort(arr) 
  
for i in range(len(arr)):
    res.insert(i,arr[i])  

print ("Sorted array is:",res)
#---------------------------------------------------------------------
# Selection Sort

# https://www.geeksforgeeks.org/selection-sort/

# Time Complexity: O(n2) as there are two nested loops.

# Auxiliary Space: O(1)
# The good thing about selection sort is it never makes more than
# O(n) swaps and can be useful when memory write is a costly operation.

# Python program for implementation of Selection 
# Sort 

A = [64, 25, 12, 22, 11] 
print('Original array is:',A)
# Traverse through all array elements 
for i in range(len(A)): 
      
    # Find the minimum element in remaining  
    # unsorted array 
    min_idx = i 
    for j in range(i+1, len(A)): 
        if A[min_idx] > A[j]: 
            min_idx = j 
              
    # Swap the found minimum element with  
    # the first element         
    A[i], A[min_idx] = A[min_idx], A[i] 


#Driver Code
res=[]  

for i in range(len(A)):
    res.insert(i,A[i])  

print ("Sorted array is:",res)