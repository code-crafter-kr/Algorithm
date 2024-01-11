class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp = ""
        result = 0
        for i in range (len(s)):
            print(temp)
            if s[i] not in temp:
                temp += s[i]
                result = max(len(temp), result)
            else:
                idx = temp.index(s[i]) + 1
                temp = temp[idx:]
                temp += s[i]
        print(temp)
        return result


if __name__ == "__main__":
    s = "dvdf"
    print (Solution().lengthOfLongestSubstring(s))