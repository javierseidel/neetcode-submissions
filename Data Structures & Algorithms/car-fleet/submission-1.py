class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for i,j in pair:
            stack.append((target - i) / j)
            
            if len(stack) > 1:
                if stack[-1] <= stack[-2]:
                    stack.pop()

        return len(stack)
