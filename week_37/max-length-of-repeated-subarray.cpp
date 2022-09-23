// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution {
public:
    vector<vector<int>> cache;
    
    int getLength(vector<int>& nums1, vector<int>& nums2, int idx1, int idx2) {
        if (idx1 >= nums1.size() || idx2 >= nums2.size() || nums1[idx1] != nums2[idx2])
            return 0;
        
        if (cache[idx1][idx2] == -1)
            cache[idx1][idx2] = 1 + getLength(nums1, nums2, idx1 + 1, idx2 + 1);
        
        return cache[idx1][idx2];
    }
    
    int findLength(vector<int>& nums1, vector<int>& nums2) {
        cache.resize(nums1.size(), vector<int>(nums2.size(), -1));
        
        int ans = 0, i = 0, j = 0;
        
        while (i < nums1.size()) {
            j = 0;
            while (j < nums2.size()) {
                ans = max(ans, getLength(nums1, nums2, i, j));
                j++;
            }
            i++;
        }
        
        return ans;
    }
};
