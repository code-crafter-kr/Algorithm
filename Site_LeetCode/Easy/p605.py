class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        count = 0
        flowerbed = [0] + flowerbed + [0] #the start point and end point will be regard as [0]
        sw = 0

        for i in range (len(flowerbed)):
            if flowerbed[i] == 0:
                sw += 1
                if sw % 2 == 1 and sw != 1:
                    count += 1  
            else:
                sw = 0
            
        if count >= n:
            return True
        else:
            return False
        
if __name__ == "__main__":
    canPlaceFlowers_test = Solution()
    lst = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    n = 3
    print(canPlaceFlowers_test.canPlaceFlowers(lst, n))