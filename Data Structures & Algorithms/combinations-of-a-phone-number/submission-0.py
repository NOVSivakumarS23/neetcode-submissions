class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #dfs is better becuase it builds each string solution one by one instead of appending
        if not digits:
            return []
            
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []
        
        def dfs(idx: int, path: list[str]):
            # Base case: completed a full combination
            if idx == len(digits):
                res.append("".join(path))
                return
            
            # Explore all mapped characters for the current digit
            for char in mapping[digits[idx]]:
                path.append(char)     # CHOOSE
                dfs(idx + 1, path)    # EXPLORE
                path.pop()            # UNCHOOSE
                
        dfs(0, [])
        return res
        