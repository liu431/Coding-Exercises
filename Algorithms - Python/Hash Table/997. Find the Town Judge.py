class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and len(trust) == 0:
            return 1
        trusted_dic = {}
        people = set()
        for a, b in trust:
            people.add(a)
            trusted = b
            if trusted not in trusted_dic:
                trusted_dic[trusted] = 1
            else:
                trusted_dic[trusted] += 1

        for k, v in trusted_dic.items():
            # The town judge trusts nobody.
            # Everybody (except for the town judge) trusts the town judge.
            if k not in people and v == n - 1:
                return k
        return -1
