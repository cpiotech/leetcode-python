class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        distance = 0
        current = [beginWord]
        visited = [beginWord]

        d = {}
        for word in wordList:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

        while current:
            # queue
            _next = []

            for word in current:
                if word == endWord:
                    return distance + 1
                for i in range(len(word)):
                    b = word[:i] + '_' + word[i + 1:]
                    if b in d:
                        for c in d[b]:
                            if c not in visited:
                                _next.append(c)
                                visited.append(c)
            distance += 1
            current = _next

        return 0

import collections

class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        w = set(wordList)
        # w.add(endWord)
        queue = collections.deque([[beginWord, 1]])
        print queue
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in w:
                        w.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

if __name__ == "__main__":
    # print Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
    # print Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print Solution2().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    # print Solution2().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])