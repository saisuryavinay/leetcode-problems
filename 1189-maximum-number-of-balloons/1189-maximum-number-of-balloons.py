class Solution:
    def maxNumberOfBalloons(self, ans: str) -> int:
        hash_map = {}
        for text in ans:
            hash_map[text] = hash_map.get(text,0) + 1

        return min(
        hash_map.get('b', 0),
        hash_map.get('a', 0),
        hash_map.get('l', 0) // 2,
        hash_map.get('o', 0) // 2,
        hash_map.get('n', 0)
    )