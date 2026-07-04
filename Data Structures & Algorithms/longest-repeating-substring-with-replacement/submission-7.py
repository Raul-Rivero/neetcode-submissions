class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        cur = 0
        reps = defaultdict(int)

        l = 0

        for r in range(len(s)):
            reps[s[r]] += 1

            while (r - l + 1) - max(reps.values()) > k:
                reps[s[l]] -= 1
                l += 1

            cur = max(cur, r - l + 1)

        return cur