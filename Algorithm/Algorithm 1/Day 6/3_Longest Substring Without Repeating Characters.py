class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        used = dict()
        
        for right, c in enumerate(s):
            if c in used and left <= used[c]:
                left = used[c] + 1
            else:
                answer = max(answer, right-left+1)
            used[c] = right
        return answer
