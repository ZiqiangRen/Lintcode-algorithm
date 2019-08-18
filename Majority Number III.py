# Given an array of integers and a number k, the majority number is the number that occurs more than 1/k of the size of the array.
# There is only one majority number in the array.
# O(n) time and O(k) extra space.


class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        count = collections.defaultdict(int)
        for n in nums:
            if n in count or len(count) < k:
                count[n] += 1
            else:
                for key in dict(count):
                    count[key] -= 1
                    if count[key] == 0:
                        count.pop(key)
                if len(count) < k:
                    count[n] = 1
        for key in count:
            count[key] = 0
        res = 0
        m = -1
        for n in nums:
            if n in count:
                count[n] += 1
                if count[n] > m:
                    m = count[n]
                    res = n
        return res
                    
            
