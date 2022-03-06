#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    bool isBoomerang(vector<vector<int>>& points) {
      //Sort our points left to right
      // sort(points.begin(),
      //   points.end(), [] (vector<int> &a, vector<int> &b){
      //     bool result;
      //     if (a[0] < b[0])
      //       return true;
      //     else if (a[0] > b[0])
      //       return false;
      //     else
      //       return a[1] < b[1];
      //   });

      // //Confirm that our points are distinct
      // for (int i = 0; i < points.size()-1; i++) {
      //   if (points[i] == points[i+1]) return false;
      // }

      // //See if the middle point falls in a straight line
      // //between the first and last point
      // vector<int> e1 = points[0];
      // vector<int> e2 = points[points.size()-1];
      // vector<int> temp = {e2[0]-e1[0],e2[1]-e1[1]};

      // if (temp == points[1]) return false;
      // return true;

      int slp = slope(points[0],points[1]);

      for (int i = 0; i < points.size()-1; i++){
        for (int j = i+1; j < points.size(); j++){
          if (slp != slope(points[i],points[j]))
            return false;
        }
      }
      return true;
    }

    int slope(vector<int> a, vector<int> b){
      int slp = (b[1]-a[1]) / (b[0]-a[0]);
      return slp;
    };
};


int main(){
  Solution obj;
  vector<vector<int>> points = {{1,2},{2,1},{2,2}};
  bool ret = obj.isBoomerang(points);
  cout << ret << endl;
  return 0;
}