import random
def setup():
    global cx
    global cy
    global r
    global theta
    global px
    global py
    global cx2
    global cy2
    global r2
    global theta2
    global px2
    global py2
    size(1000, 1000)
    cx = width/2
    cy = height/2
    px = cx
    py = cy
    cx2 = width/2
    cy2 = height/2
    px2 = cx2
    py2 = cy2
    background(0)

cx = 0
cy = 0
r = 1
theta = 0
px = 0
py = 0
trans = 255

cx2 = 0
cy2 = 0
r2 = 1
theta2 = 0
px2 = 0
py2 = 0
trans2 = 255

def draw():
    global cx
    global cy
    global r
    global theta
    global px
    global py
    global cx2
    global cy2
    global r2
    global theta2
    global px2
    global py2
    global trans
    x = cx + sin(theta) * r
    y = cy + cos(theta) * r
    stroke(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    line(px, py, x, y)
    
    x2 = cx2 + sin(theta) * r2
    y2 = cy2 + cos(theta) * r2
    stroke(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    line(px2, py2, x2, y2)
    
    r = r + 10
    theta = theta + 1
    
    r2 = r2 - 10
    theta2 = theta2 - 1
#    if r < 500:
#        theta = theta + 49
#    else:
#        r = 0
    
    px = x
    py = y
    
    px2 = x2
    py2 = y2
