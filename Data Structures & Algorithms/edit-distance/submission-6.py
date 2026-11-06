class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        visited = {word1}
        bfs = [word1]
        count = 0

       
        while True:
            newlvl = []
            def insertWord(w):
                if w not in visited:
                    visited.add(w)
                    newlvl.append(w)

            for word in bfs:
                if word==word2: 
                    return count
                for i in range(max(len(word), len(word2))):
                    if i>=len(word):
                        insertWord(word+word2[i])
                        break
                    if i >=len(word2):
                        #only one option, delete
                        insertWord(word[0:i]+word[i+1:])
                        break
                    if word[i]!=word2[i]:
                        insertWord(word[0:i]+word2[i]+word[i+1:])
                        insertWord(word[0:i] + word2[i] + word[i:])
                        if (i+1)<len(word) and word[i+1]==word2[i]:
                            insertWord(word[0:i] + word[i+1:])
                        break
            bfs = newlvl
            count+=1
                
                        

