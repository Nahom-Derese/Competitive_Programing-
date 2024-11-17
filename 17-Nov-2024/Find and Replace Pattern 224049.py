# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        return [i for i in words if [*map(i.index, i)] == [*map(pattern.index, pattern)]]