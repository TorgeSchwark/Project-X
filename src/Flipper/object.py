import pygame
from global_variables import *
import numpy as np

class Polygon:
    def __init__(self, corners):
        self.corners = corners
        self.imgae = None
        self.color = WHITE

    def set_image(self, image):
        pass 

    #returns the normal of the colision point
    def collision(self, x_before, y_before, x_after, y_after):
        line_start = np.array([x_before, y_before])
        line_end = np.array([x_after, y_after])

        for i in range(len(self.corners)):
            start_corner = np.array(self.corners[i])
            end_corner = np.array(self.corners[(i + 1) % len(self.corners)])

            edge_vector = end_corner - start_corner
            normal = np.array([-edge_vector[1], edge_vector[0]])
            normal = normal / np.linalg.norm(normal)  

            if self.line_intersects(line_start, line_end, start_corner, end_corner):
                return normal  

        return None

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.corners)

    