import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom  # or / in Python 2

class Solution:
    def climbStairs(self, n: int) -> int:
        
        num_two = n//2 #2의 최대 갯수
        result = 0
        
        for i in range(1,num_two+1):  #1에서 2의 최대 갯수 까지 가능한 순열 조합
            
            result = result + ncr(n-i,i)
            
            print(result)
                        
        
        return round(result)+1 # 1인 경우의 수
        