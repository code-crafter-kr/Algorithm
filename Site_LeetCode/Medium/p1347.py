class Solution(object):
    def minSteps(self, s, t):
        lst = [0] * 26
        result = 0
        for i in range (len(s)):
            lst[ord(s[i])-97] += 1
            lst[ord(t[i])-97] -= 1
            
        for x in lst:
            if x > 0:
                result += x

        return result

        