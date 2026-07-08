class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        reps = defaultdict(int)
        cur = 0

        l = 0

        maxf = 0

        for r in range(len(s)):

            reps[s[r]] += 1
            maxf = max(maxf,max(reps.values()))

            while ((r - l + 1) - maxf) > k:
                reps[s[l]] -= 1
                l += 1

            cur = max(cur, r - l + 1)

        return cur
