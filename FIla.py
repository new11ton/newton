from pygame import*
from random import*

window = display.set_mode((700,500))
display.set_caption(ping-fonk)
game = True
finish = False

class GameSprite(sprite,sprite):
    def __init__(self , player_image , player_x , player_y , player_speed , width , height):
        super().__init__()
        self.image = transform.scale(image.load(player_image) , (width , height))
        self.speed = player_speed
        self.rect = self_image.get_rect()
        self.rect.x = self.rect.x
        self.rect.y = self.rect.y
    def reset(self):
        window.blit(self.image , ( self.rect.x , self.rect.y ))
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]and self.rect.y 
            self.rect.y -= self.speed
        if keys_pressed[K_s]and self.rect.y 
            self.rect.y += self.speed
    def update2(self):
        if keys_pressed[K_UP]and self.rect.y 
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN]and self.rect.y 
            self.rect.y += self.speed