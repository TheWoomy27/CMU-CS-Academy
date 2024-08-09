### To do list:
# difficulty animation
# ball menu come from edge
# functional difficulty
# multiplayer
# fix able to change difficulty in custom menu
# finish custom menu buttons 
# 3D mode

### Objects / Defines

import math

app.background =  "black"
app.opening = False 
app.state = "booting"  ### Possible states: booting, idle, starting1, starting2, starting3, starting4, customizing1, customizing2, painting, lining1, lining 2, ingame, paused, lose, reseting
app.stepsPerSecond = 90
app.bgColorCounter = 0
app.difficulties = ["Easy", "Normal", "Hard", "Dynamic"]
app.index = 1
app.autoAIEnabled = True

baseRect = Rect(0, 250, 400, 150, fill = "white")   

c = Circle(200, -25, 20, fill="navy", opacity = 100)    
c.red = 0
c.green = 0
c.blue = 128
c.dy = 0
c.dx = 0
c.angle = 0
c.bottom = baseRect.top
c.leftHitsGap = False
c.rightHitsGap = False
c.corner = "none"
c.isCorner = True
c.cornerSteps = 0
c.fxSteps = 0

cosmetic = Group(
    Circle(185, 225, 2, fill = 'white'),
    Circle(215, 225, 2, fill = 'white'),
    Line(185, 240, 215, 240, fill = 'white'))
cosmeticLine = Line(0, 0, 0, 0, fill = 'white', lineWidth = 2) 

score = Label(0, 200, 50, fill = "white", visible = True, size = 50, opacity = 0)   
score.animation = 0
score.angle = 0

gap1 = Line(50, 250, 50, 250, fill = "black", lineWidth = 50)  
gap2 = Line(50, 250, 50, 250, fill = "black", lineWidth = 50)
gap3 = Line(50, 250, 50, 250, fill = "black", lineWidth = 50)
gap4 = Line(50, 250, 50, 250, fill = "black", lineWidth = 50)
gap5 = Line(50, 250, 50, 250, fill = "black", lineWidth = 50, visible = False)
gaps = [gap1, gap2, gap3, gap4, gap5]

vignette = Rect(0, 0, 400, 400, opacity = 0)    

startSound = Sound("https://studio.code.org/api/v1/sound-library/category_accent/puzzle_game_accent_a_04.mp3") 
explosion = Sound("https://studio.code.org/api/v1/sound-library/category_explosion/vibrant_deep_wet_explosion.mp3")
unpauseSound = Sound("https://studio.code.org/api/v1/sound-library/category_pop/vibrant_game_harvest_collect_bubble_pop.mp3")
pauseSound = Sound("https://studio.code.org/api/v1/sound-library/category_tap/vibrant_game_water_drop_game_touch_1.mp3")
bounceSound = Sound("https://studio.code.org/api/v1/sound-library/category_app/snap.mp3")
cornerSound = Sound("https://studio.code.org/api/v1/sound-library/category_app/app_button_1.mp3")
loseSound = Sound("https://studio.code.org/api/v1/sound-library/category_app/bass_power_off.mp3")
music = Sound("https://studio.code.org/api/v1/sound-library/category_background/synthesize.mp3")
music.play(loop=True)
click = Sound("https://studio.code.org/api/v1/sound-library/category_app/modern_ui_sound.mp3")
easySound = Sound("cmu://584498/26345333/vibrant_game_dirty_desolve_0.wav")
normalSound = Sound("https://studio.code.org/api/v1/sound-library/category_hits/vibrant_game_dirty_desolve_1.mp3")
hardSound = Sound("https://studio.code.org/api/v1/sound-library/category_hits/vibrant_game_dirty_desolve_2.mp3")
dynamicSound = Sound("https://studio.code.org/api/v1/sound-library/category_hits/vibrant_game_deep_hit.mp3")

menuUI = {
    "difficultyLabel": Label("Normal", 200, 170, fill = "white", bold = True, size = 20, opacity = 0),
    "box": Rect(100, 100, 200, 100, fill = None, border = "white", borderWidth = 5, opacity = 0),
    "title": Label("Sphere Sprint", 200, 40, size = 30, fill = "white", bold = True, opacity = 0),
    "startLabel": Label("[ START ]", 200, 135, fill = "white", bold = True, size = 20, opacity = 0),
    "startButton": Rect(155, 125, 90, 25, opacity = 0),
    "leftDifficultyLabel": Label("<", 135, 170, fill = 'white', bold = True, size = 20, opacity = 0),
    "leftDifficultyButton": Rect(125, 160, 20, 20, opacity = 0),
    "rightDifficultyLabel": Label(">", 265, 170, fill = 'white', bold = True, size = 20, opacity = 0),
    "rightDifficultyButton": Rect(255, 160, 20, 20, opacity = 0),
    }
    
pauseButton = Group(
    Rect(15, 15, 25, 25, fill = None, border = 'white', borderWidth = 3),
    Label("||", 27.5, 26.5, fill = 'white', size = 15, bold = True),
    Rect(15, 15, 25, 25, opacity = 0)
    )
    
pauseUI = Group(
    Rect(100, 100, 200, 100, fill = None, border = "white", borderWidth = 5, opacity = 0),
    Label("[ PAUSED ]", 200, 150, fill = "white", bold = True, size = 20, opacity = 0),
    )
    
customButton = Group(
    Rect(15, 45, 25, 25, fill = None, border = 'white', borderWidth = 3),
    Circle(27.5, 57.5, 5, fill = 'white'),
    Rect(15, 45, 25, 25, opacity = 0)
    )

redSlider = Line(75, 75, 150, 75, fill = 'red', lineWidth = 5, opacity = 0)
redBall = Circle(75, 75, 7, fill = 'white', opacity = 0)
redBall.touch = False
greenSlider = Line(75, 90, 150, 90, fill = 'lime', lineWidth = 5, opacity = 0)
greenBall = Circle(75, 90, 7, fill = 'white', opacity = 0)
greenBall.touch = False
blueSlider = Line(75, 105, 150, 105, fill = 'blue', lineWidth = 5, opacity = 0)
blueBall = Circle(113, 105, 7, fill = 'white', opacity = 0)
blueBall.touch = False
paintButton = Group(
    Rect(200, 100, 25, 25, fill = "black", opacity = 0),
    Rect(200, 100, 25, 25, fill = None, border = 'white', borderWidth = 3, opacity = 0),
    )
lineButton = Group(
    Rect(250, 100, 25, 25, fill = "black", opacity = 0),
    Rect(250, 100, 25, 25, fill = None, border = 'white', borderWidth = 3, opacity = 0),
    )
customUI = Group(
    Rect(50, 50, 300, 150, fill = None, border = "white", borderWidth = 5, opacity = 0),
    redSlider,
    redBall,
    greenSlider,
    greenBall,
    blueSlider,
    blueBall,
    paintButton,
    lineButton,
    )
    
### Functions

def changeGaps(action): 

    if (action == "open"):
        
        app.opening = True
        for gap in gaps:
            if gap.visible == True:
                gap.centerX = randrange(0,390)
            else: 
                gap.centerX = 500
    
    elif (action == "close"):
        
        app.opening = False
     
def onKeyPress(key):
    
    if key == "escape":
        if app.state == "ingame":
            app.state = "paused"
            pauseSound.play(restart=True)
        elif app.state == "paused":
            app.state = "ingame"
            unpauseSound.play(restart=True)
        elif "customizing" in app.state:
            app.state = "booting"

def onKeyHold(keys):

    if app.state != "lose" and app.state != "paused":
    
        if ("right" in keys): 
            c.centerX += 6
            cosmetic.rotateAngle += 6
        elif ("left" in keys):
            c.centerX -= 6
            cosmetic.rotateAngle -= 6
            
        elif "space" in keys and app.autoAIEnabled == True:
            for gap in gaps:
                if gap.centerX-25 < c.centerX < gap.centerX+25:
                    c.centerX += 6
            
def changeDifficulty(direction):
    
    for gap in gaps:
        gap.lineWidth = 50
        gap.visible = True
        vignette.toFront()

    if direction == "up":
        app.index += 1
    elif direction == "down":
        app.index -= 1
        
    app.index %= 4
        
    menuUI["difficultyLabel"].value = app.difficulties[app.index]
        
    if app.index == 0:
        easySound.play(restart = True)
        for gap in gaps:
            gap.lineWidth = 30
        gap4.visible = False
        gap5.visible = False

    elif app.index == 1:
        normalSound.play(restart = True)
        gap5.visible = False
        
    elif app.index == 2:
        hardSound.play(restart = True)
        for gap in gaps:
            gap.lineWidth = 70

    elif app.index == 3:
        app.difficulty = "dynamic"
        dynamicSound.play(restart = True)
        
def onMouseMove(x, y):
    if app.state == "lining2":
        cosmeticLine.x2 = x
        cosmeticLine.y2 = y
        
                
def onMousePress(x, y):
    

    if app.state == "lining1" and c.contains(x, y):
        cosmeticLine.x1 = x
        cosmeticLine.y1 = y
        cosmeticLine.x2 = x
        cosmeticLine.y2 = y
        app.state = "lining2"
        
    elif app.state == "lining2":
        if c.contains(x, y):
            newCosmeticLine = Line(cosmeticLine.x1, cosmeticLine.y1, x, y, fill = 'white', lineWidth = 2)
            cosmetic.add(newCosmeticLine)
            cosmeticLine.x1 = 0
            cosmeticLine.y1 = 0
            cosmeticLine.x2 = 0
            cosmeticLine.y2 = 0
            app.state = "customizing2"
            lineButton.opacity = 100
        else: 
            cosmeticLine.fill = 'red'
            sleep(0.00001)
            cosmeticLine.fill = 'white'
    
    if menuUI["startButton"].hits(x, y):
        if app.state == 'idle':
            app.state = 'starting1'
            music.pause()
            explosion.play()
    
    elif menuUI["leftDifficultyButton"].hits(x, y):
        changeDifficulty("down")
    elif menuUI["rightDifficultyButton"].hits(x, y):
        changeDifficulty("up")
        
    elif pauseButton.hits(x, y):
        if app.state == "ingame":
            app.state = "paused"
            pauseSound.play(restart=True)
        elif app.state == "paused":
            app.state = "ingame"
            unpauseSound.play(restart=True)
            
    elif customButton.hits(x, y):
        if app.state == 'idle':
            app.state = 'customizing1'
            
    elif paintButton.hits(x, y):
        if app.state == 'painting':
            app.state = 'customizing2'
            paintButton.opacity = 100
        elif app.state == 'customizing2':
            app.state = 'painting'
            paintButton.opacity = 50
            
    elif lineButton.hits(x, y):
        if app.state == "customizing2":
            app.state = "lining1"
            lineButton.opacity = 50
        elif app.state == "lining1" or app.state == "lining2":
            app.state = "customizing2"
            lineButton.opacity = 100
            cosmeticLine.x2 = cosmeticLine.x1
            cosmeticLine.y2 = cosmeticLine.y1

def changeScore():
    
    if app.index == 0:
        score.value += 1
    elif app.index == 1:
        score.value += 2
    elif app.index == 2:
        score.value += 4
    elif app.index == 3:
        ### add dynamic score here
        pass
    
def rotateBall(speed):
    c.angle += speed 
    c.centerX = 200 + int(140 * math.cos(math.radians(c.angle)))
    c.centerY = 150 + int(81 * math.sin(math.radians(c.angle)))
    cosmetic.rotateAngle += 6

def onMouseDrag(x, y):
    
    if app.state == "painting" and c.contains(x, y):
        p = Circle(x, y, 1, fill = 'white')
        cosmetic.add(p)
    
    c.fill = rgb(c.red, c.green, c.blue)
    if redBall.hits(x, y) or redBall.touch == True:
        redBall.touch = True
        if 75 <= x <= 150 and redBall.touch == True:
            redBall.centerX = x
            c.red = (redBall.centerX - 75) * 3.4
            
            
    elif greenBall.hits(x, y) or greenBall.touch == True:
        greenBall.touch = True
        if 75 <= x <= 150 and greenBall.touch == True:
            greenBall.centerX = x
            c.green = (greenBall.centerX - 75) * 3.4
            
    elif blueBall.hits(x, y) or blueBall.touch == True:
        blueBall.touch = True
        if 75 <= x <= 150 and blueBall.touch == True:
            blueBall.centerX = x
            c.blue = (blueBall.centerX - 75) * 3.4
            
def onMouseRelease(x, y):
    redBall.touch = False
    greenBall.touch = False
    blueBall.touch = False

def moveToSpot(x, y):
    
    c.centerX = int(c.centerX / 5) * 5
    c.centerY = int(c.centerY / 5) * 5
    
    if c.centerX < x:
        c.centerX += 5
    elif c.centerX > x: 
        c.centerX -= 5
        
    if c.centerY < y:
        c.centerY += 5
    elif c.centerY > y:
        c.centerY -= 5

    if cosmetic.rotateAngle != 0:
        cosmetic.rotateAngle += 6

def onStep():
    
    if (c.centerX > 400): 
        c.centerX = 0
    elif (c.centerX < 0):
        c.centerX = 400
    
    c.toFront()
    cosmetic.toFront()
    cosmetic.centerX = c.centerX
    cosmetic.centerY = c.centerY
    cosmeticLine.toFront()
    
    if app.state == "booting":
        
        if c.centerY < 75:
            c.centerY += c.dy
            c.dy += 0.29
        else: 
            rotateBall(2.5)
        
        for name, element in menuUI.items():    
            if (element.opacity < 100)  and not "Button" in name: 
                element.opacity += 1
                if element.opacity == 100:
                    app.state = 'idle'
        
        if customUI.opacity > 0:
            customUI.opacity -= 4
        
    elif app.state == "idle":
        rotateBall(2.5)
        
    elif app.state == "customizing1":
            
        moveToSpot(115, 150)
        
        for name, element in menuUI.items():    
            if (element.opacity > 0)  and not "custom" in name: 
                element.opacity -= 4
                if element.opacity == 0:
                    app.state = 'customizing2'
        customUI.opacity += 4
        
    elif app.state == 'customizing2':
        
        if cosmetic.rotateAngle == 0 and c.centerX == 100 and c.centerY == 250:
            app.state = "customizing3"
            
        moveToSpot(115, 150)

    elif app.state == 'starting1':
    
        rotateBall(2.5)
        
        score.opacity += 4
        
        for name, element in menuUI.items():    
            if (element.opacity > 0)  and not "Button" in name: 
                element.opacity -= 4
                if element.opacity == 0:
                    app.state = 'starting2'
                    
    elif app.state == 'starting2':
        
        if c.centerX > 200:
            rotateBall(4)
        else:
            rotateBall(2.5)
        if  190 < c.centerX < 200 and c.centerY < 200:
            app.state = "starting3"

    elif app.state == "starting3":
        
        c.centerY += c.dy
        c.dy += 0.29
        if c.hitsShape(baseRect):
            c.dy = -10.5
            bounceSound.play()
            app.state = "starting4"
            
    elif app.state == "starting4":
        c.centerY += c.dy
        c.dy += 0.29
        if c.centerY < 200:
            app.state = "ingame"

    elif app.state == "ingame":
        
        if (pauseUI.opacity > 0):
            pauseUI.opacity -= 2
            
        if score.animation == 1:
            score.angle += 2
            score.size = 20 + abs(int(60 * math.sin(math.radians(score.angle))))
            if c.centerY < 75:
                score.angle = 0
                score.animation = 0
    
        for name, element in menuUI.items():    
            if (element.opacity > 0)  and not (name == 'leftDifficulty') and not (name == 'rightDifficulty') and not (name == 'startButton'): 
                element.opacity -= 2
        
        if ((c.hitsShape(baseRect)) and not (c.hitsShape(gap1)) and not (c.hitsShape(gap2)) and not (c.hitsShape(gap3)) and not (c.hitsShape(gap4)) and not (c.hitsShape(gap5))):
            
            c.dy = -10.5
            bounceSound.play()
            changeScore()
            score.animation = 1
            changeGaps("close")
            
        cornerGapDistance = 0
        
        if (c.hitsShape(gap1)) or (c.hitsShape(gap2)) or (c.hitsShape(gap3)) or (c.hitsShape(gap4)) or (c.hitsShape(gap5)):
            gapWidth = gap1.lineWidth / 2

            for gap in gaps:
                if gap.centerX - gapWidth <= c.left <= gap.centerX + gapWidth:
                    c.leftHitsGap = True
                    cornerGapDistance = c.right - gap.centerX
                if gap.centerX - gapWidth <= c.right <= gap.centerX + gapWidth:
                    c.rightHitsGap = True
                    cornerGapDistance = gap.centerX - c.left
            

            if c.rightHitsGap == True and c.leftHitsGap == True:    
                c.rightHitsGap = False
                c.leftHitsGap = False
                app.state = "lose"
                
            else: 
                c.dy = -10.5
                cornerSound.play()
                changeScore()
                score.animation = 1
                changeGaps("close")
                if (c.leftHitsGap == False and c.rightHitsGap == True):
                    c.dx = 4
                
                elif (c.leftHitsGap == True and c.rightHitsGap == False):
                    c.dx = -4
            
        c.centerY += c.dy
        c.dy += 0.29
        c.centerX += c.dx
        if c.dx > 0:
            c.dx -= 0.05
        elif c.dx < 0:
            c.dx += 0.05

        if (app.opening == True):
        
            if (gap1.y2 < 400):
                for gap in gaps:
                    if gap.visible == True:
                        gap.y2 += 10
                    
        elif (app.opening == False):
            
            if  (gap1.y2 > 250):
                for gap in gaps:
                    gap.y2 -= 10
            else:
                changeGaps("open")
    
    elif app.state == 'lose':
        
        if (pauseUI.opacity > 0):
            pauseUI.opacity -= 2
        
        c.centerY += c.dy
        c.dy += 0.29

        if 340 < c.centerY < 380:
            loseSound.play()
            
        elif (c.top > 12000):
            if (vignette.opacity < 100):
                vignette.opacity += 2
            else:
                for gap in gaps: 
                    gap.y1 = 250
                    gap.fill = 'black'
                    gap.y2 = 250
                baseRect.top = 250
                baseRect.height = 150
                c.centerX = 200
                c.centerY = -25
                c.dy = 8
                app.background = 'black'
                app.bgColorCounter = 0
                    
                app.state = 'reseting'

        elif (c.top > 400):
            
            if (app.background != rgb(210, 0, 0)):
                app.bgColorCounter += 5
                app.background = rgb(app.bgColorCounter, 0, 0)
                for gap in gaps:
                    gap.fill = rgb(app.bgColorCounter, 0, 0)
                    gap.y1 -= c.dy
                baseRect.top -= c.dy
                baseRect.height += c.dy
                    
    elif app.state == 'reseting':
        
        c.dx = 0
        score.value = 0
        if (vignette.opacity > 0):
            vignette.opacity -= 2
        else:
            app.state = 'starting3'
            
    elif app.state == "paused":
    
        if (pauseUI.opacity < 100):
                pauseUI.opacity += 2
                
    if cosmetic.rotateAngle == 360:
        cosmetic.rotateAngle = 0        
