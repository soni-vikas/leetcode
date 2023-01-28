class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.generate("", 0, 0, n, res)
        return res
    
    def generate(self, so_far, _open, _close, n, res):
        if _close == n:
            res.append(so_far)
            return
            
        if _open < n:
            self.generate(so_far + "(", _open + 1, _close, n, res)
        
        if _open > _close:
            self.generate(so_far + ")", _open, _close + 1, n, res)
        
