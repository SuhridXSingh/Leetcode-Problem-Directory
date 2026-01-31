class Solution {
public:
    void reverseString(vector<char>& s) {

        auto strt = s.begin();
        auto end = s.end()-1;

        for (int i=0; ; i++){
            if (strt>=end){
                break;
            }
            char temp = *strt;
            *strt = *end;
            *end = temp;
            strt++;
            end--;
        }
    }
};
