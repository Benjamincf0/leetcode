class WordDictionary:
    class TrieNode:
        def __init__(self):
            self.children: dict[str, TrieNode] = {}
            self.endOfWord: bool = False

    def __init__(self):
        self.root = self.TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            new = curr.children.get(c, None)
            if new is None:
                new = curr.children[c] = self.TrieNode()
            curr = new
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(word, self.root)

    def dfs(self, word, node) -> bool:
        if node is None: return False
        if len(word) == 0: return node.endOfWord

        char = word[0]

        if char != ".":
            if char in node.children:
                return self.dfs(word[1:], node.children[char])
            else: return False
        else:
            return any([self.dfs(word[1:], child) for child in node.children.values()])