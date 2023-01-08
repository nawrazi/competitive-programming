# https://leetcode.com/problems/maximize-the-minimum-powered-city/description/

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        window = sum(stations[:r + 1])
        left, center, right = -r, 0, r
        power = [0 for _ in stations]
        
        while right < len(stations) + r:
            power[center] += window
            
            if left >= 0:
                window -= stations[left]
                
            left += 1
            center += 1
            right += 1
            
            if right < len(stations):
                window += stations[right]
                
        def chooseMin(value):
            low_power = []
            
            for idx, city in enumerate(power):
                if city < value:
                    low_power.append((idx, value - city))
                    
            cache = []
            stations = k
            last_pos, last_pow = -1, 0
            for city, need in low_power:
                if city > last_pos:
                    stations -= need
                    last_pos = city + 2*r
                    last_pow = need
                elif city <= last_pos and need > last_pow:
                    stations -= need - last_pow
                    last_pow = need
                cache.append(stations)
                
            if stations >= 0:
                return True
            
            stations = k
            last_pos, last_pow = len(power), 0
            for i, (city, need) in enumerate(reversed(low_power)):
                if city < last_pos:
                    stations -= need
                    last_pos = city - 2*r
                    last_pow = need
                elif city >= last_pos and need > last_pow:
                    stations -= need - last_pow
                    last_pow = need
                if k % 2 == 0 and cache[len(low_power) - i - 1] == 0 and stations >= 0 and r:
                    return True
                
            return stations >= 0
        
        left, right = 0, k + max(power)
        best = min(power)
        
        while left <= right:
            mid = (left + right) // 2
            if chooseMin(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1
                
        return best
    
