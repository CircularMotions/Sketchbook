def setup():
    size(500, 500)
    colorMode(HSB)
    for i in range(10):
        print(i)
    
    for i in range(20, 30, 2):
        print(i)
    
def draw():
    background(0)
    stroke(255)
    
    line(100, 100, 100, 400)
    line(400, 100, 400, 400)
    
    for y in range(200, 261, 20):
        line(100, y, 400, y)

    
    for i in range(4):
        y = 300 + (i*20)
        line(100, y, 400, y)
    
    for i in range(4):
        y = map(i, 0, 3, 400, 430)
        line(100, y, 400, y)
