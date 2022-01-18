class BrowserHistory:

    def __init__(self, homepage: str):
      self.pages = [homepage]
      self.indices = [0]
      self.position = 0
      
    def visit(self, url: str) -> None:
      self.pages.append(url)
      self.position = len(self.indices)
      self.indices.append(len(self.indices))

    def back(self, steps: int) -> str:
      if self.position - steps < 0:
        self.position = 0
      else:
        self.position -= steps
      return self.pages[self.position]

    def forward(self, steps: int) -> str:
      if self.position + steps >= len(self.indices):
        self.position = len(self.indices)-1
      else:
        self.position += steps
      return self.pages[self.position]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)