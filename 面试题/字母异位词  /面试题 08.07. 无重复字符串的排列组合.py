class Solution:
    def permutation(self, S: str) -> List[str]:
        if not S:
            return []
        st = list(sorted(S))
        res = []

        def dfs(st, tmp):
            if not st:
                res.append(''.join(tmp))
            for i in range(len(st)):
                dfs(st[:i] + st[i + 1:], tmp + [st[i]])

        dfs(st, [])
        return res


