from models._index import *
from models.cube import draw_cube

def draw_bench():
    # Seat
    glColor3f(0.6, 0.4, 0.2)
    glPushMatrix()
    glScalef(0.8, 0.2, 0.3)
    draw_cube(1.0)
    glPopMatrix()

    # Backrest
    glPushMatrix()
    glTranslatef(0, 0.2, -0.15)
    glScalef(0.8, 0.3, 0.05)
    draw_cube(1.0)
    glPopMatrix()

    # Legs
    for x in [-0.35, 0.35]:
        for z in [-0.1, 0.1]:
            glPushMatrix()
            glTranslatef(x, -0.2, z)
            glScalef(0.05, 0.4, 0.05)
            draw_cube(1.0)
            glPopMatrix()


