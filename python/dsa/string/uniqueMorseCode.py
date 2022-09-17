class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
               "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        res = set()
        # res = {}
        for word in words:
            str = ""
            for char in word:
                str += (arr[ord(char) - 97])
            res.add(str)
            #res[str] = res.get(str, 0) + 1
        return len(res)
