class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        trie = self.trie
        for i in word:
            trie[i] = trie.get(i, {})
            trie = trie[i]

        trie["__is_word__"] = True

    def search(self, word: str) -> bool:
        return self.search_recursive(word, 0, self.trie)

    def search_recursive(self, word, i, trie):
        if i == len(word):
            return trie.get("__is_word__", False)

        if word[i] == ".":
            keys = trie.keys() - {"__is_word__"}

        elif word[i] in trie:
            keys = [word[i]]

        else:
            return False

        for key in keys:
            if self.search_recursive(word, i + 1, trie[key]):
                return True

        return False
