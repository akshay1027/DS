from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, a: List[int], k: int) -> List[int]:
        hash = {}

        for i in range(len(a)):
            if a[i] in hash:
                hash[a[i]] += 1
            else:
                hash[a[i]] = 1

        # sorted returns a list
        arr = sorted(hash, key=hash.get, reverse=True)
        return arr[:k]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        print(frq)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k:
                return res[:k]

        return res[:k]
