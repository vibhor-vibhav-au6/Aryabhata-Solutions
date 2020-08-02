# https://practice.geeksforgeeks.org/problems/number-of-occurrence/0
t = int(input())
for i in range (t):
    (n,x) = map(int,input().split())
    array = list(map(int, input().split()))[:n]
    flag = 0
    for i in range(n):
        if array[i]==x:
            flag += 1
    
    if flag == 0:
        print (-1)
    else:
        print (flag)


# https://leetcode.com/problems/find-peak-element/
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            if i < len(nums)-1:
                if nums[i]>nums[i+1]:
                    return i
        return (len(nums)-1)