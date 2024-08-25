# O(n) time | O(n) space
def collidingAsteroids(asteroids):
    if not asteroids:
        return []
    stack = [asteroids[0]]
    for index in range(1, len(asteroids)):
        stack = asteroidOperation(asteroids[index], stack)
    return stack

def asteroidOperation(asteroid, stack):
    if not stack:
        return [asteroid]
    first = stack[-1]
    second = asteroid
    if first > 0 and second < 0:
        if abs(first) > abs(second):
            stack[-1] = first
        elif abs(second) > abs(first):
            stack[-1] = second
        else:
            stack.pop()
        if not stack:
            return []
        else:
            asteroid = stack.pop()
            return asteroidOperation(asteroid, stack)
    else:
        stack.append(second)
        return stack
