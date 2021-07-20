class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s :
            if letter in ['(', '[', '{'] :
                stack.append(letter)
            elif stack != [] and stack[-1] in ['(', '[', '{'] :
                if letter == ')' and stack[-1] == '(' :
                    stack.pop()
                elif letter == ']' and stack[-1] == '[' :
                    stack.pop()
                elif letter == '}' and stack[-1] == '{' :
                    stack.pop()
                else :
                    return False
            else :
                return False
        if stack == [] :
            return True
        else :
            return False
