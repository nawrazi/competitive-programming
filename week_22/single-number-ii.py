# https://leetcode.com/problems/single-number-ii/

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int result = 0;
        int mask = 1;
        
        for (int i = 0; i < 32; i++) {
            int count = 0;
            for (int j = 0; j < nums.size(); j++) {
                if (nums[j] & mask) {
                    count++;
                }
            }
            if (count % 3 == 1)
                result |= mask;
            if (i < 31)
                mask <<= 1;
        }
        
        return result;
    }
};
