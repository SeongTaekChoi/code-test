class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 20달러를 받으면 어짜피 거스름돈으로 못줌. 5달러 리스트와 10 달러 리스트를 만들어 넣고 빼가면서 계산
        dollar5 = []
        dollar10 = []
        for i in range(len(bills)):
            if bills[i] == 5:
                dollar5.append(5)
            elif bills[i] == 10:
                dollar10.append(10)
                if len(dollar5) >= 1:
                    dollar5.pop()
                else:
                    return False
            else:
                if len(dollar10) >= 1 and len(dollar5) >= 1:
                    dollar10.pop()
                    dollar5.pop()
                elif len(dollar5) >= 3:
                    dollar5.pop()
                    dollar5.pop()
                    dollar5.pop()
                else:
                    return False
        return True
