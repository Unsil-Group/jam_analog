from models._index import *
from models.cube import draw_cube

def draw_clock_face():
    glPushMatrix()
    
    # Clock face
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(32 + 1):
        angle = 2 * math.pi * i / 32
        glVertex3f(0.4 * math.cos(angle), 0.4 * math.sin(angle), 0)
        glVertex3f(0.38 * math.cos(angle), 0.38 * math.sin(angle), 0)
    glEnd()

    # Hour markers
    glColor3f(0.0, 0.0, 0.0)
    for i in range(12):
        angle = math.radians(i * 30)
        x = 0.35 * math.cos(angle)
        y = 0.35 * math.sin(angle)
        glPushMatrix()
        glTranslatef(x, y, 0)
        glScalef(0.02, 0.02, 0.01)
        draw_cube(1.0)
        glPopMatrix()

    now = datetime.now()
    hour = now.hour % 12
    minute = now.minute
    second = now.second

    # Hour hand
    glPushMatrix()
    glRotatef(-(hour * 30 + minute * 0.5), 0, 0, 1)
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0.2, 0)
    glEnd()
    glPopMatrix()

    # Minute hand
    glPushMatrix()
    glRotatef(-minute * 6, 0, 0, 1)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0.3, 0)
    glEnd()
    glPopMatrix()

    # Second hand
    glPushMatrix()
    glRotatef(-second * 6, 0, 0, 1)
    glColor3f(1.0, 0.0, 0.0)
    glLineWidth(1)
    glBegin(GL_LINES)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0.35, 0)
    glEnd()
    glPopMatrix()

    glPopMatrix()