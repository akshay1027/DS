# https://leetcode.com/problems/implement-trie-prefix-tree/k
# https://leetcode.com/problems/implement-trie-prefix-tree/discuss/362916/Simple-Python-solution-(beats-99-runtime-95-memory)
# we use trie to build search feature and autocomplete.

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

class Trie(object):

    # uisng "-" to indicate end of word

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t["-"] = True

    # {'a': {'p': {'p': {'l': {'e': {'-': True}}}}}}
    # {'a': {'p': {'p': {'l': {'e': {'-': True}}, '-': True}}}}

    def search(self, word):
        t = self.trie
        print(t)
        for c in word:
            if c not in t:
                return False
            t = t[c]
        return "-" in t

    def startsWith(self, prefix):
        t = self.trie
        for c in prefix:
            if c not in t:
                return False
            t = t[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    {"a": {"p": {"p": {"l": {"e": {True}}}}}}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()  # going on root down
            curr = curr.children[c]  # same level
        curr.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in te trie.
        """
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
