class Solution:
    digits = "0123456789"
    
    def decodeString(self, s: str) -> str:
        number = 0
        ans = ""
        
        stack = []
        for i in s:
            if i == "]":
                repeatable = ""
                while stack and stack[-1] != "[":
                    repeatable = stack.pop() + repeatable
                
                if stack: stack.pop()

                number = ""
                while stack and stack[-1] in self.digits:
                    number = stack.pop() + number

                stack.append(repeatable * int(number or "1"))
            
            else:
                stack.append(i)
            
            # print(i, stack)
        
        return "".join(stack)
                
                
            
        