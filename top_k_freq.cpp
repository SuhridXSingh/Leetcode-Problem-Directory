class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {

        unordered_map<int,int>freq;

        for(int n : nums){
            freq[n]++;
        }

        vector<int>ans;

        vector<pair<int,int>>cpy(freq.begin(),freq.end());
        sort(cpy.begin(),cpy.end(),[](pair<int,int>& a, pair<int,int>& b){
            return a.second > b.second;
        });

        for(int i=0; i<k; i++){
            ans.push_back(cpy[i].first);
        }

        // sort(ans.begin(),ans.end());
        return ans;
    }
};
