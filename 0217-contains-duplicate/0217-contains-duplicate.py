class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 1. 정렬 후 앞 인덱스와 뒤 인덱스 요소가 하나라도 동일한게 나올 시 즉시 true 출력
        nums.sort() # 리스트 정렬
        for i in range(len(nums)-1): # 마지막 인덱스는 다음 인덱스가 없으므로 1을 뺌
            if nums[i] == nums[i+1]:
                return True
        return False
        # 결과: 

        # # 2 set함수를 이용하여 요소 압축 후 nums 리스트와 비교
        # nums.sort() # 리스트 정렬
        # set_nums = set(nums) # set 함수 사용
        # list_nums = list(set_nums) # set 클래스를 리스트로 변환하고 정렬
        # list_nums.sort()
        # print(list_nums, nums)
        # if list_nums != nums:
        #     return True
        # else:
        #     return False
        # # 결과: runtime 91ms memory 33.78MB


        