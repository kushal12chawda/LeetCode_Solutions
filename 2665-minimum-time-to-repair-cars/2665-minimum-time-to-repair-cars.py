class Solution(object):
    def repairCars(self, ranks, cars):
        def repair_time(time):
            repaired = 0
            for r in ranks:
                repaired += int((time // r) ** 0.5) 
            return repaired >= cars

        left, right = 1, min(ranks) * (cars ** 2)
        
        while left < right:
            mid = (left + right) // 2
            if repair_time(mid):
                right = mid  
            else:
                left = mid + 1 

        return left