#Insert the newInterval into the sorted intervals
#merge intervals as needed to avoid overlapping ones
def insert(intervals,newInterval):
  #find the spot where it can be inserted
  #collect all the intervals it overlaps with
  overlap_start, overlap_end = 0,0
  found = False
  for i in range(len(intervals)):
    if not found:
      if intervals[i][0] > newInterval[0]:
        overlap_start = i
        found = True
      elif intervals[i][1] > newInterval[0]:
        overlap_start = i + 0.5
        found = True
      
    else:
      if intervals[i][0] > newInterval[1]:
        overlap_end = i
        break
      elif intervals[i][1] > newInterval[1]:
        overlap_end = i + 0.5
        break

  return overlap_start, overlap_end


intervals = [[1,3],[6,9]]
newInterval = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals,newInterval))
