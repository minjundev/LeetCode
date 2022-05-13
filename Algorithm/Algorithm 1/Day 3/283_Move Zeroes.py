class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = nums.count(0)
        for _ in range(cnt):
            nums.remove(0)
            nums.append(0)
