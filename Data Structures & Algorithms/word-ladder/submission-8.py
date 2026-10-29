class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lookup = {}
        wordList.append(beginWord)
        for i in range(0, len(wordList)):
            for j in range(i+1, len(wordList)):
                #compare string
                c = 0
                for k in range(len(wordList[0])):
                    if wordList[i][k] != wordList[j][k]:
                        c+=1
                if c==1:
                    if wordList[i] in lookup: lookup[wordList[i]].append(wordList[j])
                    else: lookup[wordList[i]] = [wordList[j]]

                    if wordList[j] in lookup: lookup[wordList[j]].append(wordList[i])
                    else: lookup[wordList[j]] = [wordList[i]]
            if not wordList[i] in lookup:
                lookup[wordList[i]] = []
        #graph is built lets do bfs
        print(lookup)
        reps = {beginWord}
        paths = deque([beginWord])
        c = 2
        while(len(paths)>0):
            print(paths)
            for i in range(len(paths)):
                for val in lookup[paths[0]]:
                    if val==endWord:
                        return c
                    if not val in reps:
                        paths.append(val)
                        reps.add(val)
                paths.popleft()
            c+=1
        return 0




        