# Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array.
# There is only one majority number in the array.
# O(n) time and O(1) extra space.

class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        count1 = count2 = 0
        res1 = None
        res2 = None
        for i in xrange(len(nums)):
            if res1 == None:
                res1 = nums[i]
                count1 += 1
            elif nums[i] == res1:
                count1 += 1
            elif res2 == None:
                res2 = nums[i]
                count2 += 1
            elif nums[i] == res2:
                count2 += 2
            else:
                count1 -= 1
                count2 -= 1
                if count1 < 0:
                    count1 = 1
                    res1 = nums[i]
                elif count2 < 0:
                    count2 = 1
                    res2 = nums[i]
        return res1 if nums.count(res1) > nums.count(res2) else res2
            
        
