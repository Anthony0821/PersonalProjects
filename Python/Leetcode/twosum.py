'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            
        for x in range(len(nums)):
            for y in range(x + 1,len(nums)):
                if nums[x] + nums[y] == target:
                    return (x, y)
                    
    THE ABOVE CODE WILL WORK IT IS JUST NOT EFFICIENT BECAUSE IT USES A NESTED LOOP
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twonums = {}
        
        
        return twonums