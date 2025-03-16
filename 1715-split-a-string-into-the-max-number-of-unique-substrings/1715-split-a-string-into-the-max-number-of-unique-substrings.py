class Solution(object):
    def maxUniqueSplit(self, s):
        def helper(idx, seen):
            if idx == len(s):
                return len(seen)
            
            max_count = 0
            for end in range(idx + 1, len(s) + 1):
                part = s[idx:end]
                if part not in seen:
                    seen.add(part)
                    max_count = max(max_count, helper(end, seen))
                    seen.remove(part)
            
            return max_count

        return helper(0, set())
            