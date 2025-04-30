from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math
import datetime

width, height = 600, 600


def draw_circle(radius, segments=100):
    glBegin(GL_LINE_LOOP)
    for i in range(segments):
        angle = 2 * math.pi * i / segments
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)
    glEnd()


def draw_tick_marks():
    for i in range(60):
        angle = 2 * math.pi * i / 60
        outer = 0.95
        inner = 0.90 if i % 5 == 0 else 0.93
        x1, y1 = outer * math.cos(angle), outer * math.sin(angle)
        x2, y2 = inner * math.cos(angle), inner * math.sin(angle)
        glLineWidth(2 if i % 5 == 0 else 1)
        glBegin(GL_LINES)
        glVertex2f(x1, y1)
        glVertex2f(x2, y2)
        glEnd()


def draw_numbers():
    for i in range(1, 13):
        angle = 2 * math.pi * (i / 12) - math.pi / 2
        x = 0.78 * math.cos(angle)
        y = 0.78 * math.sin(angle)
        glRasterPos2f(x - 0.03, y - 0.03)
        for char in str(i):
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char)) # type: ignore


def draw_hand(length, angle, width):
    glLineWidth(width)
    glBegin(GL_LINES)
    glVertex2f(0, 0)
    glVertex2f(length * math.cos(angle), length * math.sin(angle))
    glEnd()


def draw_clock():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Lingkaran luar
    glColor3f(0.1, 0.1, 0.1)
    draw_circle(1.0)

    glColor3f(1, 1, 1)
    draw_circle(0.98)

    draw_tick_marks()

    glColor3f(1, 1, 0.5)
    draw_numbers()

    now = datetime.datetime.now()
    sec = now.second  # TANPA microsecond -> LONCAT
    minute = now.minute + sec / 60.0
    hour = (now.hour % 12) + minute / 60.0

    # Jam
    hour_angle = math.radians(360 * (hour / 12)) - math.pi / 2
    glColor3f(0, 0.5, 1)
    draw_hand(0.5, hour_angle, 5)

    # Menit
    minute_angle = math.radians(360 * (minute / 60)) - math.pi / 2
    glColor3f(0, 1, 0)
    draw_hand(0.7, minute_angle, 3)

    # Detik (lompat)
    second_angle = math.radians(360 * (sec / 60)) - math.pi / 2
    glColor3f(1, 0, 0)
    draw_hand(0.85, second_angle, 1)

    glPointSize(8)
    glBegin(GL_POINTS)
    glColor3f(1, 1, 1)
    glVertex2f(0, 0)
    glEnd()

    glutSwapBuffers()


def update(value):
    glutPostRedisplay()
    glutTimerFunc(1000, update, 0)  # 1000 ms = per detik


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Jam Analog - Detik Lompat, Menit & Jam Halus")
    glutDisplayFunc(draw_clock)
    glutTimerFunc(0, update, 0)

    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)

    glutMainLoop()


if __name__ == "__main__":
    main()
