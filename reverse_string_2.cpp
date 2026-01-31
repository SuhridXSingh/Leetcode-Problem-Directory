class Solution {
public:
    void reverseString(vector<char>& s) {

        auto strt = s.begin();
        auto end = s.end()-1;

        while (strt<end){
            char temp = *strt;
            *strt = *end;
            *end = temp;
            strt++;
            end--;
        }
    }
};
