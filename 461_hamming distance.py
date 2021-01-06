class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bit_x, bit_y, diff = bin(x)[2:].zfill(32), bin(y)[2:].zfill(32), 0

        for i in range(32):
            if bit_x[i] != bit_y[i]:
                diff += 1
        return diff