class Solution(object):
    def longestNiceSubarray(self, nums):
        left = 0
        used_bits = 0
        max_len = 0

        for right in range(len(nums)):
            while (used_bits & nums[right]) != 0:
                used_bits ^= nums[left]
                left += 1

            used_bits |= nums[right]
            max_len = max(max_len, right - left + 1)

        return max_len
        