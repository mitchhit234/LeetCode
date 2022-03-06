#include <iostream>
#include <vector>

class Solution {
public:
    //0 = 0, 1 = 1, 2 = 1
    //T_n+3 = T_n + T_n+1 + T_n+2
    int tribonacci(int n) {
      std::vector<int> help{0,1,1};
      for (int i = 3; i < n+1; i++) {
        help.push_back(help[i-3] + help[i-2] + help[i-1]);
      }
      return help[n];
    }
};


int main(){
  Solution obj;
  int inp = 37;
  int ret = obj.tribonacci(inp);
  std::cout << ret << std::endl;
  return 0;
}