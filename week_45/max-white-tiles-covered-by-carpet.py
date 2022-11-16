# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        edges = []
        prefix = []
        current = 0
        
        for start, end in tiles:
            edges.append(start)
            edges.append(end)
            
            current += 1
            prefix.append(current)
            current += end - start
            prefix.append(current)
            
        def search(target):
            start, end = 0, len(edges) - 1
            best = 0
            while start <= end:
                mid = (start + end) // 2
                if edges[mid] < target:
                    best = mid
                    start = mid + 1
                else:
                    end = mid - 1
                    
            return best
        
        max_cover = 0
        for s, (start, _) in enumerate(tiles):
            end = start + carpetLen
            e = search(end)
            cover = prefix[e] - prefix[2 * s]
            if e % 2 == 0:  # ending on white tiles
                cover += end - edges[e]
            else:   # ending on non-white tiles
                cover += 1
            max_cover = max(max_cover, cover)
            
        return max_cover
    
