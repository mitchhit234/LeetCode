from os import CLD_CONTINUED


class Solution:

  def videoStitching(self, clips, time) -> int:

    clips = sorted(clips,key=lambda x: (x[0],x[1]))
    ret = self.rec(clips,0,time)

    if len(ret) > 0:
      if ret[0][0] == 0 and ret[-1][1] >= time:
        for i in range(len(ret)-1):
          if ret[i][1] < ret[i+1][0]:
            return -1
        return len(ret)
    return -1


  def rec(self,clips,l_time,u_time):
    mx, index = 0, -1
    if l_time < u_time:
      for i in range(len(clips)):
        to_gain = clips[i][1]-clips[i][0]
        to_gain -= max(clips[i][1]-u_time,0)
        to_gain -= max(l_time-clips[i][0],0)
        if to_gain > mx:
          mx = to_gain
          index = i

    if index < 0:
      return []

    val = clips[index]
    return self.rec(clips[:index],l_time,val[0]) + [val] + self.rec(clips[index+1:],val[1],u_time)




  




obj = Solution()
clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
#clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
clips = [[7,9],[5,9],[10,10],[5,10],[8,10],[2,6],[7,9],[7,10],[4,5]]
time = 2
print(obj.videoStitching(clips,time))