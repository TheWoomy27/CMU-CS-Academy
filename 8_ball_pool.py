import math

app.background = 'steelBlue'

collide_sound = Sound("cmu://584498/30779725/collide.MP3")
strike_sound = Sound("cmu://584498/30779731/big_strike.MP3")
switch_players_sound = Sound("cmu://584498/30779734/switch_players.MP3")
bank_sound = Sound("cmu://584498/30779776/bank.MP3")
pot_sound = Sound("cmu://584498/30779787/pot.mp3")

# Corners
Rect(10, 85, 27, 27, fill = gradient("dimGray","dimGray", "white")),
Rect(10, 287, 27, 27, fill = gradient("dimGray","dimGray", "white")),
Rect(362, 85, 27, 27, fill = gradient("dimGray","dimGray", "white")),
Rect(362, 287, 27, 27, fill = gradient("dimGray","dimGray", "white")),

base = Rect(25, 100, 350, 200, fill = gradient('forestGreen', "green", 'darkGreen'))
    
# Wood
Rect(37, 85, 325, 15, fill = gradient('saddleBrown','saddleBrown', "sienna", start = "bottom")),
Rect(37, 300, 325, 15, fill = gradient('saddleBrown','saddleBrown', "sienna", start = "top")),
Rect(10, 112, 15, 175, fill = gradient('saddleBrown','saddleBrown', "sienna", start = "right")),
Rect(375, 112, 15, 175, fill = gradient('saddleBrown','saddleBrown', "sienna", start = "left")),

# Holes
holes = [    
    Circle(25, 100, 12, fill = gradient("brown", "black", "black", start = "left-top")),
    Circle(200, 95, 10, fill = gradient("brown", "black", "black", start = "top")),
    Circle(375, 100, 12, fill = gradient("brown", "black", "black", start = "right-top")),
    Circle(25, 300, 12, fill = gradient("brown", "black", "black", start = "left-bottom")),
    Circle(200, 304, 10, fill = gradient("brown", "black", "black", start = "bottom")),
    Circle(375, 300, 12, fill = gradient("brown", "black", "black", start = "right-bottom")),
    ]

# Rim
app.horizontal_rims = [
    Polygon(37, 100, 40, 105, 185, 105, 190, 100, fill = "green", border="white", borderWidth = 0.5),
    Polygon(210, 100, 215, 105, 359, 105, 362, 100, fill = "green", border="white", borderWidth = 0.5),
    Polygon(37, 300, 40, 295, 185, 295, 190, 300, fill = "green", border="white", borderWidth = 0.5),
    Polygon(210, 300, 215, 295, 359, 295, 362, 300, fill = "green", border="white", borderWidth = 0.5),
    ]
    
app.vertical_rims = [Polygon(25, 112, 30, 117, 30, 284, 25, 287, fill = "green", border="white", borderWidth = 0.5),
    Polygon(375, 112, 370, 117, 370, 284, 375, 287, fill = "green", border="white", borderWidth = 0.5)]    
    
cue_ball = Circle(100, 200, 5, fill = "white", border = "black", borderWidth = 0.5)
cue_ball.v = [0, 0]

cue = Line(90, 200, -25, 200, fill = "khaki", lineWidth = 4) 

eight_ball = Circle(300, 200, 5, fill = "black")
eight_ball.v = [0, 0]

red_balls = [Circle(310, 195, 5, fill = "red", border = "black", borderWidth = 0.5), 
            Circle(310, 205, 5, fill = "red", border = "black", borderWidth = 0.5),
            Circle(320, 200, 5, fill = "red", border = "black", borderWidth = 0.5),
            Circle(320, 190, 5, fill = "red", border = "black", borderWidth = 0.5),
            Circle(300, 190, 5, fill = "red", border = "black", borderWidth = 0.5),
            Circle(290, 195, 5, fill = "red", border = "black", borderWidth = 0.5),
            Circle(300, 210, 5, fill = "red", border = "black", borderWidth = 0.5)
            ]
            
yellow_balls = [Circle(310, 185, 5, fill = "gold", border = "black", borderWidth = 0.5), 
            Circle(310, 215, 5, fill = "gold", border = "black", borderWidth = 0.5),
            Circle(320, 210, 5, fill = "gold", border = "black", borderWidth = 0.5),
            Circle(320, 180, 5, fill = "gold", border = "black", borderWidth = 0.5),
            Circle(320, 220, 5, fill = "gold", border = "black", borderWidth = 0.5),
            Circle(290, 205, 5, fill = "gold", border = "black", borderWidth = 0.5),
            Circle(280, 200, 5, fill = "gold", border = "black", borderWidth = 0.5)
            ]
            
balls = [cue_ball, eight_ball]

for ball in red_balls: 
    ball.v = [0, 0]
    balls.append(ball)
for ball in yellow_balls: 
    ball.v = [0, 0]
    balls.append(ball)

cue_guideline = Line(102, 200, 288, 200, fill = "white", lineWidth = 1.5)
cue_guideline.length = 200
cue_guideline.newx = 0
cue_guideline.newy = 0
cue_guideline.dx = 0
cue_guideline.dy = 0

cue_guideline_angle = Line(cue_guideline.x2, cue_guideline.y2, cue_guideline.x2, cue_guideline.y2, fill = "white", lineWidth = 1.5)
cue_guideline_angle.dx = 0
cue_guideline_angle.dy = 0

cue_guideline_circle = Circle(288, 200, 5, fill = None, border = "white")
cue_guideline_circle.newx = 0
cue_guideline_circle.newy = 0

app.mouseX = 0
app.mouseY = 0

app.stepsPerSecond = 60

Rect(95, 45, 210, 10, fill = "dimgrey", border ="white", borderWidth = 1)

cue_power_scale = Rect(96, 46, 208, 8, fill = gradient("red", "orange", "yellow", start = "left"), opacity = 0)

power_cue = Line(100, 50, 300, 50, fill = "khaki", lineWidth = 4)
power_cue_hitbox = Rect(90, 40, 220, 20, opacity = 0)

def onMouseMove(x, y):
    app.mouseX = x
    app.mouseY = y

app.isMovingBall = False
app.isGoingToHit = False
def onMousePress(x, y):
    
    if power_cue_hitbox.hits(x, y):
        app.isGoingToHit = True
    if cue_ball.hits(x, y) and app.ballInHand:
        app.isMovingBall = True
        cue.visible = False
        cue_guideline_circle.visible = False
        cue_guideline.visible = False
        
app.power = 0
app.endTurn = True
def onMouseRelease(x, y):
    
    app.isMovingBall = False
    
    if app.isGoingToHit:
        app.isGoingToHit = False
        
        if power_cue.right < 300:
            app.power = 300 - power_cue.right
            app.power /= 20
            cue_ball.v[0] = cue_guideline.dx * app.power
            cue_ball.v[1] = cue_guideline.dy * app.power
            cue.visible = False
            cue_guideline.visible = False
            cue_guideline_circle.visible = False
            strike_sound.play()
            app.endTurn = False
            app.ballInHand = False
            app.startingBallInHand = False
            
    else: 
        cue.x1 = cue_ball.centerX + cue_guideline.dx * -10
        cue.y1 = cue_ball.centerY + cue_guideline.dy * -10
        cue.x2 = cue_ball.centerX + cue_guideline.dx * -150
        cue.y2 = cue_ball.centerY + cue_guideline.dy * -150
        cue.visible = True
        cue_guideline_circle.visible = True
        cue_guideline.visible = True
            
    power_cue.right = 300
    power_cue_hitbox.right = 310

    cue_power_scale.opacity = 0

app.ballInHand = True
app.startingBallInHand = True
def onMouseDrag(x, y):
    
    previousX = x
    previousY = y
    
    direction_x = x - app.mouseX
    direction_y = y - app.mouseY
    
    # Calculate distance moved
    distance = ((x - app.mouseX)**2 + (y - app.mouseY)**2)**0.5
  
    if app.isGoingToHit:
        power_cue.right = x
        power_cue_hitbox.right = x + 10
        
        cue.x1 = cue_ball.centerX + cue_guideline.dx * (-10 - (300 - power_cue.right))
        cue.y1 = cue_ball.centerY + cue_guideline.dy * (-10 - (300 - power_cue.right))
        cue.x2 = cue_ball.centerX + cue_guideline.dx * (-150 - (300 - power_cue.right))
        cue.y2 = cue_ball.centerY + cue_guideline.dy * (-150 - (300 - power_cue.right))
        
        opacity = math.floor(300 - power_cue.right) / 2
        while opacity > 100:
            opacity -= 1
        while opacity < 0:
            opacity += 1
        
        cue_power_scale.opacity = opacity
        
    if app.isGoingToHit == False and app.isMovingBall == False:        
        cue_guideline.dx = x - cue_ball.centerX
        cue_guideline.dy = y - cue_ball.centerY
        length = math.sqrt(cue_guideline.dx ** 2 + cue_guideline.dy ** 2)
        if length != 0:
            cue_guideline.dx /= length
            cue_guideline.dy /= length
        
        cue.x1 = cue_ball.centerX + cue_guideline.dx * -10
        cue.y1 = cue_ball.centerY + cue_guideline.dy * -10
        cue.x2 = cue_ball.centerX + cue_guideline.dx * -150
        cue.y2 = cue_ball.centerY + cue_guideline.dy * -150
      
    # Update previous position and time
    app.mouseX, app.mouseY = x, y
    
    if power_cue.right > 300:
        power_cue.right = 300
        power_cue_hitbox.right = 310
        cue.x1 = cue_ball.centerX + cue_guideline.dx * -10
        cue.y1 = cue_ball.centerY + cue_guideline.dy * -10
        cue.x2 = cue_ball.centerX + cue_guideline.dx * -150 
        cue.y2 = cue_ball.centerY + cue_guideline.dy * -150
    if power_cue.right < 100:
        power_cue.right = 100
        power_cue_hitbox.right = 110
        cue.x1 = cue_ball.centerX + cue_guideline.dx * -210
        cue.y1 = cue_ball.centerY + cue_guideline.dy * -210
        cue.x2 = cue_ball.centerX + cue_guideline.dx * -350 
        cue.y2 = cue_ball.centerY + cue_guideline.dy * -350
    
def onStep():
    
    if app.ballInHand and app.isMovingBall:
        cue_ball.centerX, cue_ball.centerY = app.mouseX, app.mouseY
        if cue_ball.left < 30: cue_ball.left = 30
        if cue_ball.top < 105: cue_ball.top = 105
        if cue_ball.bottom > 295: cue_ball.bottom = 295
        if cue_ball.right > 370: cue_ball.right = 370
        
        if app.startingBallInHand and cue_ball.right > 100:
            cue_ball.right = 100
            
    balls.sort(key=lambda ball: ball.centerX)

    active_balls = []

    for ball in balls:
        
        for hole in holes:
            if hole.hits(ball.centerX, ball.centerY):
                balls.remove(ball)
                pot_sound.play()
        
        # Remove ballects that are no longer in the active interval
        active_balls = [active_ball for active_ball in active_balls if active_ball.right > ball.left]

        # Check for collisions with active ballects
        for active_ball in active_balls:
            if ball.hitsShape(active_ball):
                ball2 = active_ball
                if ball.v[0] <= 0.005 and ball2.v[0] <= 0.005 and ball.v[1] <= 0.005 and ball2.v[1] <= 0.005:   pass
                else: collide_sound.play()
                # Calculate collision normal
                collision_normal = [ball2.centerX - ball.centerX, ball2.centerY - ball.centerY]
                magnitude = (collision_normal[0]**2 + collision_normal[1]**2)**0.5
                collision_normal = [collision_normal[0] / magnitude, collision_normal[1] / magnitude]

                # Calculate relative velocity
                relative_velocity = [ball2.v[0] - ball.v[0], ball2.v[1] - ball.v[1]]

                # Calculate relative velocity in terms of the normal direction
                vel_along_normal = relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1]

                # Do not resolve if velocities are separating
                if vel_along_normal > 0:
                    continue

                # Calculate restitution
                e = 1

                # Calculate impulse scalar
                j = -(1 + e) * vel_along_normal
                j /= (1 / ball.radius + 1 / ball2.radius)

                # Apply impulse to balls
                impulse = [collision_normal[0] * j, collision_normal[1] * j]
                ball.v[0] -= impulse[0] / ball.radius
                ball.v[1] -= impulse[1] / ball.radius
                ball2.v[0] += impulse[0] / ball2.radius
                ball2.v[1] += impulse[1] / ball2.radius

        # Add the current ballect to the active interval
        active_balls.append(ball)

    for ball in balls:
        
        ball.centerX += float(ball.v[0])
        ball.centerY += float(ball.v[1])

        ball.v[0] *= 0.985
        ball.v[1] *= 0.985
    
        for rim in app.horizontal_rims:
            if ball.hitsShape(rim):
                ball.v[1] *= -1
                bank_sound.play()
        
        for rim in app.vertical_rims:
            if ball.hitsShape(rim):
                ball.v[0] *= -1
                bank_sound.play()

    if app.endTurn == False:    
        for ball in balls:
            if abs(ball.v[0]) > 0.0025 and abs(ball.v[1]) > 0.0025: break
            if ball == balls[len(balls)-1] and app.endTurn == False: 
                if cue_ball not in balls:
                    cue_ball.centerX = 100
                    cue_ball.centerY = 200
                    cue_ball.v = [0, 0]
                    balls.append(cue_ball)
                    app.ballInHand = True
                app.endTurn = True
                switch_players_sound.play()
                cue_guideline.visible = True
                cue_guideline_circle.visible = True 
                cue.visible = True
                cue.x1 = cue_ball.centerX + cue_guideline.dx * -10
                cue.y1 = cue_ball.centerY + cue_guideline.dy * -10
                cue.x2 = cue_ball.centerX + cue_guideline.dx * -150
                cue.y2 = cue_ball.centerY + cue_guideline.dy * -150
    
    cue_guideline.x1 = cue_ball.centerX
    cue_guideline.y1 = cue_ball.centerY
    
    cue_guideline_circle.centerX = cue_guideline.x2
    cue_guideline_circle.centerY = cue_guideline.y2
    
    cue_guideline_angle.x1 = cue_guideline_circle.centerX
    cue_guideline_angle.y1 = cue_guideline_circle.centerY
    
    cue_guideline.x2 = (cue_ball.centerX + cue_guideline.dx * 25.5 + cue_guideline.dx * cue_guideline.length)
    cue_guideline.y2 = (cue_ball.centerY + cue_guideline.dy * 25.5 + cue_guideline.dy * cue_guideline.length)
    
    if app.endTurn == True:
        while 30 > cue_guideline.x2 or 370 < cue_guideline.x2 or 105 > cue_guideline.y2 or 295 < cue_guideline.y2:
            cue_guideline.length -= 1
            cue_guideline.x2 = (cue_ball.centerX + cue_guideline.dx * 25.5 + cue_guideline.dx * cue_guideline.length)
            cue_guideline.y2 = (cue_ball.centerY + cue_guideline.dy * 25.5 + cue_guideline.dy * cue_guideline.length)
            cue_guideline_circle.centerX = cue_guideline.x2
            cue_guideline_circle.centerY = cue_guideline.y2
            
        else:
            cue_guideline.length = 300
    
        for ball in balls: if ball != cue_ball:
            if cue_guideline_circle.hitsShape(ball):
                
                cue_guideline_angle.visible = True
                
                collision_normal = [cue_guideline_circle.centerX - ball.centerX, cue_guideline_circle.centerY - ball.centerY]
                magnitude = (collision_normal[0]**2 + collision_normal[1]**2)**0.5
                collision_normal = [collision_normal[0] / magnitude, collision_normal[1] / magnitude]

                # Calculate relative velocity
                relative_velocity = [5, 5]

                # Calculate relative velocity in terms of the normal direction
                vel_along_normal = relative_velocity[0] * collision_normal[0] + relative_velocity[1] * collision_normal[1]

                # Do not resolve if velocities are separating
                if vel_along_normal > 0:
                    continue

                # Calculate restitution
                e = 1

                # Calculate impulse scalar
                j = -(1 + e) * vel_along_normal
                j /= (1 / ball.radius + 1 / cue_ball.radius)

                # Apply impulse to balls
                impulse = [collision_normal[0] * j, collision_normal[1] * j]
                
                
                cue_guideline_angle.x2 = cue_guideline_circle.centerX - (impulse[0])
                cue_guideline_angle.y2 = cue_guideline_circle.centerY - (impulse[1])
                
            while cue_guideline.hitsShape(ball):
                cue_guideline.length -= 1
                cue_guideline.x2 = (cue_ball.centerX + cue_guideline.dx * 25.5 + cue_guideline.dx * cue_guideline.length)
                cue_guideline.y2 = (cue_ball.centerY + cue_guideline.dy * 25.5 + cue_guideline.dy * cue_guideline.length)
                cue_guideline_circle.centerX = cue_guideline.x2
                cue_guideline_circle.centerY = cue_guideline.y2
