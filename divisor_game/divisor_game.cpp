#include <iostream>

using namespace std;

class Solution {
public:
    bool divisorGame(int n) {
        if (n % 2 == 0)
          return true;
        return false;
    }
};


int main(){
  Solution obj;
  int n = 2;
  bool result = obj.divisorGame(n);
  cout << result << endl;

  return 0;
}