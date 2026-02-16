class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {

        unordered_map<string,vector<string>>um;

        for(string s : strs){
            string key = s;
            sort(key.begin(),key.end());
            um[key].push_back(s);
        }

        vector<vector<string>>ans;

        // auto itr = um.begin();
        // auto end = um.end();

        // while(itr!=end){
        //     ans.push_back(itr->second);
        //     itr++;
        // }

        for(auto pair : um){
            ans.push_back(pair.second);
        }

        return ans;

    }
};
