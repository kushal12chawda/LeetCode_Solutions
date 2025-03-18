class Solution(object):
    def largestNumber(self, nums):
        def compare(x, y):
            if x + y < y + x:
                return 1
            else:
                return -1

        nums = list(map(str, nums))
        nums.sort(key=cmp_to_key(compare))
        result = ''.join(nums)

        if result[0] == '0':
            return '0'
        else:
            return result