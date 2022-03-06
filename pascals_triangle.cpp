#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

class Solution {
public:
    //Given an integer rowIndex return the 
    //rowIndex'th tow of Pascal's Triangle
    std::vector<int> getRow(int rowIndex) {
        std::vector<int> current (1,1);
        for (int i = 0; i < rowIndex; i++) {
          std::vector<int> nw (1,1);
          for (int j=0; j < i; j++) {
            int temp = current[j] + current[j+1];
            nw.push_back(temp);
          }
          current = nw;
          current.push_back(1);
        }
        return current;
    }
};



int main()
{
  int rowIndex;
  std::cin >> rowIndex;
  Solution m;
  std::vector<int> ret = m.getRow(rowIndex);
  
  std::copy(ret.begin(),ret.end(),std::ostream_iterator<int>(std::cout, " "));

  return 0;
}