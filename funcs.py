import pygame
from constants import *
from classes import Player ,Block

def handle_vertical_collision(player, objects, dy):
    collided_objects = []
    for obj in objects:

        if pygame.sprite.collide_mask(player, obj):

            if dy > 0:
                player.rect.bottom = obj.rect.top
                player.landed()

            elif dy < 0:
                player.rect.top = obj.rect.bottom
                player.hit_head()

            collided_objects.append(obj)

    return collided_objects

def collide(player, objects, dx):
    player.move(dx, -15)
    player.update()
    collided_object = None

    for obj in objects:

        if pygame.sprite.collide_mask(player, obj):
            collided_object = obj
            break

    player.move(-dx, 15)
    player.update()

    return collided_object

def handle_move(player, objects):
    keys = pygame.key.get_pressed()
    player.is_siting = False
    player.x_vel = 0
    collide_left = collide(player, objects, -PLAYER_VEL *7)
    collide_right = collide(player, objects, PLAYER_VEL *7)
 
    if keys[pygame.K_a] and not collide_left:
        player.move_left(PLAYER_VEL)

    elif keys[pygame.K_a] and collide_left:
        player.rect.left = collide_left.rect.right

    if keys[pygame.K_d] and not collide_right:
        player.move_right(PLAYER_VEL)

    elif keys[pygame.K_d] and collide_right:
        player.rect.right = collide_right.rect.left

    if keys[pygame.K_s]:
        player.is_siting = True
    
def level_importer(name):
    objects = []

    for i in range(-1,len(name)):

        for j in range(-1,len(name[i])):
            
            if name[i][j] == 'x':
                block = Block(j*block_size,i*block_size,block_size,block_size,name='green block')
                objects.append(block)
                
            elif name[i][j] == 'D':
                player1 = Player(j*block_size,i*block_size,48,48,'1 Dog')
              
            elif name[i][j] == 'C':
                player2 = Player(j*block_size,i*block_size,48,48, '3 Cat')

            if name[i][j] == 'b':
                block = Block(j*block_size,i*block_size,block_size,block_size,name='brick')
                objects.append(block)

    return objects, player1, player2