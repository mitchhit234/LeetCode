class RecentCounter:

    def __init__(self):
      self.counter = []
        
    def ping(self, t: int) -> int:
      self.counter += [t]
      index = len(self.counter)-1
      while index >= 0 and self.counter[index] >= t-3000:
        index -= 1
      return self.counter[index:]
        




