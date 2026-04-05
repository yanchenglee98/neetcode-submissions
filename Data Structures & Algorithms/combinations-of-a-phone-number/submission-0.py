class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        combi = []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(combi))
                return
            
            for c in digitToChar[digits[i]]:
                # include this character
                combi.append(c)
                dfs(i+1)
                # backtrack 
                combi.pop()
        if len(digits) == 0: return []
        dfs(0)
        return res
        