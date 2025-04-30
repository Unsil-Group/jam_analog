from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import datetime
import math

window_width, window_height = 800, 800


def resize(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)


def draw_background():
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.8, 1.0)
    glVertex2f(-1, 1)
    glVertex2f(1, 1)
    glColor3f(0.7, 0.85, 1.0)
    glVertex2f(1, -1)
    glVertex2f(-1, -1)
    glEnd()


def draw_tower_body():
    glColor3f(0.76, 0.69, 0.5)  # warna bata coklat kekuningan
    glBegin(GL_QUADS)
    glVertex2f(-0.3, -1)
    glVertex2f(0.3, -1)
    glVertex2f(0.3, 0.4)
    glVertex2f(-0.3, 0.4)
    glEnd()

    # Aksen emas horizontal
    glColor3f(0.9, 0.75, 0.2)
    for y in [-0.8, -0.6, -0.4, -0.2, 0.0, 0.2]:
        glBegin(GL_QUADS)
        glVertex2f(-0.3, y)
        glVertex2f(0.3, y)
        glVertex2f(0.3, y + 0.015)
        glVertex2f(-0.3, y + 0.015)
        glEnd()


def draw_roof():
    glColor3f(0.3, 0.3, 0.3)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.35, 0.4)
    glVertex2f(0.35, 0.4)
    glVertex2f(0.0, 0.65)
    glEnd()

    glColor3f(0.9, 0.75, 0.2)
    glBegin(GL_TRIANGLES)
    glVertex2f(-0.03, 0.65)
    glVertex2f(0.03, 0.65)
    glVertex2f(0.0, 0.7)
    glEnd()


def draw_circle(radius, segments=100):
    glBegin(GL_POLYGON)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        glVertex2f(radius * math.cos(angle), radius * math.sin(angle))
    glEnd()


def draw_clock():
    glPushMatrix()
    glTranslatef(0.0, 0.15, 0)

    # Bingkai luar emas
    glColor3f(0.9, 0.75, 0.2)
    draw_circle(0.18)

    # Latar jam putih
    glColor3f(1.0, 1.0, 1.0)
    draw_circle(0.15)

    # Garis tick marks
    glColor3f(0.2, 0.2, 0.2)
    for i in range(60):
        angle = 2 * math.pi * i / 60
        outer = 0.14
        inner = 0.12 if i % 5 == 0 else 0.135
        x1, y1 = outer * math.cos(angle), outer * math.sin(angle)
        x2, y2 = inner * math.cos(angle), inner * math.sin(angle)
        glLineWidth(2 if i % 5 == 0 else 1)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()

    # Jam saat ini
    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute + sec / 60.0
    hour = (now.hour % 12) + minute / 60.0

    angle_hour = math.radians((hour / 12) * 360 - 90)
    angle_min = math.radians((minute / 60) * 360 - 90)
    angle_sec = math.radians((sec / 60) * 360 - 90)

    # Jarum jam
    glLineWidth(5)
    glColor3f(0.1, 0.1, 0.1)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0.08 * math.cos(angle_hour), 0.08 * math.sin(angle_hour))
    glEnd()

    # Jarum menit
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0.12 * math.cos(angle_min), 0.12 * math.sin(angle_min))
    glEnd()

    # Jarum detik merah
    glColor3f(1, 0, 0)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(0.13 * math.cos(angle_sec), 0.13 * math.sin(angle_sec))
    glEnd()

    # Titik tengah
    glPointSize(8)
    glColor3f(0, 0, 0)
    glBegin(GL_POINTS)
    glVertex2f(0, 0)
    glEnd()

    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    draw_background()
    draw_tower_body()
    draw_roof()
    draw_clock()

    glutSwapBuffers()


def update(value):
    glutPostRedisplay()
    glutTimerFunc(1000, update, 0)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(window_width, window_height)
    glutCreateWindow(b"Big Ben Style Clock - Large Version")

    glutDisplayFunc(display)
    glutReshapeFunc(resize)
    glutTimerFunc(0, update, 0)

    glClearColor(1.0, 1.0, 1.0, 1)
    gluOrtho2D(-1, 1, -1, 1)
    glutMainLoop()


if __name__ == "__main__":
    main()
