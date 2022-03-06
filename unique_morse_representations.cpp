#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <set>

using namespace std;


class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        vector<string> morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        string letters = "abcdefghijklmnopqrstuvwxyz";

        unordered_map<char,string> L;
        for (int i = 0; i < letters.size(); i++) {
            L[letters[i]] = morse[i];
        }

        set<string> conversions;

        for (int i=0; i < words.size(); i++){
            string tmp = "";
            for (int j=0; j < words[i].size(); j++){
                tmp += L[words[i][j]];
            }
            //cout << tmp << endl;
            conversions.insert(tmp);
        }
        return conversions.size();
        
    }
};


int main(){
    Solution obj;
    vector<string> inp = {"gin", "zen", "gig", "msg"};
    int ret = obj.uniqueMorseRepresentations(inp);
    cout << ret << endl;
    return 0;
}