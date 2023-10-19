def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
    blueShirtHeights.sort()
    n = len(redShirtHeights)
    if (redShirtHeights[0] < blueShirtHeights[0]):  ## red row first
        for i in range(n):
            if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
        return True
    else: ## blue row first
        for i in range(n):
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False
        return True
