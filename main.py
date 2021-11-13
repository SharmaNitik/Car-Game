import pygame, collide
from random import randint
pygame.init()
screenX = 360
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

car = pygame.image.load('car.png') # 50,100
carX = screenX/2 + 50
carY = screenY - 100 
carX_change = 0
carY_change = 0

enemy_car_1 = pygame.image.load('enemy_car_1.png')
enemy_car_1 = pygame.transform.flip(enemy_car_1, False,True)
enemy_car_X = randint(screenX/2 - 95,screenX/2 + 50)
enemy_car_Y = 0
enemy_car_change = .5

count = 0
background = pygame.image.load('back_ground.jpg')
running = True
while running:
    screen.blit(background, (screenX/2-180,0))
    for event in pygame.event.get():        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            if event.key == pygame.K_LEFT:
                carX_change = -0.2      
            if event.key == pygame.K_RIGHT:
                carX_change = 0.2
            if event.key == pygame.K_UP:
                carY_change = -0.2
            if event.key == pygame.K_DOWN:
                carY_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                carX_change = 0 
                carY_change = 0

    carX += carX_change
    carY += carY_change
    screen.blit(car,(carX, carY))
    if carX <= screenX/2 - 95:
        carX = screenX/2 - 95
    if carX >= screenX/2 + 50:
        carX = screenX/2 + 50
    
    enemy_car_Y += enemy_car_change
    screen.blit(enemy_car_1, ( enemy_car_X, enemy_car_Y))
    if enemy_car_Y >= screenY:
        count += 1
        enemy_car_Y = 0
        enemy_car_X = randint(screenX/2 - 95,screenX/2 + 50)
    if collide.collision(carX, carY, enemy_car_X, enemy_car_Y):
        collide.game_over(screen,screenX,screenY)
        pygame.display.update() 
        pygame.time.wait(2000) # in miliseconds
        running = False
    collide.scoreboard(count, screen)
    pygame.display.update() 