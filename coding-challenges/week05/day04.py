# o(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range (len(nums)):
            for j in range (i+1, len(nums)):
                if(nums[i]+nums[j] == target):
                    return [i,j]
        return False

# o(n)
def twoSum(self, nums, target): 
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


# o(nlogn)
class Solution:
              
    def twoSum(self, nums, target):
       
        nums.sort()
        l = 0
        r = len(nums)- 1
        while l<r:
            currentSum = nums[l]+nums[r]
            if currentSum == target:
                return (nums[l],nums[r])
            elif currentSum < target:
                l +=1
            elif currentSum > target:
                r -= 1
        return []