def setup():
    size(1000, 500)

def draw():
    background(255, 0, 0)
    fill(255, 255, 0)                    #OMG HAAAAIIIIIII :D   (¬.¬)
    noStroke()
    circle(250, 250, 400)
    circle(750, 250, 400)
    circle(mouseX, mouseY, 100)
    fill(0, 255, 255)                       #Rawr~ X3 ('3')
    triangle(250, 20, 50, 445, 450, 445)   # Heyyy :D (>_<) :3
    triangle(750, 480, 950, 55, 550, 55)
    triangle(mouseX, mouseY-55, mouseX-50, mouseY+40, mouseX+50, mouseY+40)
    fill(255)
    ellipse(250, 250, 200, 100)
    ellipse(750, 250, 200, 100)
    ellipse(mouseX, mouseY, 100, 50)
    fill(0)
    circle(250, 250, 75)
    circle(750, 250, 75)
    
