from livewires import games, color
from tkinter import*
import settings
import random

games.init(screen_width = 735, screen_height = 350, fps = 35)

class Bounce(games.Sprite):
    def update(self):

        if self.right > games.screen.width or self.left < 0: 
            self.dx = -self.dx

        if self.top < 0:
            self.dy = -self.dy

        if self.bottom == 315 and self.overlapping_sprites: 
            self.dy = -self.dy


class Bar_moving(games.Sprite):
    def update(self):   

        self.x = games.mouse.x  
        self.y = 315

class handling_settings():

    self.yr = settings.app.bbbbb()
    print("printing number from settings  ", self.yr)

    def create_ball_numbers(self):
        print("inside def", self.yr)



def main():

    background = games.load_image("BG.jpg", transparent = False)
    games.screen.background = background

    call = handling_settings()
    call.create_ball_numbers()

    bar_small = games.load_image("bar_small.jpg", transparent = False)
    the_bar_small = Bar_moving(image = bar_small, x = games.mouse.x)

    games.screen.add(the_bar_small)
    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()


main()    