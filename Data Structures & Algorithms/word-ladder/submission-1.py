class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList: return 0
        depth = 0
        queue = []
        queue.append(beginWord)
        visited = set()
        while queue:
            depth+=1
            ls = []
            for word in queue:
                if word == endWord:
                    return depth
                if word in visited:
                    continue
                visited.add(word)
                for i in range(len(word)):
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        newWord = word[:i] + c + word[i+1:]
                        print(newWord)
                        if newWord in wordList:
                            ls.append(newWord)
            queue = ls
        return 0