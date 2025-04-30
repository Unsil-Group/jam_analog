from models.sphere import draw_sphere
import random
from OpenGL.GL import *

def create_cloud_positions():
    """Generate fixed positions for clouds"""
    positions = []
    for _ in range(6):  # Create 6 static clouds
        positions.append([
            random.uniform(-10, 10),  # x position
            random.uniform(3, 5),     # y height (above most objects)
            random.uniform(-10, -5),  # z position (behind scene center)
            random.uniform(0.8, 1.2)  # size
        ])
    return positions

# Fixed cloud positions
CLOUD_POSITIONS = create_cloud_positions()

def draw_cloud(x, y, z, size):
    """Draw a static cloud using spheres"""
    glDisable(GL_LIGHTING)
    glColor3f(0.95, 0.95, 0.95)  # Slightly off-white
    
    glPushMatrix()
    glTranslatef(x, y, z)
    
    # Main cloud body (3 overlapping spheres)
    draw_sphere(size * 0.8)
    glTranslatef(size*0.3, -size*0.1, 0)
    draw_sphere(size * 0.6)
    glTranslatef(-size*0.6, size*0.1, 0)
    draw_sphere(size * 0.7)
    
    glPopMatrix()
    glEnable(GL_LIGHTING)

def draw_sky():
    """Draw sky background with static clouds"""
    # Sky gradient
    glDisable(GL_LIGHTING)
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.6, 1.0)  # Top color
    glVertex3f(-15, 8, -15)
    glVertex3f(15, 8, -15)
    glColor3f(0.7, 0.8, 1.0)  # Bottom color
    glVertex3f(15, -1, -15)
    glVertex3f(-15, -1, -15)
    glEnd()
    
    # Sun
    glPushMatrix()
    glTranslatef(3, 3, -3)
    glColor3f(1.0, 0.85, 0.2)
    draw_sphere(0.5)
    glPopMatrix()
    
    # Draw all static clouds
    for x, y, z, size in CLOUD_POSITIONS:
        draw_cloud(x, y, z, size)
    
    glEnable(GL_LIGHTING)