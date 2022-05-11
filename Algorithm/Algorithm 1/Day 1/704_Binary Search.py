class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            curr = nums[mid]
            if target == curr:
                return mid
            elif target > curr:
                left = mid+1
            else:
                right = mid-1
        return -1
        
