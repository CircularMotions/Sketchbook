#scope of a variable: global & Local

def setup():
    size(500, 500)
    colorMode(HSB)

def draw():
    #RGBA
    #Hue/Saturation/Value                                                                                                           (>_<)
    
    f = 10.0
    g = 20.0
    h = 5
    
    f = f + 1
    f += 1
    
    g -= 30
    g = g - 27
    
    g = f * h
    h *= 2
    
    g = f / h
    h = h / 2.5
    
    f = pow(g, 2)
    
    h = h- 7
    g += f
    f += g
    h = f - (g + 5)
    
    println(f)
    println(g)
    println(h)
    
    
    println(f/2)
    println(f)
    background(255)#                                                            X3
    stroke(80, 255, 255);
    line(mouseX, 10, 100, mouseY)
    rectMode(CORNERS)
    rect(20, 20,  50, 100)
    noStroke()
    ellipse(200, 200, 100, 5)
    fill(90, mouseX/2, 255)
    circle(mouseX, mouseY, 50)#                                                                                                                                                                      :P
