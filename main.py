import pygame
pygame.init()

from constants import *
from levels import *
from asset_loader import get_BG
from funcs import handle_vertical_collision, handle_move, level_importer



pygame.display.set_caption('Platformer')

WN =  pygame.display.set_mode((wn_width, wn_height))



def main(WN):
    clock = pygame.time.Clock()
    cordinates, BG_image = get_BG('Yellow.png')
    offset_x = 0
    player_choise = '1'
    objects, player1, player2 = level_importer(map1)



    Run = True
    while Run:
        clock.tick(FPS)

        if player_choise == '1':
            player = player1
        elif player_choise == '2':
            player = player2


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False
                break
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    player_choise = '1'
                if event.key == pygame.K_2:
                    player_choise = '2'
                if (event.key == pygame.K_SPACE or event.key == pygame.K_w) and player.jump_count < 2:
                    player.jump()
                if event.key == pygame.K_k and player.attack_count < 1:
                   player.attack()


        # functionalities
        player1.loop(FPS)
        player2.loop(FPS)
        player1.update_sprite()
        player2.update_sprite()
        handle_vertical_collision(player1, objects, player1.y_vel)
        handle_vertical_collision(player2, objects, player2.y_vel)
        handle_move(player, objects)
        
        
        if ((player.rect.right  >= wn_width + offset_x - scroll_area_width) and player.x_vel > 0) or (
            (player.rect.left  <= scroll_area_width + offset_x) and player.x_vel < 0):
            offset_x += player.x_vel



        # drawing
        for cordinate in cordinates:
            WN.blit(BG_image, cordinate)

        for block in objects:
            block.draw(WN, offset_x)

        player1.draw(WN, offset_x)
        player2.draw(WN, offset_x)

        pygame.display.update()

    pygame.quit()
    quit()



if __name__ == '__main__':
    main(WN)



