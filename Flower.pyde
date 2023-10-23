import random
def setup():
    global cx, cy
    size(500, 500)
    background(0)
    colorMode(HSB)
    cx = width/2
    cy = height/2
    
    
go = 0
num = 100
cx = 0
cy = 0
r = 100
flowersize = 1

def draw():
    global num, cx, cy, r, go, flowersize
    theta = TWO_PI / 360
    omega = TWO_PI / 5
    
    #noStroke()
    if go == 0:
        for i in range(num):
            stroke(255, 191, 222)
            strokeWeight(5 * flowersize)
            r = random.randint(1, 300)
            angle = theta * random.randint(1, 360)
            c = (i / float(num)) * 255
            print(c)
            x = cx + (sin(angle) * r)
            y = cy + (cos(angle) * r)
            line(cx, cy, x, y)
            offset = random.randint(1, 50)
            noStroke()
            for j in range(5):
                sAngle = (omega * j) + offset
                sx = x + (sin(sAngle) * (20 * flowersize))
                sy = y + (cos(sAngle) * (20 * flowersize))
                fill(202, 191, 191)
                circle(sx - ((sx - x) / 2), sy - ((sy - y) / 2), 10 * flowersize)
                circle(sx - ((sx - x) / 3), sy - ((sy - y) / 3), 15 * flowersize)
                circle(sx, sy, 20 * flowersize)
                fill(234, 255, 220)
                circle(x, y, 20 * flowersize)
            go = 1
