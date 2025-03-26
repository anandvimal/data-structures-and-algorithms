class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        right_stack = []
        left_stack = []
        for asteroid in asteroids:
            if asteroid > 0: # going right
                right_stack.append(asteroid)
            elif asteroid < 0: # -ve left
                if len(right_stack) > 0:
                    if right_stack[len(right_stack)-1] > abs(asteroid): #if right is bigger left destroy
                        continue
                    elif right_stack[len(right_stack)-1] < abs(asteroid):
                        while len(right_stack) > 0  and right_stack[len(right_stack)-1] < abs(asteroid):
                            right_stack.pop()
                        if len(right_stack) > 0:
                            if right_stack[len(right_stack)-1] == abs(asteroid):
                                right_stack.pop()
                                asteroid = None
                                continue
                    elif right_stack[len(right_stack)-1] == abs(asteroid):
                        right_stack.pop()
                        asteroid = None
                        continue
                    if len(right_stack) == 0 and asteroid is not None:
                        left_stack.append(asteroid)
                elif len(right_stack) ==0:
                    left_stack.append(asteroid)
        stack = left_stack + right_stack
        return stack