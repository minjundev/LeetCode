class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        answer = ''
        for i in range(len(s)):
            t = list(s[i])
            left = 0
            right = len(t)-1
            while left <= right:
                saved = t[right]
                t[right] = t[left]
                t[left] = saved
                left += 1
                right -= 1
            answer += ''.join(t)+' '
        return answer[:-1]
