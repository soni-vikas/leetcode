bracket_map = {
    ")": "(", 
    "}": "{", 
    "]": "[",
}

opens = bracket_map.values()
closes = bracket_map.keys()

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            # print(i, stack)
            if i in opens:
                stack.append(i)
            elif (not stack) or stack[-1] != bracket_map[i]:
                return False
            else:
                stack.pop()
        
        return not stack
                
