# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    if not buildings:
        return []
    if direction == 'WEST':
        highestBuilding = 0
        visibleBuildings = []
        for buildingIndex in range(len(buildings)):
            if buildings[buildingIndex] > highestBuilding:
                visibleBuildings.append(buildingIndex)
                highestBuilding = buildings[buildingIndex]
        return visibleBuildings
    elif direction == 'EAST':
        highestBuilding = 0
        visibleBuildings = []
        for buildingIndex in range(len(buildings)-1, -1, -1):
            if buildings[buildingIndex] > highestBuilding:
                visibleBuildings.append(buildingIndex)
                highestBuilding = buildings[buildingIndex]
        return visibleBuildings[::-1]
