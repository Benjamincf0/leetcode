from functools import cache
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str):
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.end_of_word = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict: trie.add_word(word)

        @cache
        def dfs(i, node):
            if i == len(s) or s[i] not in node.children: return False

            child_node = node.children[s[i]]

            if child_node.end_of_word:
                if i == len(s)-1: return True
                return dfs(i+1, trie.root) or dfs(i+1, child_node)
            else:
                return dfs(i+1, child_node)

        return dfs(0, trie.root)