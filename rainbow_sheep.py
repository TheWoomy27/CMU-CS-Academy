app.background = 'lightSkyBlue'

### Sheep

# Legs

def drawSheepLeg(x, y):
    Polygon(x, y, x+40, y-15, x+40, y-25, x, y-10, x-40, y-25, x-40, y-15, fill=rgb(41, 34, 30))
    Polygon(x, y-10, x, y-70, x-40, y-85, x-40, y-25, fill=rgb(137, 114, 96))
    Polygon(x, y-10, x+40, y-25, x+40, y-85, x, y-70, fill=rgb(87, 72, 59))

drawSheepLeg(120, 360)
drawSheepLeg(190, 390)
drawSheepLeg(250, 300)
drawSheepLeg(310, 330)

# Body

colorChange = Polygon(45, 175, 45, 200, 70, 210, 70, 271, 120, 290, 130, 287, 130, 300, 190, 320, 240, 304, 240, 235, 260, 230, 260, 245, 310, 260, 365, 245, 365, 180, 375, 175, 375, 70, 250, 10, 120, 50, 110, 45, 40, 80 ,fill=rgb(255, 0, 0))

Polygon(375, 70, 375, 175, 365, 180, 365, 245, 310, 260, 310, 215, 240, 235, 240, 304, 190, 320, 190, 255, 170, 260, 170, 135, opacity=40)
Polygon(120, 290, 130, 287, 130, 260, 120, 255, opacity=40)
Polygon(110, 105, 180, 70, 180, 110, 145, 123, 145, 185, 110, 200, opacity=40)
Polygon(190, 320, 190, 255, 170, 260, 170, 135, 145, 123, 145, 185, 110, 200, 110, 105, 40, 80, 40, 100, 45, 175, 45, 200, 70, 210, 70, 271, 120, 290, 120, 255, 130, 260, 130, 300, opacity=20)
Polygon(310, 260, 310, 215, 260, 230, 260, 245, opacity=20)

# Head

Polygon(90, 190, 90, 120, 30, 100, 30, 170, fill=rgb(156, 156, 156))
Polygon(90, 190, 105, 180, 105, 157, 100, 161, 100, 130, 105, 125, 105, 110, 90, 120, fill=rgb(100, 100, 100))
Polygon(100, 165, 105, 160, 105, 120, 100, 125, fill=rgb(87, 72, 60))
Polygon(90, 120, 30, 100, 45, 90, 105, 110, fill=rgb(225, 225, 225))
Polygon(80, 187, 80, 160, 90, 164, 90, 130, 30, 110, 30, 145, 40, 150, 40, 172, fill=rgb(130, 108, 92))

Polygon(90, 144, 90, 154, 80, 150, 80, 140)
Polygon(80, 140, 80, 150, 70, 146, 70, 137, fill='white')
Polygon(30, 123, 40, 128, 40, 138, 30, 133)
Polygon(40, 129, 40, 138, 50, 142, 50, 133, fill='white')

Polygon(50, 153, 70, 160, 70, 183, 50, 175, fill=rgb(186, 132, 132))

### Nametag 

nametag = Group(
    
    Rect(100, 5, 140, 55, opacity=15),
    Rect(100, 5, 140, 55, fill=None, border=rgb(50, 50, 50), borderWidth=5),
    
    # j
    Rect(110, 35, 5, 10, fill='white'),
    Rect(115, 45, 15, 5, fill='white'),
    Rect(130, 25, 5, 20, fill='white'),
    Rect(130, 15, 5, 5, fill='white'),
    # e
    Rect(145, 25, 15, 5, fill='white'),
    Rect(140, 30, 5, 15, fill='white'),
    Rect(145, 45, 20, 5, fill='white'),
    Rect(145, 35, 20, 5, fill='white'),
    Rect(160, 30, 5, 5, fill='white'),
    # b
    Rect(170, 15, 5, 35, fill='white'),
    Rect(175, 45, 15, 5, fill='white'),
    Rect(190, 30, 5, 15, fill='white'),
    Rect(175, 30, 5, 5, fill='white'),
    Rect(180, 25, 10, 5, fill='white'),
    # _
    Rect(200, 45, 25, 5, fill='white')
)

### Rainbow 

# Labels

redCounter = Label(255, 310, 350, visible=False)       # These counters will be the rgb values 
greenCounter = Label(0, 335, 350, visible=False) 
blueCounter = Label(0, 360, 350, visible=False)

redDirection = Label('Up', 310, 375, visible=False)    # These are the direction labels that make the number of the counters increase or decrease  
greenDirection = Label('Up', 335, 375, visible=False)
blueDirection = Label('Down', 360, 375, visible=False)

# Counter Boundaries

def enforceCounterBoundaries():      # Whenever this function is called, it will make sure that the counters are within the range of possible rgb values 

   if (redCounter.value > 255):
        redCounter.value = 255
   if (greenCounter.value > 255):
        greenCounter.value = 255
   if (blueCounter.value > 255):
        blueCounter.value = 255
   if (redCounter.value < 0):
       redCounter.value = 0
   if (greenCounter.value < 0):
       greenCounter.value = 0
   if (blueCounter.value < 0):
       blueCounter.value = 0

app.stepsPerSecond = 220
def onStep():

# Red     
   
   if (redCounter.value == 255):            # When all of the counters reach a specific number, the direction of one of the colors goes either up or down
       if(greenCounter.value == 255):
           if(blueCounter.value == 0):
                redDirection.value = 'Down' # In this case, when the counters are (255, 255, 0), the direction of the red color will be down, because that's when the red value is supposed to decrease
           
   if (redCounter.value == 0):
       if(greenCounter.value == 0):
           if(blueCounter.value == 255):
               redDirection.value = 'Up'

   if (redDirection.value == 'Up'): # If the direction is 'Up', the counter will increase by 1
        redCounter.value += 1
   else:                            # If the direction is 'Down', the counter will decrease by 1
        redCounter.value -= 1

   enforceCounterBoundaries()       # Call the counter boundaries function after each color algorithm so that the direction for the next color will update properly
            
# Green 

   if (redCounter.value == 255):
       if(greenCounter.value == 0):
           if(blueCounter.value == 0):
                greenDirection.value = 'Up'
           
   if (redCounter.value == 0):
       if(greenCounter.value == 255):
           if(blueCounter.value == 255):
               greenDirection.value = 'Down'


   if (greenDirection.value == 'Up'):
        greenCounter.value += 1
   else:
        greenCounter.value -= 1

   enforceCounterBoundaries()
            
# Blue         

   if (redCounter.value == 0):
       if (greenCounter.value == 255):
           if (blueCounter.value == 0):
               blueDirection.value = 'Up'
           
   if (redCounter.value == 255):
       if (greenCounter.value == 0):
           if (blueCounter.value == 255):
               blueDirection.value = 'Down'

   if (blueDirection.value == 'Up'):
        blueCounter.value += 1
   else:
        blueCounter.value -= 1
        
   enforceCounterBoundaries()

# Rainbow

   colorChange.fill = rgb(redCounter.value, greenCounter.value, blueCounter.value)  # Updates the color of the sheep
   
### Nametag angle

def onMouseMove(mouseX, mouseY):
    
   if (mouseX < 200):                       # Change the angle of the nametag to face the mouse
      nametag.rotateAngle = 380-mouseX/10
   else:
       nametag.rotateAngle = 380-mouseX/10
       
# Show Labels

   if (mouseX > 350):                   # Show the counters and directions if the mouse is in the bottom right corner
      if (mouseY > 350):
        redCounter.visible = True
        greenCounter.visible = True
        blueCounter.visible = True
        redDirection.visible = True
        greenDirection.visible = True 
        blueDirection.visible = True
   else:
      redCounter.visible = False
      greenCounter.visible = False
      blueCounter.visible = False
      redDirection.visible = False
      greenDirection.visible = False 
      blueDirection.visible = False
