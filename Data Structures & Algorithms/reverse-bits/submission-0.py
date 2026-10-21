class Solution:
    def reverseBits(self, n: int) -> int:
        a = 1
        b = 2147483648
        res = 0
        while b>0:
            if (a & n)!=0:
                res = res | b
            b = b>>1
            a = a<<1
        return res
