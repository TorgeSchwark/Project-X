import pygame 
from button import *

class Bar:

    def __init__(self, x, y, width, height, permanent, scrollable, axis, color):
        
        self.color = color
        self.axis = axis # "H / V"
        self.elements = {"top": [], "scrollable": [], "bottom": []}
        
        style = {"size": 100, "fill_size": 0.8, "color": (50,50,50), "hover_color": (200,200,200), "text_color": (100,100,100), "text_size": 20, "spacing": 10}
        self.element_style = {"top": style.copy(), "scrollable" : style.copy(), "bottom": style.copy()}
        self.y = y
        self.x = x
        self.width = width
        self.height = height
        self.permanent = permanent
        self.scrollable = scrollable # ?? 
        # Rect that represents the bar area
        self.rect = pygame.Rect(x, y, width, height)
        
        if axis == "H":
            self.scrollable_cords = [x + self.element_style["top"]["spacing"], x + width - self.element_style["bottom"]["spacing"], 0, 0] 
        else:
            self.scrollable_cords = [y + self.element_style["top"]["spacing"], y + height - self.element_style["bottom"]["spacing"], 0, 0]

        # Scroll position
        self.scroll_offset = 0

    # self, text, x, y, width, height, color, hover_color, text_color, text_size
    def add_button(self, position, text):
        color = self.element_style[position]["color"]
        hover_color =  self.element_style[position]["hover_color"]
        text_color = self.element_style[position]["text_color"]
        text_size = self.element_style[position]["text_size"]

        if self.axis == "H":
            height = self.element_style[position]["fill_size"] * self.height
            width = self.element_style[position]["size"]
            y_pos = self.y+ (((1-self.element_style[position]["fill_size"])/2)*self.height)
            if position == "top":
                x_pos = self.scrollable_cords[0]
                button = Button(text, x_pos, y_pos, width, height, color, \
                                 hover_color, text_color, text_size)
                self.scrollable_cords[0] += width + self.element_style[position]["spacing"]
                
            if position == "scrollable":
                x_pos = self.scrollable_cords[2]+ self.element_style[position]["spacing"]+ self.element_style[position]["size"]
                button = Button(text, x_pos, y_pos, width, height, color, \
                                 hover_color, text_color, text_size)
            if position == "bottom":
                x_pos = self.scrollable_cords[1]-self.element_style[position]["size"]
                button = Button(text, x_pos, y_pos, width, height, color, \
                                 hover_color, text_color, text_size)
                self.scrollable_cords[1] -= (width + self.element_style[position]["spacing"])
            
                
        else:
            x_pos = self.x + (((1-self.element_style[position]["fill_size"])/2)*self.width)
            width = self.element_style[position]["fill_size"] * self.width
            height = self.element_style[position]["size"]
            if position == "top": 
                y_pos = self.scrollable_cords[0]
                button = Button(text, x_pos, y_pos, width, height, color, \
                                 hover_color, text_color, text_size)
                self.scrollable_cords[0] += height + self.element_style[position]["spacing"]

            if position == "scrollable":
                y_pos = self.scrollable_cords[2]+ self.element_style[position]["spacing"]+ self.element_style[position]["size"]
                button = Button(text, x_pos, y_pos, width, height, color, \
                                 hover_color, text_color, text_size)
            if position == "bottom":
                y_pos = self.scrollable_cords[1]-self.element_style[position]["size"]
                button = Button(text, x_pos, y_pos, width, height, color, \
                                 hover_color, text_color, text_size)
                self.scrollable_cords[1] -= (height + self.element_style[position]["spacing"])

        self.elements[position].append(button)
                

    def scrolling(self, amount):
        self.scroll_offset = max(0, self.scroll_offset+amount)
        
             
    def draw(self, screen):

        pygame.draw.rect(screen, self.color, self.rect)

        # Save the original clipping area
        original_clip = screen.get_clip()

        # Set the clipping area to the bar's rectangle (only draw inside this)
        clip_rect = self.rect
        if self.axis == "V":
            height = self.scrollable_cords[1] - self.scrollable_cords[0]
            clip_rect = pygame.Rect(self.x, self.scrollable_cords[0], self.width, height)
        else:
            width = self.scrollable_cords[1]- self.scrollable_cords[0]
            clip_rect = pygame.Rect(self.scrollable_cords[0], self.y, width, self.height)

        screen.set_clip(clip_rect)
        
        # Draw middle (scrollable) elements
        temp_storage = 0
        temp_size = 0
        for i, obj in enumerate(self.elements["scrollable"]):
            if self.axis == "V":
                obj.rect.y = self.scrollable_cords[0] + i * self.element_style["scrollable"]["spacing"] + temp_size - self.scroll_offset

                # draw and clip objects that are inside
                if obj.rect.bottom > self.y and obj.rect.top < self.y + self.height:
                    obj.draw(screen)

                temp_size += obj.rect.height
                temp_storage = obj.rect.y
            else:
                obj.rect.x = self.scrollable_cords[0] + i * self.element_style["scrollable"]["spacing"] + temp_size - self.scroll_offset
                
                # draw and clip objects that are inside
                if obj.rect.right > self.x and obj.rect.left < self.x + self.width:
                    obj.draw(screen)
                
                temp_size += obj.rect.width
                temp_storage = obj.rect.x
            
        # Update scrollable cords to match last drawn element    
        self.scrollable_cords[2] = temp_storage
        
        # Restore the original clipping area
        screen.set_clip(original_clip)

        # Draw top (permanent) elements
        for obj in self.elements["top"]:
            obj.draw(screen)
        
        # Draw bottom (permament) elements
        for obj in self.elements["bottom"]:
            obj.draw(screen)
