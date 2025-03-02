from button import *
from bar import * 
from dropout_selection import *
from settings import *

class FrameGame:
    def __init__(self, size):
        
        self.window_size = size
        self.left_mouse_button_pressed = False

        self.base_ui = None
        self.games_buttons = None
        self.settings_menu = None

        self.current_game = "frame_game"
        self.games = {"frame_game": self, "settings": self}
        self.to_draw = []
        self.active = []
        self.save_todraw = []

        self.base_game_ui()
        self.setup_frame()
        self.setup_settings()

    # only function that is called from the main loop
    # handles Whjich elements need to be drawn applies physics etc
    def manager(self, screen, events):
        self.games[self.current_game].draw(screen)
        self.games[self.current_game].manage_inputs(events)


    def manage_inputs(self, events):
        
        mouse_button = pygame.mouse.get_pressed()
        
        if mouse_button[0] and not self.left_mouse_button_pressed:
            self.left_mouse_button_pressed = True
            for obj in self.active:
                obj.is_clicked_left()  

        if not mouse_button[0]:
            self.left_mouse_button_pressed = False


        for event in events:
            if event.type == pygame.MOUSEWHEEL:
                for obj in self.active:
                    obj.scrolling(-event.y*30)


    def base_game_ui(self):
        width = self.window_size[0]/22
        self.base_ui = Bar(self.window_size[0]-width+1, 0, width, self.window_size[1], "V", (50,50,50), BAR_STYLE_ONE)
        self.base_ui.add_button("bottom", "Setttings")
        self.base_ui.set_function(self.display_settings, "bottom", 0)
        self.base_ui.add_button("top", "Upgrades")
        self.base_ui.add_button("top", "Games")
        self.base_ui.set_function(self.display_games , "top", 1)

        # register bar
        self.to_draw.append(self.base_ui)
        self.active.append(self.base_ui)
        

    def setup_frame(self):
        games_button_position = [0.1,0.03,0.7,0.15]
        width = self.window_size[0]/7
        height = self.window_size[1]
        x = self.base_ui.rect.x - width + 1
        y = 0

        self.games_buttons = Bar(x, y, width, height, "V",(100,100,100), BAR_STYLE_ONE)
        self.games_buttons.add_button("scrollable", "1st game")
        self.games_buttons.set_button_frame_image("./src/Images/game_frame_gold.png","scrollable", 0)
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
        self.games_buttons.deactivate()
        

    def setup_settings(self):
        self.settings_menu = Settings(0,0, self.window_size[0], self.window_size[1], (100,100,100), (255,255,255), 20, self.save_settings, self.dismiss_settings, False)

    def display_games(self):
        if self.games_buttons in self.to_draw:
            self.to_draw.remove(self.games_buttons)
            self.active.remove(self.games_buttons)
            self.games_buttons.deactivate()
        else:
            self.to_draw.append(self.games_buttons)
            self.active.append(self.games_buttons)
            self.games_buttons.activate()

    def display_settings(self):
        if self.settings_menu in self.to_draw:
            self.reactivate_screen()
            self.settings_menu.deactivate()
        else:
            self.save_todraw = self.to_draw
            self.clear_screen()
            self.to_draw.append(self.settings_menu)
            self.active.append(self.settings_menu)
            self.settings_menu.activate()

    def clear_screen(self):
        # remove everthing exept the base ui
        self.to_draw = [self.to_draw[0]]
        for obj in self.active:
                obj.deactivate()
        self.active = [self.active[0]]

    def reactivate_screen(self):
        self.to_draw = self.save_todraw
        self.active = self.save_todraw
        for obj in self.active:
            obj.activate()

    def save_settings(self):
        # save settings

        print("Save settings")
        self.reactivate_screen()
        self.settings_menu.deactivate()

    def dismiss_settings(self):
        print("Dismiss settings")
        # reset attributes?
        self.reactivate_screen()
        self.settings_menu.deactivate()
        

    def draw(self, screen):
        for obj in self.to_draw:
            obj.draw(screen)