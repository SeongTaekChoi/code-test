class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0) # 첫번째 인덱스이거나 이전 인덱스가 0일 때
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0) # 마지막 인덱스 이거나 이후 인덱스가 0일 때

                if left_empty and right_empty: # 양 쪽 다 비면 꽃 심기(첫, 마지막 인덱스는 각각 이전 이후 인덱스에 0이 있다고 생각)
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True

        return count >= n