# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class TrieNode:
    def __init__(self):
        self.is_end = False
        self.children = [ None for _ in range(26) ]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        iterator = self.root
        for char in word:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                iterator.children[loc] = TrieNode()
            
            iterator = iterator.children[loc]
            
        iterator.is_end = True 

    def search(self, word: str) -> bool:
        iterator = self.root
        for char in word:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                return False
            
            iterator = iterator.children[loc]

        return iterator.is_end

    def startsWith(self, prefix: str) -> bool:
        iterator = self.root
        for char in prefix:
            loc = ord(char) - ord('a')
            if not iterator.children[loc]:
                return False
            
            iterator = iterator.children[loc]

        return True

    

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        trie = Trie()
        ans = 0

        words.sort(key=lambda x: -len(x))

        for word in words:
            if not trie.startsWith(word[::-1]):
                ans += len(word) + 1
                trie.insert(word[::-1])

        return ans