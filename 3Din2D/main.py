# ===============================================================================
# @File:   main.py (3Din2D)
# @Brief:  Implementing 3D rendering in python
# @Author: Tejas
# @Date:   2026-09-22 Tue
# @Notice: This is how games will render 3D graphics even though the screen is 2D.
# ===============================================================================

# DISCLAIMER(Tejas): This will seem very complicated if you havent done any graphics programming before.
# But this is essentially how 3D graphics are rendered in games. The idea is to
# take a 3D point and project it onto a 2D screen. This is done by using some
# trignometry and some linear algebra. The code is not optimized for performance
# but it should give you a good idea of how 3D graphics are rendered in games.

# NOTE(Tejas): we could implement this using terminal but I think it looks
# better if we use a proper GUI window and plus this would be a great
# introduction to graphics programming
import pygame

# NOTE(Tejas): we are going to use some trignometry to rotate things
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

FPS = 60.0

# NOTE(Tejas): this is a what we implemented in the lecture on OOP. Try to use
# it define a Rect and do a draw call on it. Keep in mind that in maths the x: 0
# and y: 0 is at the bottom left but usually in graphics applications the 
# x: 0 and y: 0 is at the top left. 
class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self, screen, color):
        start_x = round(self.x)
        start_y = round(self.y)
        end_x = round(self.x + self.w)
        end_y = round(self.y + self.h)
        for x in range(start_x, end_x):
            for y in range(start_y, end_y):
                screen.set_at((x, y), color)


# NOTE(Tejas): This is might seem like a complex idea but its very common in
# graphics programming.  As I mentioned above our 0, 0 starts at the top left
# and goes on for SCREEN_WIDTH and SCREEN_HEIGHT. But this point is in 3D space
# and the 0,0 starts at the center of the screen, no where in the code it says
# this but since this is our data we can make stuff however we want.
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def draw(self, screen, color):

        # NOTE(Tejas): for now our point is going to be a square of size 5x5
        size = 20
        
        # NOTE(Tejas): Pygame has a built in function to draw a rectangle but
        # since we defined our own Rect we'll use it

        projected_point = self.project()
        if projected_point is None:
            return

        screen_coords = projected_point.to_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
        rect_point = Rect(screen_coords.x - size / 2, screen_coords.y - size / 2, size, size)

        rect_point.draw(screen, color)

    def to_screen(self, screen_width, screen_height):

        # NOTE(Tejas): As I said we represent our point so that the center is at
        # 0,0 but we have to convert it to screen space where 0,0 is at the top
        # left so that pygame can render it properly
        screen_x = (self.x + 1.0) / 2.0 * screen_width
        screen_y = (1.0 - (self.y + 1) / 2.0) * screen_height

        return Point(screen_x, screen_y, self.z)

    def project(self):
        # NOTE(Tejas): here we'll use the Z value to determine how far or near the point is from the camera.
        # this is to make it look 3D
        if self.z <= 0:
            return None
        return Point(self.x / self.z, self.y / self.z, self.z)

    def translate_z(self, dz):
        # NOTE(Tejas): translate_z means modify the z value by dz.
        return Point(self.x, self.y, self.z + dz)

    def rotate_y(self, angle):

        # NOTE(Tejas): this is a know formula to rotate a point around the y
        # axis. Google it! (formula to rotate a point around the y axis)
        cos_angle = math.cos(angle)
        sin_angle = math.sin(angle)

        new_x = self.x * cos_angle - self.z * sin_angle
        new_z = self.x * sin_angle + self.z * cos_angle

        return Point(new_x, self.y, new_z)

# NOTE(Tejas): This is a helper function that will take in 2 Points and draw a
# line between them.
def draw_line(screen, p1, p2, color):

    p1_projected = p1.project()
    p2_projected = p2.project()

    if p1_projected is None or p2_projected is None:
        return

    p1_screen = p1_projected.to_screen(SCREEN_WIDTH, SCREEN_HEIGHT)
    p2_screen = p2_projected.to_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

    pygame.draw.line(screen, color, (p1_screen.x, p1_screen.y), (p2_screen.x, p2_screen.y), 3)

def main():

    # NOTE(Tejas): since python is interpreted you dont actually have to do this
    # def main() facade, but since I have programmed C this is the best way I
    # can keep track of what is happening. The choise is yours...

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("3D in 2D")

    clock = pygame.time.Clock()

    # NOTE(Tejas): now this is a fully functional 3D renderer in python. if you
    # want you can paste the above points and faces list to ChatGPT and ask it
    # to generate a 3D model of a house in the same format, and then paste that
    # code right here and you will have a 3D rotating house!!!
    # make sure to paste the code below this line so it gets overriden and used.
    # or you can delete the above points and faces list and paste the new one!
    points = [
        # Body - bottom
        Point(-0.30, -0.60, -0.20),  # 0
        Point(+0.30, -0.60, -0.20),  # 1
        Point(+0.30, -0.60, +0.20),  # 2
        Point(-0.30, -0.60, +0.20),  # 3
        
        # Body - shoulders
        Point(-0.35, +0.20, -0.20),  # 4
        Point(+0.35, +0.20, -0.20),  # 5
        Point(+0.35, +0.20, +0.20),  # 6
        Point(-0.35, +0.20, +0.20),  # 7
        
        # Head
        Point(-0.28, +0.45, -0.20),  # 8
        Point(+0.28, +0.45, -0.20),  # 9
        Point(+0.28, +0.45, +0.20),  # 10
        Point(-0.28, +0.45, +0.20),  # 11
        
        # Top of head
        Point(-0.20, +0.75, -0.15),  # 12
        Point(+0.20, +0.75, -0.15),  # 13
        Point(+0.20, +0.75, +0.15),  # 14
        Point(-0.20, +0.75, +0.15),  # 15
        
        # Beak
        Point(-0.08, +0.52, -0.20),   # 16
        Point(+0.08, +0.52, -0.20),   # 17
        Point(0.0, +0.43, -0.40),     # 18
        
        # Left wing
        Point(-0.35, +0.15, -0.15),   # 19
        Point(-0.55, -0.05, -0.15),   # 20
        Point(-0.45, -0.45, -0.15),   # 21
        Point(-0.25, -0.30, -0.15),   # 22
        
        # Right wing
        Point(+0.35, +0.15, -0.15),   # 23
        Point(+0.55, -0.05, -0.15),   # 24
        Point(+0.45, -0.45, -0.15),   # 25
        Point(+0.25, -0.30, -0.15),   # 26
        
        # Left foot
        Point(-0.30, -0.60, -0.20),   # 27
        Point(-0.05, -0.60, -0.20),   # 28
        Point(-0.05, -0.68, -0.45),   # 29
        Point(-0.35, -0.68, -0.45),   # 30
        
        # Right foot
        Point(+0.05, -0.60, -0.20),   # 31
        Point(+0.30, -0.60, -0.20),   # 32
        Point(+0.35, -0.68, -0.45),   # 33
        Point(+0.05, -0.68, -0.45),   # 34
    ]
    
    # NOTE(Tejas): These tell us which points to connect
    # to make the penguin.
    faces = [
        # Body
        [0, 1, 5, 4],
        [1, 2, 6, 5],
        [2, 3, 7, 6],
        [3, 0, 4, 7],
        
        # Head
        [8, 9, 13, 12],
        [9, 10, 14, 13],
        [10, 11, 15, 14],
        [11, 8, 12, 15],
        
        # Head to body
        [4, 5],
        [5, 9],
        [9, 8],
        [8, 4],
        
        # Top of head
        [12, 13],
        [13, 14],
        [14, 15],
        [15, 12],
        
        # Beak
        [16, 17],
        [16, 18],
        [17, 18],
        
        # Left wing
        [19, 20],
        [20, 21],
        [21, 22],
        [22, 19],
        
        # Right wing
        [23, 24],
        [24, 25],
        [25, 26],
        [26, 23],
        
        # Left foot
        [27, 28],
        [28, 29],
        [29, 30],
        [30, 27],
        
        # Right foot
        [31, 32],
        [32, 33],
        [33, 34],
        [34, 31],
    ]



    # NOTE(Tejas): this is the speed at which the cube will rotate. The angle is
    # in radians and we are rotating it at 90 degrees per second. You can adjust
    # this to make the cube go fast or slow.
    rotation_speed = math.pi
    angle = 0.0

    dz = 1.0
    z_offset = 1.0

    running = True
    while running:

        delta_time = 1.0 / FPS
        angle += rotation_speed * delta_time
        z_offset += dz * delta_time

        transformed_points = []

        # NOTE(Tejas): here we are translating (meaning changing) the z value of
        # the point so that it moves away from us (the camera). And we are also
        # rotating the point around its y axis so that it looks like the cube is
        # rotating. 
        for point in points:
            rotated_point = point.rotate_y(angle)
            translated_point = rotated_point.translate_z(z_offset)
            transformed_points.append(translated_point)

        # NOTE(Tejas): here we process all the input that the window has
        # received: like mouse clicks, key presses, window related things like
        # closing window etc
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # NOTE(Tejas): clear the screen. if you are using VS Code you can hover
        # over any function to see its details
        screen.fill((0, 0, 0)) # NOTE(Tejas): Clearing to black

        # NOTE(Tejas): Uncomment this to see the points of the cube.
        # for point in transformed_points:
        #     point.draw(screen, (255, 255, 255))

        for face in faces:
            for i in range(len(face)):
                p1 = transformed_points[face[i]]
                p2 = transformed_points[face[(i + 1) % len(face)]]
                draw_line(screen, p1, p2, (0, 0, 255))

        # NOTE(Tejas): look up double buffering on the internet if you dont
        # understand what this is.
        pygame.display.flip() 

        # NOTE(Tejas): we'll hard code the FPS to be 60.
        clock.tick(FPS) 

    pygame.quit()

if __name__ == "__main__":
    main()

