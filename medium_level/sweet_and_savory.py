import math

def sweetAndSavory(dishes, target):
    if all([x<0 for x in dishes]) or all([x>0 for x in dishes]) or len(dishes) == 0:
        return [0, 0]
    dishes.sort()
    sweetDishes = []
    savoryDishes = []
    for elem in dishes:
        if elem < 0:
            sweetDishes.append(elem)
        else:
            savoryDishes.append(elem)
    sweetDishes.reverse()
    sweetDishesIndex = 0
    savoryDishesIndex = 0
    sweetDishesLength = len(sweetDishes)
    savoryDishesLength = len(savoryDishes)
    bestCandidate = [0, 0]
    bestDistance = math.inf
    print(sweetDishes, savoryDishes)
    while True:
        candidate = [sweetDishes[sweetDishesIndex], savoryDishes[savoryDishesIndex]]
        candidate_sum = (candidate[0] + candidate[1])
        candidate_distance = candidate_sum - target
        if abs(candidate_distance) < bestDistance:
            if isValidCandidate(candidate_sum, target):
                bestDistance = abs(candidate_distance)
                bestCandidate = candidate
        if candidate_sum < target:
            if savoryDishesIndex < savoryDishesLength-1:
                savoryDishesIndex += 1
            elif sweetDishesIndex < sweetDishesLength-1:
                sweetDishesIndex += 1
        else:
            if sweetDishesIndex < sweetDishesLength-1:
                sweetDishesIndex += 1
            elif savoryDishesIndex < savoryDishesLength-1:
                savoryDishesIndex += 1
        if sweetDishesIndex == sweetDishesLength-1 and savoryDishesIndex == savoryDishesLength-1:
            # Ensure last entries of both lists are checked before exiting
            candidate = [sweetDishes[sweetDishesIndex], savoryDishes[savoryDishesIndex]]
            candidate_sum = (candidate[0] + candidate[1])
            candidate_distance = candidate_sum - target
            if abs(candidate_distance) < bestDistance:
                if isValidCandidate(candidate_sum, target):
                    bestDistance = abs(candidate_distance)
                    bestCandidate = candidate
            break
    return bestCandidate

def isValidCandidate(candidate_sum, target):
    if candidate_sum > target:
        return False
    return True
