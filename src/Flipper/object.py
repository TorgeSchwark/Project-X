import pygame
from global_variables import *
import numpy as np

class Polygon:
    def __init__(self, relative_corners):
        self.relative_corners = relative_corners
        self.corners = []
        self.edges = []
        self.imgae = None
        self.color = WHITE
        self.bounce_speed = 1.1
        self.randomness = 10

        self.rotation = {"total_rotation_steps": 8, "current_rotation_step": 0, "rotation_point": [0,0], "total_rotation_degree": 30, "current_rotation_direction": 0}
        self.rel_rotation_point = [0,0]
        self.lines_and_norms()

    def set_image(self, image):
        pass

    def set_rotation(self, rotation):
        self.rotation = rotation

    def scale_with_size(self, size):
        actual_corner = []
        for i in self.relative_corners:
            actual_corner.append((i[0]*size[0], i[1]*size[1]))
        self.corners = actual_corner
        self.rotation["rotation_point"] = [self.rel_rotation_point[0]*size[0],self.rel_rotation_point[1]*size[1]]
        self.lines_and_norms()

    def lines_and_norms(self):
        
        lines = []  
        for index in range(len(self.corners)):
            next_ind = (index + 1) % len(self.corners)
            line_start = self.corners[index]
            line_end = self.corners[next_ind]
            
            
            center_point = ((line_start[0] + line_end[0]) / 2, (line_start[1] + line_end[1]) / 2)            
            lines.append([line_start, line_end, center_point])

        for line in lines:
            if (line[0][0], line[0][1]) == (840.0, 9.0):
                print("hier")
            line_vec = [line[1][0]-line[0][0],line[1][1]-line[0][1]]
            norm = [line_vec[1], -line_vec[0]]
            norm /= np.linalg.norm(norm)
            right_direction = True
            for other_line in lines:
                if line == other_line:
                    continue
                mid_vec = np.array([line[2][0] - other_line[2][0],line[2][1] - other_line[2][1] ])
                mid_vec /= np.linalg.norm(mid_vec)  # Normiere den Vektor zu anderen Linien
                dot_product = np.dot(mid_vec, norm)
                if dot_product < 0:
                    right_direction = False
                
            if right_direction == False:
                norm = [float(-norm[0]),float(-norm[1])]
            norm = [float(norm[0]), float(norm[1])]
            norm_length = np.linalg.norm(norm)
            if norm_length >= 1.1:
                print("wrong_len", norm_length)
            line.append(norm)
        print(lines)

        self.edges = lines
    
    def collision(self, from_point, to_point, radius):
        result = [0.0, [0, 0], False, 0, 0, [0,0]]  # distance in percent, ball_turn_point, did_colide, randomness, speed, norm
        results = []
        conor = [False, [], [], [],[]]
        for edge in self.edges:
            edge_start = np.array(edge[0]) 
            edge_normal = np.array(edge[3])  
            edge_end = np.array(edge[1])

            dist_to_corner = [self.distance_from_line_to_point(from_point, to_point, edge_start, radius), self.distance_from_line_to_point(from_point, to_point, edge_end, radius)]

            from_ball_vector = np.array(from_point) - edge_start
            first_dist = np.dot(from_ball_vector, edge_normal)

            if first_dist < 0:
                continue

            to_ball_vector = np.array(to_point) - edge_start
            second_dist = np.dot(to_ball_vector, edge_normal)

            if first_dist >= radius > second_dist:

                direction_vector = np.array(to_point) - np.array(from_point)
                direction_length = np.linalg.norm(direction_vector)

                factor = (first_dist - radius) / (first_dist - second_dist)
                intersection_point = from_point + factor * direction_vector

                contact_point = intersection_point + (-edge_normal*radius)
                from_to_contact = np.array(contact_point) - edge_start
                from_to_contact_norm = from_to_contact / np.linalg.norm(from_to_contact)

                edge_vec = edge_end-edge_start
                edge_norm = edge_vec / np.linalg.norm(edge_vec)
                acuracy= 0.2
                if (edge_norm[0] - from_to_contact_norm[0] < acuracy and edge_norm[0] - from_to_contact_norm[0] > -acuracy) and (edge_norm[1] - from_to_contact_norm[1] < acuracy and edge_norm[1] - from_to_contact_norm[1] > -acuracy) and abs(from_to_contact[0]) < abs(edge_vec[0])+acuracy and abs(from_to_contact[1]) < abs(edge_vec[1])+acuracy:
                    result[0] = factor
                    result[1] = intersection_point.tolist()  
                    result[2] = True  
                    result[3] = self.randomness
                    result[4] = self.bounce_speed
                    result[5] = edge_normal
                    results.append(result.copy())
                else:
                    for edge_distance in dist_to_corner:
                        if len(edge_distance) != 0:
                            conor[0] = True
                            conor[1].append(edge_norm)
                            edge_len = np.linalg.norm(edge_vec)
                            len_to_point = np.linalg.norm(edge_distance[0]-edge_start)
                            conor[2].append(len_to_point/edge_len)
                            conor[3].append(edge_distance[0])
        if conor[0] == True:
            print(len(conor[1]))
            if len(conor[1]) == 2:
                result[0] = conor[2][0]
                result[1] = conor[3][0]
                result[2] = True
                result[3] = self.randomness
                result[4] = self.bounce_speed
                result[5] = self.vector_between(conor[1][0], conor[1][1])
                results.append(result.copy())

        return results

    def vector_between(self, v1, v2):
        # Normalisieren der Vektoren
        v1_normalized = v1 / np.linalg.norm(v1)
        v2_normalized = v2 / np.linalg.norm(v2)

        # Berechnung des Mittelwerts der normalisierten Vektoren
        midpoint = (v1_normalized + v2_normalized) / 2

        # Normalisieren des resultierenden Vektors
        result_vector = midpoint / np.linalg.norm(midpoint)

        return result_vector

    def distance_from_line_to_point(self, point1, point2, point, r):
        # Punkte der Geraden
        x1, y1 = point1
        x2, y2 = point2

        # Berechnung der Koeffizienten der Geraden
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2

        # Berechnung des Abstands zur Geraden
        distance = abs(A * point[0] + B * point[1] + C) / np.sqrt(A**2 + B**2)

        # Wenn der Abstand bereits dem gewünschten Abstand entspricht
        if distance >= r:
            return []

        # Richtung des Normalenvektors zur Geraden
        normal_vector = np.array([A, B])
        normal_vector /= np.linalg.norm(normal_vector)  # Normalisieren

        # Berechnung der beiden Punkte in der Richtung des Normalenvektors
        delta = normal_vector * (r - distance)
        
        point1_result = (point[0] + delta[0], point[1] + delta[1])
        point2_result = (point[0] - delta[0], point[1] - delta[1])

        # Rückgabe des Punktes, der näher an point1 ist
        distance_to_point1_result = np.linalg.norm(np.array(point1) - np.array(point1_result))
        distance_to_point1_result2 = np.linalg.norm(np.array(point1) - np.array(point2_result))

        if distance_to_point1_result < distance_to_point1_result2:
            return point1_result
        else:
            return point2_result

    def set_relative_rotation_point(self, point):

        self.rel_rotation_point[0] = point[0]
        self.rel_rotation_point[1] = point[1]

    def rotate_kick(self):
        if self.rotation["current_rotation_direction"] == 0:
            self.rotation["current_rotation_direction"] = 1

    def apply_physics(self):
        
        if self.rotation["current_rotation_direction"] == 1:
            rotate_per_step = self.rotation["total_rotation_degree"]/self.rotation["total_rotation_steps"]
            self.rotation["current_rotation_step"] += self.rotation["current_rotation_direction"]
            if self.rotation["current_rotation_step"] == 10:
                self.rotation["current_rotation_direction"] = -1
            self.rotate(rotate_per_step)
        elif self.rotation["current_rotation_direction"] == -1:
            rotate_per_step = -self.rotation["total_rotation_degree"]/self.rotation["total_rotation_steps"]
            self.rotation["current_rotation_step"] += self.rotation["current_rotation_direction"]
            if self.rotation["current_rotation_step"] == 0:
                self.rotation["current_rotation_direction"] = 0
            self.rotate(rotate_per_step)

    def rotate(self, degree):
        radians = np.radians(degree)
        cos_theta = np.cos(radians)
        sin_theta = np.sin(radians)

        rotation_matrix = np.array([[cos_theta, -sin_theta],
                                     [sin_theta, cos_theta]])

        rotation_point = self.rotation["rotation_point"]
        rotation_point = np.array(rotation_point)

        translated_corners = self.corners - rotation_point

        rotated_corners = np.dot(translated_corners, rotation_matrix)

        self.corners = rotated_corners + rotation_point

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.corners)

    