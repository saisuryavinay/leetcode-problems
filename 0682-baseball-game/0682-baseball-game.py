class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i.isdigit() or i.lstrip("-").isdigit():
                stack.append(int(i))
            elif i == "C":
                stack.pop()
            elif i == "D":
                stack.append(stack[-1] * 2)
            elif i == "+":
                ans = stack[-1] + stack[-2]
                stack.append(ans)

        return sum(stack)