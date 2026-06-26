class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]
        
        count = Counter(nums)

        for num, freq in count.items():
            buckets[freq].append(num)

        ans = []
        ct = 0
        for i in reversed(range(len(buckets))):
            for num in buckets[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans