import random
def setup():
    size(500, 500)
    colorMode(HSB)

tlColor = 60
trColor = 180
blColor = 120
brColor = 240

def draw():
    global tlColor
    global trColor
    global blColor
    global brColor
    noStroke()
    if mouseX < width/2:
        if mouseY < height/2:
            fill(tlColor, 255, 255)
        else:
            fill(blColor, 255, 255)
    else:
        if mouseY < height/2:
            fill(trColor, 255, 255)
        else:
            fill(brColor, 255, 255)
    circle(mouseX, mouseY, 50)#                                                                         (>_<)
    if (mouseX > 200) and (mouseX < 300) and (mouseY > 200) and (mouseY < 300):
        fill(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        tlColor = tlColor + 1
        trColor = trColor + 1
        blColor = blColor + 1
        brColor = brColor + 1
        if tlColor == 255:
            tlColor = 0
        elif trColor == 255:
            trColor = 0
        elif blColor == 255:
            blColor = 0
        elif brColor == 255:
            brColor =0
    else:
        fill(0, 0, 255)
    rect(200, 200, 100, 100)
