import sys
sys.stdin = open('input.txt', 'r')

class Solution(object):
    def romanToInt(self, s):
        dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000, "IV" : 4, "IX" : 9, "XL" : 40, "XC" : 90, "CD" : 400, "CM" : 900}
        ans = 0
        valid = False
        s += "I"
        for i in range (0, len(s)-1):
            if valid == True:
                valid = False
                continue
            if (s[i] == "I" and (s[i+1] == "V" or s[i+1] == "X")) or (s[i] == "X" and (s[i+1] == "L" or s[i+1] == "C")) or (s[i] == "C" and (s[i+1] == "D" or s[i+1] == "M")):
                ans += dic[s[i] + s[i+1]]
                valid = True
            else:
                ans += dic[s[i]]
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = input()
    print(sol.romanToInt(s))