class PrefixTree:
    class Node:
        def __init__(self):
            self.children: dict[str, Node] = dict()
            self.final: bool = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = self.Node()
            node = node.children[char]
        node.final = True
        
    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            node = node.children.get(char, None)
            if node is None:
                return False
        return node.final

        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            node = node.children.get(char, None)
            if node is None:
                return False
        return True
        