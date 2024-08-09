import numpy as np
from cmu_graphics import *

app.background = "black"

bounceSound = Sound("https://studio.code.org/api/v1/sound-library/category_app/snap.mp3")

particles = []
for i in range(2):
    p = Circle(150+ i*55,150+ i*55, 20 + i* 5, fill = "white")
    p.vx = i + 0.5
    p.vy = i + 1
    p.v = [p.vx, p.vy]
    p.pos = [p.centerX, p.centerY]
    particles.append(p)
    
boundary  = Rect(100, 100, 200, 200, fill = None, border = "white")
    
app.stepsPerSecond = 60
def onStep():

    for i in range(len(particles)):
        p = particles[i]
        for j in range(i+1, len(particles)):
            p2 = particles[j]

            if p.hitsShape(p2):
                bounceSound.play(restart=True)
                # Calculate collision normal
                collision_normal = np.array([p2.centerX - p.centerX, p2.centerY - p.centerY])
                collision_normal = collision_normal.astype(float) / np.linalg.norm(collision_normal)

                # Calculate relative velocity
                relative_velocity = np.array([p2.v[0] - p.v[0], p2.v[1] - p.v[1]])

                # Calculate relative velocity in terms of the normal direction
                vel_along_normal = np.dot(relative_velocity, collision_normal)

                # Do not resolve if velocities are separating
                if vel_along_normal > 0:
                    continue

                # Calculate restitution
                e = 1

                # Calculate impulse scalar
                j = -(1 + e) * vel_along_normal
                j /= (1 / p.radius + 1 / p2.radius)

                # Apply impulse to particles
                impulse = collision_normal * j
                p.v -= (impulse / p.radius)
                p2.v += (impulse / p2.radius)

    for p in particles:
        p.centerX += rounded(p.v[0])
        p.centerY += rounded(p.v[1])

        p.v[1] += 0.04125  # Add a gravity-like effect

        # Handle boundary collisions
        if p.left <= boundary.left:
            p.v[0] = abs(p.v[0])  # Reflect X velocity
            p.left = boundary.left
            bounceSound.play(restart=True)
        if p.right >= boundary.right:
            p.v[0] = -abs(p.v[0])  # Reflect X velocity
            p.right = boundary.right
            bounceSound.play(restart=True)
        if p.bottom >= boundary.bottom:
            p.v[1] = -abs(p.v[1])  # Reflect Y velocity
            p.bottom = boundary.bottom
            bounceSound.play(restart=True)
        if p.top <= boundary.top:
            p.v[1] = abs(p.v[1])  # Reflect Y velocity
            p.top = boundary.top
            bounceSound.play(restart=True)

cmu_graphics.run() # type: ignore
