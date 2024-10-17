from Flipper.ball import *
from Flipper.object import *

class Flipper:

    def __init__(self, size):
        self.window_size = size
        self.score = 0
        self.highscore = 0

        self.relative_coords = {"left_player": [(0.2,0.8),(0.2,0.85),(0.44,0.9),(0.44,0.89)], "ball": [0.015, 0.94, 0.8], "rotation_point_left": (0.21, 0.83), \
                                "right_player": [(0.8,0.8),(0.8,0.85),(0.56,0.9),(0.56,0.89)], "rotation_point_right": (0.79, 0.83), "blocks": [], "blocks_round": []}
        
        self.relative_coords["blocks"].append([(0.88,0.85),(0.88,0.3),(0.9,0.3),(0.9,0.85)]) #pipe left
        self.relative_coords["blocks"].append([(0.97,0.85),(0.97,0.2),(0.99,0.2),(0.99,0.85)]) #pipe right
        self.relative_coords["blocks"].append([(0.8,0),(0.82,0.0),(0.99,0.2),(0.97,0.2)]) # rail top
        self.relative_coords["blocks"].append([(0.88,0.3),(0.9,0.3),(0.73,0.1),(0.71,0.1)]) # rail top

        self.relative_coords["blocks"].append([(0.8,0.8),(0.8,0.85),(0.88,0.75),(0.88,0.7)]) #guard right
        self.relative_coords["blocks"].append([(0.2,0.8),(0.2,0.85),(0,0.7),(0,0.65)]) #guard left

        self.relative_coords["blocks"].append([(0.15,0.2),(0.17,0.2),(0.17,0.5),(0.15,0.5)]) #bounce pipe right
        self.relative_coords["blocks"].append([(0.0,0.2),(0.02,0.2),(0.02,0.5),(0,0.5)]) #bounce pipe left
        self.relative_coords["blocks"].append([(0.15,0.2),(0.17,0.2),(0.32,0.13),(0.3,0.13)]) #trichter

        self.relative_coords["blocks"].append([(0.3,0.2),(0.32,0.2),(0.25,0.3),(0.23,0.3)])

        self.relative_coords["blocks_round"].append([0.015,0.045,0.25]) 
        self.relative_coords["blocks_round"].append([0.015,0.127,0.35])
        self.relative_coords["blocks_round"].append([0.015,0.045,0.45])

        self.relative_coords["blocks_round"].append([0.035,0.5,0.4]) #centered ball
        self.relative_coords["blocks"].append([(0.65,0.4),(0.67,0.4),(0.57,0.5),(0.55,0.5)]) # right trichter
        self.relative_coords["blocks"].append([(0.35,0.4),(0.33,0.4),(0.43,0.5),(0.45,0.5)]) # left trichter
        self.relative_coords["blocks"].append([(0.43,0.27),(0.43,0.29),(0.57,0.29),(0.57,0.27)])

        self.relative_coords["blocks_round"].append([0.02,0.5,0.6])
        self.relative_coords["blocks_round"].append([0.02,0.23,0.6])
        self.relative_coords["blocks_round"].append([0.04,0.77,0.47])
        self.relative_coords["blocks_round"].append([0.04,0.77,0.63])

        self.relative_coords["blocks"].append([(0.7,0.25),(0.76,0.25),(0.76,0.3),(0.70,0.3)])
        self.relative_coords["blocks"].append([(0.45,0.1),(0.47,0.1),(0.62,0.2),(0.62,0.2155)])

        self.relative_coords["blocks"].append([(1.2,-0.2),(0.99,-0.2),(.99,1.2),(1.2,1,2)]) #right

        self.relative_coords["blocks"].append([(-0.2,-0.2),(0.01,-0.2),(0.01,1.2),(-0.2,1,2)]) #left

        self.relative_coords["blocks"].append([(-0.2,-0.2),(1.2,-0.2),(1.2,0.01),(-0.2,0.01)]) #top

        self.relative_coords["blocks"].append([(-0.2,1.2),(1.2,1.2),(1.2,1),(-0.2,1)])



        self.main_objects = {}
        self.blocks = []
        self.setup_window(size)

        self.left_key_pressed = False
        self.right_key_pressed = False

    def manage_inputs(self, events):
        keys = pygame.key.get_pressed()  

        if keys[pygame.K_LEFT]:
            if not self.left_key_pressed:  
                self.main_objects["left_player"].rotate_kick()
                self.left_key_pressed = True  
        else:
            self.left_key_pressed = False  

        if keys[pygame.K_RIGHT]:
            if not self.right_key_pressed:  
                self.main_objects["right_player"].rotate_kick()
                self.right_key_pressed = True  
        else:
            self.right_key_pressed = False 

    def applie_physics(self):
        
        ball_next = [self.main_objects["ball"].x+self.main_objects["ball"].direction[0], self.main_objects["ball"].y +self.main_objects["ball"].direction[1]]
        ball_current = [self.main_objects["ball"].x, self.main_objects["ball"].y]
        cross_points = []

        for block in self.blocks:
            cross_point = block.collision(ball_current, ball_next, self.main_objects["ball"].ball_radius)
            if len(cross_point) != 0:
                for i in cross_point:
                    cross_points.append(i)
        
        if len(cross_points) != 0:
            print("cross_points: ", cross_points)
            print("crossed")
            closest_index = 0
            closest = 1.1
            for i in range(len(cross_points)):
                print(cross_points[i])
                if cross_points[i][0] < closest:
                    closest_index = i
                    closest = cross_points[i][0]

            self.main_objects["ball"].redirect(*cross_points[closest_index])
        else:
            self.main_objects["ball"].move()

    def set_window_size(self, size):
        self.window_size = size
        self.setup_window(size)
        
    def setup_window(self, size):

        self.main_objects["left_player"] = Polygon(self.relative_coords["left_player"])
        self.main_objects["left_player"].set_relative_rotation_point(self.relative_coords["rotation_point_left"]) 
        self.main_objects["right_player"] =  Polygon(self.relative_coords["right_player"])
        self.main_objects["right_player"].set_relative_rotation_point(self.relative_coords["rotation_point_right"]) 
        self.main_objects["ball"] = Ball(*self.relative_coords["ball"])
        self.main_objects["show_point"] = Ball(*self.relative_coords["ball"])   
        self.main_objects["right_player"].set_rotation({"total_rotation_steps": 8, "current_rotation_step": 0, "rotation_point": [0,0], "total_rotation_degree": -30, "current_rotation_direction": 0})
        
        self.main_objects["ball"].direction = [0,-6]

        for relative_cords in self.relative_coords["blocks"]:
            self.blocks.append(Polygon(relative_cords))

        for relative_cords in self.relative_coords["blocks_round"]:
            self.blocks.append(Ball(*relative_cords))

        for key in self.main_objects:   
            self.main_objects[key].scale_with_size(size)
        for block in self.blocks:
            block.scale_with_size(size)
        



    def draw(self, screen):
        for object in self.main_objects:
            self.main_objects[object].draw(screen)
        for block in self.blocks:
            block.draw(screen)
        