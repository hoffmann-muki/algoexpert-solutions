def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    if fastest:  
        blueShirtSpeeds.sort(reverse=True)
        return sum([max(x,y) for (x,y) in zip(redShirtSpeeds, blueShirtSpeeds)])
    else:
        blueShirtSpeeds.sort()
        return sum([max(x,y) for (x,y) in zip(redShirtSpeeds, blueShirtSpeeds)])