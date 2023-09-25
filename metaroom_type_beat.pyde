import random
def setup():
    size(500, 500)

circX1  = 250
circY1 = 250

circX2  = 250
circY2 = 250

circX3  = 250
circY3 = 250

circX4  = 250
circY4 = 250

circXU  = 250
circYU = 250

circXR  = 250
circYR = 250

circXR  = 250
circYR = 250

circXL  = 250
circYL = 250

r = 0
g = 255
b = 0

rr = 0
rg = 0
rb = 0

def draw():
    global circX1
    global circY1
    global circX2
    global circY2
    global circX3
    global circY3
    global circX4
    global circY4
    global r
    global g
    global b
    global rr
    global rg
    global rb
    
    fill(r,g,b)
    r = r + 1
    g = g - 1
    b = b + 1
    
    rr = random.randint(0,255)
    rg = random.randint(0,255)
    rb = random.randint(0,255)
    stroke(rr,rg,rb)
    
    line(0, mouseY, mouseX, 500)
    line(mouseX, 500, 500, mouseY)
    line(500, mouseY, mouseX, 0)
    line(0, mouseY, mouseX, 0)
    
    circle(circX1 ,circY1 , 50)
    circX1 = circX1 - 1
    circY1 = circY1 - 1
    
    circle(circX2 ,circY2 , 50)
    circX2 = circX2 + 1
    circY2 = circY2 - 1
    
    circle(circX3 ,circY3 , 50)
    circX3 = circX3 - 1
    circY3 = circY3 + 1
    
    circle(circX4 ,circY4 , 50)
    circX4 = circX4 + 1
    circY4 = circY4 + 1
