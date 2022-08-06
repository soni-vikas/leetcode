from typing import List


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.so_far = ""
        self.trie = {}
        self.sentences = {}
        for i in range(len(sentences)):
            self.sentences[sentences[i]] = times[i]
            self.trie_insert(sentences[i], times[i], self.trie)

    def trie_insert(self, word, count, trie):
        for c in word:
            trie[c] = trie.get(c, {"__items__": [], "__child__": {}})

            found = False
            # Update count if word is already present in trie.
            for i, v in enumerate(trie[c]["__items__"]):
                if v[1] == word:
                    trie[c]["__items__"][i] = (-count, word)
                    found = True

            # Insert word if not present in trie
            if not found:
                trie[c]["__items__"].append((-count, word))

            trie[c]["__items__"] = sorted(trie[c]["__items__"])[:3]
            trie = trie[c]["__child__"]

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.sentences[self.so_far] = self.sentences.get(self.so_far, 0) + 1
            self.trie_insert(self.so_far, self.sentences[self.so_far], self.trie)
            self.so_far = ""
            return []

        self.so_far = self.so_far + c
        trie = self.trie
        items = []
        for c in self.so_far:
            if c not in trie:
                return []

            items = trie[c]["__items__"]
            trie = trie[c]["__child__"]

        return [i[1] for i in items]

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
