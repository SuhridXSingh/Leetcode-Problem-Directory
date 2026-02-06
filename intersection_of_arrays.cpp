class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {

        unordered_set<int> a(nums1.begin(), nums1.end());
        vector<int> ans;

        for (int i = 0; i < nums2.size(); i++) {
            int val = nums2[i];
            if (a.find(val) != a.end()) {
                ans.push_back(val);
                a.erase(val);
            }
        }

        return ans;
    }
};
