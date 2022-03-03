# https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def searchConnections(city_row):
            connected.add(city_row)

            for city_col in range(len(isConnected)):
                if isConnected[city_row][city_col] and city_col not in connected:
                    searchConnections(city_col)

        connected = set()
        provinces = 0

        for city_row in range(len(isConnected)):
            if city_row not in connected:
                provinces += 1
                searchConnections(city_row)

        return provinces
