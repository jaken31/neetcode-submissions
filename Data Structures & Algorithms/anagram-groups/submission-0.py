class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs: 
            frq = [0] * 26
            for j in i:
                frq[ord(j) - ord('a')] += 1
            
            ans[tuple(frq)].append(i)
        
        return list(ans.values())
        