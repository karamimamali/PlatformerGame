import pygame
from asset_loader import load_sprite_sheets, get_block
from constants import ATTACK_D



class Player(pygame.sprite.Sprite):
    GRAVITY = 1
    ANIMATION_DELAY = 8 


    def __init__(self, x, y, width, height, charater):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = 'L'
        self.image_count = 0
        self.fall_count = 0
        self.SPRITES = load_sprite_sheets(charater, width, height, True)
        self.jump_count = 0
        self.is_siting = False
        self.is_attacking = False
        self.attack_count = 0


    def attack(self):
        self.is_attacking = True

        if self.direction == 'L':
            self.rect.x += -ATTACK_D

        elif self.direction == 'R':
            self.rect.x += ATTACK_D


    def sit(self):
        self.is_siting = True


    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy


    def move_left(self, vel):
        self.x_vel = -vel

        if self.direction != 'L':
            self.direction = 'L'
            self.image_count = 0


    def move_right(self, vel):
        self.x_vel = abs(vel)

        if self.direction != 'R':
            self.direction = 'R'
            self.image_count = 0


    def jump(self):
        self.y_vel = -self.GRAVITY * 8
        self.animation_count = 0
        self.jump_count += 1

        if self.jump_count == 1:
            self.fall_count = 0


    def loop(self,FPS):
        self.y_vel += self.GRAVITY*(self.fall_count/FPS)
        self.move(self.x_vel, self.y_vel)

        if self.is_attacking:
            self.attack_count +=1

        if (self.attack_count/FPS) > 1.9:
            self.is_attacking = False
            self.attack_count = 0

        self.fall_count += 1

        

    def landed(self):
        self.fall_count = 0
        self.y_vel = 0
        self.jump_count = 0


    def hit_head(self):
        self.fall_count = 0
        self.y_vel *= -1
    

    def draw(self, WN, offset_x):
        WN.blit(self.sprite, (self.rect.x - offset_x, self.rect.y))


    def update_sprite(self):
        sprite_sheet = "Idle"
        if self.y_vel < 0:

            if self.jump_count == 1:
                sprite_sheet = "Jump"

            elif self.jump_count == 2:
                self.y_vel < 0

        elif self.x_vel != 0:
            sprite_sheet = "Walk"

        elif self.y_vel > self.GRAVITY*16:
            sprite_sheet = "Jump"

        elif self.is_siting:
            sprite_sheet = "Sit"

        elif self.is_attacking:
            sprite_sheet = "Attack"

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        sprite_index = (self.image_count //self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index]
        self.image_count += 1
        self.update()

    def update(self):
        self.rect = self.sprite.get_rect(topleft=(self.rect.x, self.rect.y))
        self.mask = pygame.mask.from_surface(self.sprite)





class Object(pygame.sprite.Sprite):
    def __init__(self,x, y, width, height, name=None):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.width = width
        self.height = height
        self.name = name

    def draw(self, WN, offset_x):
        WN.blit(self.image, (self.rect.x - offset_x, self.rect.y))



class Block(Object):
    def __init__(self, x, y, width, height, name=None):
        super().__init__(x, y, width, height, name)
        if name == 'green block':
            block = get_block(width,height,96,0)
        elif name == 'brick':
            block = get_block(width,height,272,64)
        self.image.blit(block, (0, 0))
        self.mask = pygame.mask.from_surface(self.image)
