class Solution(object):
    def isPalindrome(self, s):
        s1 = ""
        s2 = ""
        for i in s:
            if i.isalnum():
                if i.isalpha():
                    s1 = s1 + i.lower()
                if i.isnumeric():
                    s1 = s1 + str(i)
        s2 = s1[::-1]
        print s1
        print s2
        if s1 == s2:
            return True
        else:
            return False
        