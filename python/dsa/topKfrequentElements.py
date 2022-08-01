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
