import pygame
import sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
from datetime import datetime

from models.base_tower import draw_base_tower
from models.bench import draw_bench
from models.city_buildings import draw_city_buildings
from models.clock import draw_clock_face
from models.sky import draw_sky
from models.tree import draw_tree
from setup.lightning import setup_lighting

# Initialize 3D objects
def init_objects():
    global animation_time
    global road_list, tree_list, bench_list, base_tower_list, building_list
    animation_time = 0
    road_list = glGenLists(1)
    tree_list = glGenLists(1)
    bench_list = glGenLists(1)
    base_tower_list = glGenLists(1)
    building_list = glGenLists(1)



    # Compile Trees
    glNewList(tree_list, GL_COMPILE)
    draw_tree()
    glEndList()

    # Compile Benches
    glNewList(bench_list, GL_COMPILE)
    draw_bench()
    glEndList()

    # Compile Clock Tower base
    glNewList(base_tower_list, GL_COMPILE)
    draw_base_tower()
    glEndList()

    # Compile Buildings
    glNewList(building_list, GL_COMPILE)
    draw_city_buildings()
    glEndList()

def main():
    pygame.init()
    display = (1280, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Clock Tower in City Environment")

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, -1.0, -10.0)
    glEnable(GL_DEPTH_TEST)

    setup_lighting()
    init_objects()

    clock = pygame.time.Clock()
    mouse_drag = False
    last_mouse_pos = (0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_drag = True
                    last_mouse_pos = event.pos
                elif event.button == 4:
                    glTranslatef(0, 0, 1.0)
                elif event.button == 5:
                    glTranslatef(0, 0, -1.0)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse_drag = False

            if event.type == pygame.MOUSEMOTION and mouse_drag:
                dx, dy = event.pos[0] - last_mouse_pos[0], event.pos[1] - last_mouse_pos[1]
                last_mouse_pos = event.pos
                glRotatef(dx, 0, 1, 0)
                glRotatef(dy, 1, 0, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Draw sky background
        

        draw_sky()

        # Draw ground
        glColor3f(0.3, 0.6, 0.3)  # Green ground
        glBegin(GL_QUADS)
        glVertex3f(-10, -0.01, -10)
        glVertex3f(10, -0.01, -10)
        glVertex3f(10, -0.01, 10)
        glVertex3f(-10, -0.01, 10)
        glEnd()

        # Draw city elements
        glCallList(road_list)
        glCallList(building_list)
        glCallList(base_tower_list)

        # Draw clock faces on all 4 sides of the tower
        for i in range(4):
            glPushMatrix()
            glRotatef(90 * i, 0, 1, 0)
            glTranslatef(0, 0.8, 0.31)
            draw_clock_face()
            glPopMatrix()

        # Place trees around the scene
        for angle in range(0, 360, 45):
            glPushMatrix()
            glRotatef(angle, 0, 1, 0)
            glTranslatef(3.0, 0, 0)
            glCallList(tree_list)
            glPopMatrix()

        # Place benches around the scene
        for angle in range(0, 360, 90):
            glPushMatrix()
            glRotatef(angle + 45, 0, 1, 0)
            glTranslatef(1.5, 0, 0)
            glCallList(bench_list)
            glPopMatrix()

      

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()