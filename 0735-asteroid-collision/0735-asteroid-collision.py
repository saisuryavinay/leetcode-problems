class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            while stack and i < 0 and stack[-1] > 0:
                ans = i + stack[-1]
                if ans > 0:
                    break
                elif ans < 0:
                    stack.pop()
                else:
                    stack.pop()
                    break
            else:
                stack.append(i)
        return stack