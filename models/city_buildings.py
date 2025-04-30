from models._index import *
from models.cube import draw_cube


def draw_city_buildings():
    # Draw several buildings around the clock tower
    for i in range(8):
        glPushMatrix()
        angle = math.radians(45 * i)
        distance = 4.0
        x = distance * math.cos(angle)
        z = distance * math.sin(angle)
        glTranslatef(x, 0, z)
        
        # Random building height and width
        height = 1 + (i % 3) * 0.5
        width = 0.7 + (i % 2) * 0.2
        
        # Main building structure - PERBAIKAN POSISI Y
        glColor3f(0.5, 0.5, 0.5)  # Gray buildings
        glPushMatrix()
        glTranslatef(0, height/2, 0)  # Pusatkan bangunan di sumbu Y
        glScalef(width, height, width)
        draw_cube(1.0)
        glPopMatrix()
        
        # Roof (different types for variety)
        glColor3f(0.3, 0.3, 0.3)  # Dark gray roof
        glPushMatrix()
        glTranslatef(0, height, 0)  # Posisi atap di atas bangunan
        
        if i % 2 == 0:
            # Flat roof with edge
            glScalef(width+0.05, 0.05, width+0.05)
            draw_cube(1.0)
        else:
            # Sloped roof - PERBAIKAN UKURAN
            glBegin(GL_TRIANGLE_FAN)
            glVertex3f(0, 0.3, 0)  # Roof peak
            glVertex3f(-(width+0.05), 0, -(width+0.05))
            glVertex3f(width+0.05, 0, -(width+0.05))
            glVertex3f(width+0.05, 0, width+0.05)
            glVertex3f(-(width+0.05), 0, width+0.05)
            glVertex3f(-(width+0.05), 0, -(width+0.05))
            glEnd()
        glPopMatrix()
        
        # Windows (with frames) - PERBAIKAN POSISI Z
        window_color = (0.8, 0.8, 0.9) if i % 3 != 0 else (0.7, 0.9, 1.0)
        for y in [-0.4, -0.1, 0.2]:
            if y < height - 0.3:
                # Window frame
                glColor3f(0.3, 0.3, 0.3)
                glPushMatrix()
                glTranslatef(0, height/2 + y, width+0.001)  # Sesuaikan dengan posisi bangunan
                glScalef(0.7, 0.25, 0.02)
                draw_cube(1.0)
                glPopMatrix()
                
                # Window glass
                glColor3f(*window_color)
                glPushMatrix()
                glTranslatef(0, height/2 + y, width+0.002)
                glScalef(0.65, 0.2, 0.01)
                draw_cube(1.0)
                glPopMatrix()
        
    
        
        # Side details
        if i % 4 == 0:
            glColor3f(0.7, 0.7, 0.7)
            for y in [-0.3, 0.1]:
                glPushMatrix()
                glTranslatef(width+0.001, height/2 + y, 0)
                glScalef(0.02, 0.2, 0.3)
                draw_cube(1.0)
                glPopMatrix()
        
        glPopMatrix()