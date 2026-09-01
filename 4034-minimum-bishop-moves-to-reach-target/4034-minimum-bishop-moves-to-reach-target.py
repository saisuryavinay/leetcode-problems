class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        sx = source[0]
        sy = source[1]

        tx = target[0]
        ty = target[1]

        if (sx + tx) % 2 != (sy + ty) % 2:
            return -1
        elif sx == tx and sy == ty:
            return 0
        elif abs(sx-tx) == abs(sy-ty):
            return 1
        else:
            return 2