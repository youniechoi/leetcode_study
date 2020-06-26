class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #nums_c = nums # 주소값 복사 같이 변경된다. 
        nums_c = nums[:]
        
        for i in range(0,len(nums)):
            
            remain = target-nums[i]
            nums_c.remove(nums[i])
        #    print(nums, nums_c)

            if remain in nums_c:
                result = [nums.index(nums[i]), nums_c.index(remain)+1]
                
            else:
                nums_c.insert(nums.index(nums[i]), nums[i])
                
        return result
