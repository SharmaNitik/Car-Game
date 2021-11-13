import pygame
def collision(carX, carY, enemy_car_X, enemy_car_Y):
    dist = ((carX - enemy_car_X)**2 + (enemy_car_Y -carY)**2 )**(0.5)
    if dist<27:
        return True
    else:
        return False

def scoreboard(count, screen):
    font = pygame.font.Font('freesansbold.ttf', 32)
    font = font.render(("Score: "+ str(count)), True, (255,255,255))
    screen.blit(font, (0,0))

def game_over(screen,screenX,screenY):
    game_over = pygame.font.Font('freesansbold.ttf', 50)
    game_over = game_over.render(("GAME OVER"), True, (255,255,255))
    screen.blit(game_over, (30, screenY/2-40))




