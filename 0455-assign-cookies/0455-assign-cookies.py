class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # 욕심이 큰 아이부터 확인
        g = sorted(g, reverse=True)
        s = sorted(s, reverse=True)

        count = 0
        cookie = 0

        for child in g:
            # 남은 쿠키가 없으면 종료
            if cookie >= len(s):
                break

            # 현재 가장 큰 쿠키가 아이를 만족시키는 경우
            if s[cookie] >= child:
                count += 1
                cookie += 1

        return count