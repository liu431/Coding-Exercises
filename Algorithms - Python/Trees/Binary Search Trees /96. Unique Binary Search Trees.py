class Solution:
    def numTrees(self, n: int) -> int:
        # Given a sequence 1 ... n, we pick a number i out of the sequence as the root, then the number of unique BST with the specified root defined as F(i,n)F(i, n)F(i,n), is the cartesian product of the number of BST for its left and right subtrees
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        
        return G[n]
