class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canFinish(mid):
            load = 0
            req_day = 1
            for weight in weights:
                if load + weight <= mid:
                    load += weight
                else:
                    req_day += 1
                    load = weight
            return req_day <= days
            
        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high - low) // 2

            if canFinish(mid):
                high = mid
            else:
                low = mid + 1

        return low