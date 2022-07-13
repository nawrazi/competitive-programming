# https://leetcode.com/problems/video-stitching/

class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key = lambda x : x[1])
        start = time
        used = [[time, time]]
        
        for cur_start, cur_end in reversed(clips):
            if cur_end >= start and cur_start < start:
                if used and cur_end >= used[-1][1]:
                    used.pop()
                    
                diff = used[-1][0] if used else min(time, cur_end)
                used.append([cur_start, diff])
                start = cur_start
        
        return len(used) if used and used[-1][0] == 0 else -1
