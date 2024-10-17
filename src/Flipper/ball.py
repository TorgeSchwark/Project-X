from global_variables import *
import pygame
import numpy as np

class Ball:

    def __init__(self, size, x, y):
        self.relative_values = [size, x, y]

        self.ball_color = WHITE
        self.ball_radius = 0
        self.randomness = 0
        self.bounce_speed = 1
        self.x = 0
        self.y = 0
        self.moving = False
        self.direction = [0,0]
        self.acceleration = 5
    
    def scale_with_size(self, size):
        self.x = self.relative_values[1]*size[0]
        self.y = self.relative_values[2]*size[1]
        self.ball_radius = self.relative_values[0]*size[1]

    def apply_physics(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def move(self):
        self.x += self.direction[0]
        self.y += self.direction[1]

    def collision(self, from_point, to_point, radius):
        return []
        
    def redirect(self, factor, turn_point, cross_point_exists, randomness, speed, normal):
        # Berechnung der Länge und Normalisierung der Richtungs- und Normalenvektoren
        direction_len = np.linalg.norm(self.direction)
        direction = self.direction / direction_len if direction_len > 0 else np.array([0.0, 0.0])
        normal = normal / np.linalg.norm(normal)

        # Berechnung des Einfallswinkels
        dot_product = np.dot(direction, normal)

        # Berechnung des reflektierten Vektors
        reflected_direction = direction - 2 * dot_product * normal

        # Zufällige Ablenkung um einen bestimmten Bereich (optional)
        random_angle = np.random.uniform(-randomness, randomness)
        cos_angle = np.cos(random_angle)
        sin_angle = np.sin(random_angle)

        # Rotieren des reflektierten Vektors um den zufälligen Winkel
        rotated_direction = np.array([
            reflected_direction[0] * cos_angle - reflected_direction[1] * sin_angle,
            reflected_direction[0] * sin_angle + reflected_direction[1] * cos_angle
        ])

        if np.dot(rotated_direction, normal) < 0:
            rotated_direction = reflected_direction

        # Aktualisieren der Richtung mit der ursprünglichen Geschwindigkeit
        
        self.direction = rotated_direction * direction_len  # Geschwindigkeit beibehalten
        new_pos = turn_point + (self.direction * factor)
        self.x = new_pos[0]
        self.y = new_pos[1]

    def draw(self, screen):
        pygame.draw.circle(screen, self.ball_color, (self.x, self.y), self.ball_radius)
