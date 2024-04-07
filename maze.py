from typing import Any
from pygame import *



win_wight = 500
win_hight = 700

window = display.set_mode((win_hight, win_wight))
display.set_caption('Maze')
background = transform.scale(image.load("background.jpg"),(win_hight, win_wight))


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed) :
        super().__init__()
        self.image = transform.scale(image.load(player_image),(45,45))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > -10:
            self.rect.y -= 5
        if key_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += 5
        if key_pressed[K_LEFT] and self.rect.x > -10:
            self.rect.x -= 5
        if key_pressed[K_RIGHT]and self.rect.x < 650:
            self.rect.x += 5
        

class Enemy(GameSprite):
    def update(self):
        if self.direction == 'left':
            if self.rect.x <= 10:
                self.direction = 'right'
            else:
                self.rect.x -= 5
        else:
            if self.rect.x >= 550:
                self.direction = 'left'
            else:
                self.rect.x += 5

class Wall(sprite.Sprite):
    def __init__(self, color, wall_wight, wall_hight, wall_x, wall_y):
        self.color = color
        self.wall_hight = wall_hight
        self.wall_wight = wall_wight
        self.image = Surface((self.wall_wight, self.wall_hight)) 
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))




#WALLS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


walls = []
walls.append(Wall((0, 0, 0), 500, 10, 40, 5))#top
walls.append(Wall((0, 0, 0), 500, 10, 40, 480))#lower 
walls.append(Wall((0, 0, 0), 10, 400, 40, 5))#left 
walls.append(Wall((0, 0, 0), 10, 350, 180, 130))#first wall
walls.append(Wall((0, 0, 0), 10, 380, 330, 5))#second wall\
walls.append(Wall((0, 0, 0), 100, 10, 330, 380))
walls.append(Wall((0, 0, 0), 10, 340, 530, 150))#the lower part of the T        
walls.append(Wall((0, 0, 0), 100, 10, 430, 150))#the top part of the T



clock = time.Clock()
FPS = 60
#PLAYER
player = Player('hero.png', 40, 425, 2)
#ENEMY
enemy = Enemy('cyborg.png', 300, 250, 2)
#MONEY
treasure = GameSprite('treasure.png', 580, 40, 2)

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

finish = False
points = 0
game = True
while game:

    if not finish:
        window.blit(background, (0,0))
        
        enemy.update()
        player.update()
        
        player.reset() 
        enemy.reset()
        treasure.reset()

        if sprite.collide_rect(player, treasure):
            finish = True
            mixer.music.load('money.ogg')
            mixer.music.play()

        if sprite.collide_rect(player,enemy):
            finish = True
            mixer.music.load('kick.ogg')
            mixer.music.play()

        for wall in walls:
            wall.draw_wall()
            if sprite.collide_rect(player,wall):
                finish = True
                mixer.music.load('kick.ogg')
                mixer.music.play()
    
        clock.tick(FPS)
        display.update()

    for i in event.get():
        if i.type == QUIT:
            game == False
            quit()
            sys.exit()



            