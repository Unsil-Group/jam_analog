from models._index import *
from models.cube import draw_cube

def draw_base_tower():
    # Tower body
    glColor3f(0.76, 0.69, 0.5)  # Sandstone color
    glPushMatrix()
    glScalef(0.6, 2.5, 0.6)  # Tall and narrow
    draw_cube(1.0)
    glPopMatrix()

    # Horizontal decorations
    glColor3f(0.9, 0.75, 0.2)  # Gold color
    for y in [-0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6]:
        glPushMatrix()
        glTranslatef(0, y * 2.5, 0)
        glScalef(0.65, 0.02, 0.65)
        draw_cube(1.0)
        glPopMatrix()

    # Roof (pyramid)
    glColor3f(0.3, 0.3, 0.3)  # Dark gray
    glPushMatrix()
    glTranslatef(0, 1.3, 0)
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0.8, 0)  # Apex
    glVertex3f(-0.4, 0, -0.4)
    glVertex3f(0.4, 0, -0.4)
    glVertex3f(0.4, 0, 0.4)
    glVertex3f(-0.4, 0, 0.4)
    glVertex3f(-0.4, 0, -0.4)
    glEnd()
    glPopMatrix()

    # Roof spire
    glColor3f(0.9, 0.75, 0.2)  # Gold color
    glPushMatrix()
    glTranslatef(0, 2.1, 0)
    glScalef(0.05, 0.3, 0.05)
    draw_cube(1.0)
    glPopMatrix()



    # Straight roads
    glColor3f(0.3, 0.3, 0.3)
    for i in range(4):
        glPushMatrix()
        glRotatef(90 * i, 0, 1, 0)
        glBegin(GL_QUADS)
        glVertex3f(-1.5, 0, -0.5)
        glVertex3f(1.5, 0, -0.5)
        glVertex3f(1.5, 0, 0.5)
        glVertex3f(-1.5, 0, 0.5)
        glEnd()
        glPopMatrix()

  