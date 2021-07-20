class Solution:
    def romanToInt(self, s: str) -> int:
        s_len = len(s)
        _ = 0
        value = 0
        while _ < s_len :
            if s[_] == 'I' :
                if _ != (s_len - 1) and s[_ + 1] == 'V':
                    value += 4
                    _ += 2
                elif _ != (s_len - 1) and s[_ + 1] == 'X' :
                    value += 9
                    _ += 2
                else :
                    value += 1
                    _ += 1
            elif s[_] == 'V' :
                value += 5
                _ += 1
            elif s[_] == 'X' :
                if _ != (s_len - 1) and s[_ + 1] == 'L' :
                    value += 40
                    _ += 2
                elif _ != (s_len - 1) and s[_ + 1] == 'C' :
                    value += 90
                    _ += 2
                else :
                    value += 10
                    _ += 1
            elif s[_] == 'L' :
                value += 50
                _ += 1
            elif s[_] == 'C' :
                if _ != (s_len - 1) and s[_ + 1] == 'D' :
                    value += 400
                    _ += 2
                elif _ != (s_len - 1) and s[_ + 1] == 'M' :
                    value += 900
                    _ += 2
                else :
                    value += 100
                    _ += 1
            elif s[_] == 'D' :
                value += 500
                _ += 1
            elif s[_] == 'M' :
                value += 1000
                _ += 1
        return value
        

        
