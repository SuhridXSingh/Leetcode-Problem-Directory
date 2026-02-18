class Solution {
public:
    int longestConsecutive(vector<int>& nums) {

        if (nums.empty()) {
            return 0;
        }

        unordered_set<int> s(nums.begin(), nums.end());
        int longestStreak = 0;

        for (int n : s) {

            if (!s.count(n - 1)) {

                int currentNum = n;
                int currentStreak = 1;

                while (s.count(currentNum + 1)) {
                    currentNum++;
                    currentStreak++;
                }

                longestStreak = max(longestStreak, currentStreak);
            }
        }

        return longestStreak;
    }
};
