class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            temp = str(sorted(s))
            # keys can be strings, bcz they are immutable.
            if temp in hashmap:
                hashmap[temp].append(s)
            else:
                hashmap[temp] = [s]

        return hashmap.values()
