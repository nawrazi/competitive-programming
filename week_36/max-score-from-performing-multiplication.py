# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

class Solution {
public:
    vector<vector<int>> dp;
    
    int getSum(vector<int>& nums, vector<int>& mult, int m, int l) {
        int r = nums.size() - (m - l) - 1;
        
        if (m == mult.size() - 1) {
            return max(mult[m] * nums[l], mult[m] * nums[r]);
        }
        
        if (dp[m][l] == INT_MIN) {
            dp[m][l] = max(
                (mult[m] * nums[l]) + getSum(nums, mult, m + 1, l + 1),
                (mult[m] * nums[r]) + getSum(nums, mult, m + 1, l)
            );
        }
        
        return dp[m][l];
    }
    
    int maximumScore(vector<int>& nums, vector<int>& multipliers) {
        int m = multipliers.size();
        dp.resize(m + 1, vector<int>(m + 1, INT_MIN));
        return getSum(nums, multipliers, 0, 0);
    }
};
