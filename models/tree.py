from models._index import *
from models.sphere import draw_sphere

def draw_tree():
      # Trunk
    glColor3f(0.5, 0.3, 0.1)
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)  # Make cylinder stand up
    draw_cylinder(0.1, 1.0)
    glPopMatrix()

    # Leaves
    glPushMatrix()
    glTranslatef(0, 0.8, 0)
    glColor3f(0.0, 0.5, 0.0)
    draw_sphere(0.5)
    glPopMatrix()

def draw_cylinder(radius, height, slices=32):
    quad = gluNewQuadric()
    gluQuadricNormals(quad, GLU_SMOOTH)
    gluCylinder(quad, radius, radius, height, slices, 1)
    gluDeleteQuadric(quad)

