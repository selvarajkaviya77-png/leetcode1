
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""
        
        target_counts = Counter(t)
        required = len(target_counts)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        
        while r < len(s):
            char = s[r]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            while l <= r and formed == required:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                
                window_counts[char] -= 1
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1
                l += 1    
            r += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]