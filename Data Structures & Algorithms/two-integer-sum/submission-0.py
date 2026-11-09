class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for ind,i in enumerate(nums):
            n=target-i
            if n in map:
                return [map[n], ind]
            map[i]=ind