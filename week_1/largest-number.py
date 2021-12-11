# https://leetcode.com/problems/largest-number/submissions/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key = lambda num: num[0], reverse=True)

        similars=[[]]

        cur_digit=nums[0][0]
        while nums:
            if nums[0][0]==cur_digit:
                similars[-1].append(nums.pop(0))
            else:
                cur_digit=nums[0][0]
                similars.append([nums.pop(0)])

        for sim_nums in similars:
            n = len(sim_nums)
            if n==1:
                continue

            for i in range(n):
                for j in range(i+1,n):
                    if int(sim_nums[j]+sim_nums[i]) > int(sim_nums[i]+sim_nums[j]):
                        sim_nums[i],sim_nums[j] = sim_nums[j],sim_nums[i]

        result = ''.join([x for l in similars for x in l])

        return result if int(result)!=0 else "0"
