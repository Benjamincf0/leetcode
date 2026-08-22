class Solution:
    class TrieNode:
        def __init__(self):
            self.word = None 
            self.children = dict()

    def addWord(self, trie_root: TrieNode, word: str):
        current = trie_root

        for c in word:
            if c not in current.children:
                current.children[c] = self.TrieNode()
            current = current.children[c]

        current.word = word

    def buildTrie(self, words: list[str]) -> TrieNode:
        root = self.TrieNode()
        for word in words:
            self.addWord(root, word)

        return root

    def findWord(self, trie_root: TrieNode, word: str):
        current = trie_root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]

        return True, current.word

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Omydays finally wth was this shit
        root = self.buildTrie(words)
        visited = set()
        res = set()
        
        def dfs(node, i, j):
            if (not (0 <= i < len(board))) or (not (0 <= j < len(board[0]))) or (i, j) in visited: return

            letter = board[i][j]
            if letter not in node.children:
                return

            new_node = node.children[letter]
            if new_node.word:
                res.add(new_node.word)

            visited.add((i, j))
            dfs(new_node, i-1, j)
            dfs(new_node, i+1, j)
            dfs(new_node, i, j-1)
            dfs(new_node, i, j+1)
            visited.remove((i, j))


        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(root, i, j)

        return list(res)