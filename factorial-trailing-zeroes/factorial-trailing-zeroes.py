class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailingZeroes = 0
        while n >= 5 :
            n //= 5
            trailingZeroes += n
        return trailingZeroes
        
