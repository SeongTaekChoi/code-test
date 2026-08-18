class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # 상자 하나당 유닛 수를 기준으로 내림차순 정렬
        boxTypes.sort(key=lambda box: box[1], reverse=True)

        total_units = 0

        for number_of_boxes, units_per_box in boxTypes:
            # 현재 종류에서 실제로 실을 상자 개수
            boxes_to_load = min(number_of_boxes, truckSize)

            total_units += boxes_to_load * units_per_box
            truckSize -= boxes_to_load

            # 트럭이 가득 찬 경우 종료
            if truckSize == 0:
                break

        return total_units