import random
def  setup():
    size(500, 500)

circX = 250
circY = 250
xAccel = random.randint(-10, 10)
yAccel = random.randint(-10, 10)
r = 255
g = 255
b = 255

def draw():
    global circX
    global circY
    global xAccel
    global yAccel
    global r
    global g
    global b
    fill(r, g, b)
    circle(circX, circY, 50)
    circX = circX + xAccel
    circY = circY + yAccel
    if circX >= 475:
        xAccel = xAccel*-1
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    if circX <= 25:
        xAccel = xAccel*-1
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    if circY >= 475:
        yAccel = yAccel*-1
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    if circY <= 25:
        yAccel = yAccel*-1
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
    
