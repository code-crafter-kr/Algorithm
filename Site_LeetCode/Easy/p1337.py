class Solution(object):
    def kWeakestRows(self, mat, k):
        lst = []
        ans = []
        idx = 0
        count = 0
        for i in mat:
            lst.append(i.count(1))

        for i in range (0, 101):
            try:
                a = lst.index(i)
                ans.append(a)
                lst[a] = -1
                count += 1
                if count == k:
                    break
            except:
                continue

        return ans