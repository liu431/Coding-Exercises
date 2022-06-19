class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        out = []
        for i in range(1, len(searchWord)+1):
            typed = searchWord[:i]
            matched = sorted([p for p in products if p[:i]==typed])[:3]
            out.append(matched)
        return out
