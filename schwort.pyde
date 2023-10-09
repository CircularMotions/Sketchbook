def setup():
    size(500, 1500)
    background(0)

triY1= 100
triY2= 400
rad = 1
sRad = 1
dir1 = 200
dir2 = 250
dir3 = 250
c = 255

def draw():
    global triY1
    global triY2
    global rad
    global sRad
    global dir1
    global dir2
    global dir3
    global c
    
    if triY1 == 500:
        fill(c, 255, c)
        circle(250, dir1, sRad)
        fill(255, c, c)
        circle(dir2, triY2, sRad)
        fill(c, c, 255)
        circle(dir3, triY2, sRad)
        if sRad < 50:
            sRad=sRad+1
        elif sRad == 50:
            dir1=dir1-1
            dir2=dir2-1
            dir3=dir3+1
            c=c-1
    fill(255, 255, 255) 
    triangle(100, triY1, 400, triY1, 250, triY2)
    if triY1 < 500:
        triY1=triY1+1
        triY2=triY2-0.5
        if triY2 <= triY1:
            circle(250, triY2, rad)
            rad=rad+1
    
