class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # change in place
        # create shallow copy
        for i in nums[:]:
            if i == val:
                nums.remove(i)
        return len(nums)