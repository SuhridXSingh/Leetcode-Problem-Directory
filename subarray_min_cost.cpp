class Solution {
public:
    int minimumCost(vector<int>& nums) {

        int n = nums[0];

        nums.erase(nums.begin());

        sort(nums.begin(),nums.end());

        int minCost = n + nums[0] + nums[1];

        return minCost;
        
    }
};
