import math
import time

app.angle = 0
app.mouseX = 0
app.mouseY = 0
app.time = time.time()
app.speed = 0

spinner = Group(
    # Middle
    Circle(200, 200, 60, fill = "skyBlue"),
    Circle(200, 200, 30, fill = "skyBlue", border = gradient("grey", "black", start = "left"), borderWidth = 1),
    
    # Top
    Circle(200, 125, 42, fill = "skyBlue"),
    Circle(200, 125, 32, fill = "black", border = "silver", borderWidth = 4),
    Circle(200, 125, 15, fill = "white", border = "silver", borderWidth = 4),
    
    # Left
    Circle(133, 235, 42, fill = "skyBlue"),
    Circle(133, 235, 32, fill = "black", border = "silver", borderWidth = 4),
    Circle(133, 235, 15, fill = "white", border = "silver", borderWidth = 4),
    
    # Right
    Circle(266, 235, 42, fill = "skyBlue"),
    Circle(266, 235, 32, fill = "black", border = "silver", borderWidth = 4),
    Circle(266, 235, 15, fill = "white", border = "silver", borderWidth = 4),
    
    # Empty space
    Circle(132, 159, 35, fill = "white"),
    Circle(268, 159, 35, fill = "white"),
    Circle(200, 275, 36, fill = "white"),
)

app.stepsPerSecond = 90
def onStep():
    spinner.rotateAngle += app.speed / 80
    if app.speed > 0:
        app.speed -= 0.5
    elif app.speed < 0:
        app.speed += 0.5

def onMouseMove(x, y):
    app.mouseX = x
    app.mouseY = y

def onMouseDrag(x, y):
    
    direction_x = x - app.mouseX
    direction_y = y - app.mouseY
    
    # Calculate distance moved
    distance = ((x - app.mouseX)**2 + (y - app.mouseY)**2)**0.5
    
    # Calculate time taken
    current_time = time.time()
    time_difference = current_time - app.time
    
    # Calculate speed
    app.speed = distance / time_difference
    
    if direction_x > 0 or direction_y < 0:
        app.speed *= -1
    
    print(app.speed)

    # Update previous position and time
    app.mouseX, app.mouseY = x, y
    app.time = current_time
        
