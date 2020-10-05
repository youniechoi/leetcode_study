class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        for i, n in enumerate(nums):
            #print(i,n)
            if(n in nums):
                nums.remove(n)
             #   print(nums)
                if(n in nums):
                    nums.insert(i, n)                    
                else:
                    return n
