class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        for i in range(len(s)):
            freqs[s[i]] = freqs.get(s[i], 0) + 1
        
        for i in range(len(t)):
            freqt[t[i]] = freqt.get(t[i], 0) + 1

        return freqs == freqt