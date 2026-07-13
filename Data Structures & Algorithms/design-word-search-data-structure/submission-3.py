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

        def dfs(idx, node) -> bool:
            if node is None: return False
            if len(word) == idx: return node.endOfWord
    
            char = word[idx]
    
            if char != ".":
                if char in node.children:
                    return dfs(idx+1, node.children[char])
                else: return False
            else:
                return any(dfs(idx+1, child) for child in node.children.values())

        
        return dfs(0, self.root)