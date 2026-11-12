class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s= set(nums)
        large=0
        for i in s:
            if i -1 not in s:
                nextnum= i+1
                length=1
                while nextnum in s:
                    length+=1
                    nextnum+=1
                large=max(large,length)
        return large

