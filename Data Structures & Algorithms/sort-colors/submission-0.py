class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        bucket = [0,0,0]
        for i in (nums):
            bucket[i] += 1

        j = 0
        for i in range(len(bucket)):
            while bucket[i] != 0:
                nums[j] = i
                bucket[i] -= 1
                j += 1