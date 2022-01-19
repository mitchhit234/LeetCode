import math
#Minimize the max amount of products given to any one store
#Each store can only be given at most one type of product,
#but they can be given any number of this product
def minimizedMaximum(n,Q):
    beg, end = 0, max(Q)
    
    while beg + 1 < end:
        mid = (beg + end)//2
        if sum(math.ceil(i/mid) for i in Q) <= n:
            end = mid
        else:
            beg = mid
    
    return end

  







n = 6
quantities = [6,11]
print(minimizedMaximum(n,quantities))