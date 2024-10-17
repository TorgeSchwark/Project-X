from button import *
from bar import * 
from Flipper.flipper import *

class FrameGame:
    def __init__(self, size):
        
        self.window_size = size
        self.left_mouse_button_pressed = False
        self.base_ui = None
        self.games_buttons = None
        self.base_game_ui()
        self.setup_frame()

        self.current_game = "frame_game"
        self.games = {"flipper": Flipper(size)}


    def base_game_ui(self):
        width = self.window_size[0]/20
        self.base_ui = Bar(self.window_size[0]-width, 0, width, self.window_size[1], True, True, "V", (50,50,50), BAR_STYLE_ONE)


    def setup_frame(self):
        games_button_position = [0.1,0.03,0.7,0.15]

        self.games_buttons = Bar(self.window_size[0]*games_button_position[0], self.window_size[1]*games_button_position[1], self.window_size[0]*games_button_position[2],self.window_size[1]*games_button_position[3], True, True, "H",(100,100,100), BAR_STYLE_ONE)
        self.games_buttons.add_button("scrollable", "1st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_gold.png","scrollable", 0)
        self.games_buttons.set_function(self.play_flipper, "scrollable", 0)
        self.games_buttons.add_button("scrollable", "2st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_diamond.png","scrollable", 1)
        self.games_buttons.add_button("scrollable", "3st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_fire.png","scrollable", 2)
        self.games_buttons.add_button("scrollable", "4st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_green.png","scrollable", 3)
        self.games_buttons.add_button("scrollable", "5st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_pink.png","scrollable", 4)
        self.games_buttons.add_button("scrollable", "6st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_red.png","scrollable", 5)

    def play_flipper(self):
        self.current_game = "flipper"
        self.window_size = (self.window_size[0]/16*7,self.window_size[1])
        self.games["flipper"].set_window_size(self.window_size)
        pygame.display.set_mode(self.window_size)

    # only function that is called from the main loop
    # handles Whjich elements need to be drawn applies physics etc
    def manager(self, screen, events):
        if self.current_game == "frame_game":
            self.draw(screen)
            self.manage_inputs(events)
        elif self.current_game == "flipper":
            self.games[self.current_game].applie_physics()
            self.games[self.current_game].draw(screen)
            self.games[self.current_game].manage_inputs(events)


    def manage_inputs(self, events):
        
        mouse_button = pygame.mouse.get_pressed()
        
        if mouse_button[0] and not self.left_mouse_button_pressed:
            self.left_mouse_button_pressed = True  
            self.games_buttons.is_clicked_left()  

        if not mouse_button[0]:
            self.left_mouse_button_pressed = False


        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                self.games_buttons.scrolling(-event.y*30)
            

    def draw(self, screen):
        self.games_buttons.draw(screen)
        self.base_ui.draw(screen)