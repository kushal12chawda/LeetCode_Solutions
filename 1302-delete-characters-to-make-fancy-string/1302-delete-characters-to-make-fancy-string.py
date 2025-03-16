class Solution(object):
    def makeFancyString(self, s):
        res = []
        for c in s:
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            res.append(c)
        ans = ""
        for i in res:
            ans = ans+i
        return ans
        