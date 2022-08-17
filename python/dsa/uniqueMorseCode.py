class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        arr = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
               "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        res = set()
        for word in words:
            str = ""
            for char in word:
                str += (arr[ord(char) - 97])
            res.add(str)
        return len(res)
