class Solution:
    def reverse(self, x: int) -> int:
        
        res = 0
        flag = 0
        
        if x<0: 
            x = x * (-1)
            flag = 1

        
        for i in range(len(str(x))):
            res = res*10 + x % 10
            x = x//10
            
        if flag == 1: res = res * (-1)
            
        if res > 2**31 or res < -2**31 - 1: return 0
        
        return res
