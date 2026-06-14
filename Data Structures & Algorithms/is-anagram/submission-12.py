class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap_s = defaultdict(int)
        hashmap_t = defaultdict(int)

        for i in s:
            hashmap_s[i] += 1

        for i in t:
            hashmap_t[i] += 1

        return hashmap_s == hashmap_t