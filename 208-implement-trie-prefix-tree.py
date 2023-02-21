class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for i in word:
            trie[i] = trie.get(i, {})
            trie = trie[i]

        trie["__is_word__"] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for i in word:
            if i not in trie:
                return False

            trie = trie[i]

        return trie.get("__is_word__", False)

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for i in prefix:
            if i not in trie:
                return False

            trie = trie[i]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
