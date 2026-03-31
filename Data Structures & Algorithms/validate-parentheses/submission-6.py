class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            # 1. If it's an opening bracket, push to stack
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            
            # 2. If it's a closing bracket
            elif i == ")" or i == "}" or i == "]":
                if stack == []:
                    return False
                
                # These checks must be OUTSIDE the 'if stack == []' block
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                else:
                    # If it's a closing bracket but doesn't match the top
                    return False
        
        # 3. Final check: stack should be empty if all pairs matched
        return len(stack) == 0