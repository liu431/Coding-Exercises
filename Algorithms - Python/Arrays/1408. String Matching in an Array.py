class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for ind, word in enumerate(words):
            compare = sum([word in i for i in words])
            if compare >= 2:
                res.append(word)
        return res
