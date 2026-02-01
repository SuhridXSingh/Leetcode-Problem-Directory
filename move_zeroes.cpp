class Solution {
public:
    void moveZeroes(vector<int>& nums) {

        auto ptr = nums.begin();
        // auto end = nums.end()-1;
        int count = 0;

        while (ptr != nums.end()) {
            
            if (*ptr == 0) {
                count++;
                ptr = nums.erase(ptr); 
            } 

            else {
                ptr++;
            }
        }

        // sort(nums.begin(),nums.end());

        for(int i=0; i<count; i++){
            nums.push_back(0);
        }
        
    }
};
