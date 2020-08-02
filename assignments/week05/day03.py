# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x/0
t = int(input())
for i in range (t):
    (n,x) = map(int,input().split())
    array = list(map(int, input().split()))[:n]
    flag = []
    for i in range(n):
        if array[i]==x:
            flag.append(i)

    if len(flag) == 0:
        print (-1)
    else:
        print (flag[0], flag[-1])

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        return Solution.peakHelper(nums, 0, len(nums)-1)
    
    def peakHelper(nums, left, right):
        if left == right:
            return right
        
        mid = (left+right)//2
        # [1,4,2,3,4]
        if(nums[mid] > nums[mid +1]):
            return Solution.peakHelper(nums,left, mid )
        else:
            return Solution.peakHelper(nums, mid +1 , right)