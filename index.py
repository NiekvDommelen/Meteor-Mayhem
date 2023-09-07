import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode(flags=pygame.FULLSCREEN)

width = screen.get_width()

height = screen.get_height()

clock = pygame.time.Clock()

#sounds
hit_sound = pygame.mixer.Sound("assets/sound/hit.wav")
lazer_sound = pygame.mixer.Sound("assets/sound/lazer.wav")
pygame.mixer.music.load("assets/sound/music.wav")

# states
running = True
menu = True
playing = False
settings = False
paused = False
game_over = False

clicking = False

dt = 0

smallfont = pygame.font.SysFont('Corbel',35)

bigfont = pygame.font.SysFont('Corbel',70)

boldfont = pygame.font.SysFont('Corbel',100)

text_raw = ["play","quit", "settings", "amount of asteroids", "speed of asteroids", "speed of player", "esc"]
big_text_raw = ["paused","game over"]

text = [[] for i in range(len(text_raw))]
big_text = [[] for i in range(len(big_text_raw))]

for x in range(len(big_text_raw)):
    big_text[x] = bigfont.render(big_text_raw[x], True, "white")

for x in range(len(text_raw)):
    text[x] = smallfont.render(text_raw[x], True, "white")
    

plus = smallfont.render("+", True, "white")
minus = smallfont.render("-", True, "white")


plane_x, plane_y = 100, 300
plane_img = pygame.image.load('assets/img/plane.png')
background = pygame.image.load('assets/img/background.png')
asteroid_img = pygame.image.load('assets/img/asteroid.png')
menu_img = pygame.image.load('assets/img/menu.png')

background = pygame.transform.scale(background, (width, height))
menu_img = pygame.transform.scale(menu_img, (width, height))


asteroid_img = pygame.transform.scale(asteroid_img, (100, 100))

lazer = 0
shooting = False



def enemiesReset():
     for e in range(len(enemies)):
        enemies[e][1] = random.randint(80, 720)
        enemies[e][0] = width + random.randint(0, 500)
        enemies[e][2] = random.randint(0, 6)

enemiesNum = 8




enemies = [[0,0,0] for i in range(enemiesNum)]


for e in range(enemiesNum):
    enemies[e][1] = random.randint(80, 720)
    enemies[e][0] = width + random.randint(0, 500)



score = 0


player_speed = 10
asteroid_speed = 2





while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    
    pygame.mixer.music.play(-1)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    


        screen.fill("black")

        screen.blit(menu_img, (0, 0, height, width))

        mouse = pygame.mouse.get_pos()

        #menu

        if game_over:
            if width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: #play
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2,140,40])

            elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+200 <= mouse[1] <= height/2+240: #quit
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2 + 200,140,40])
            
            elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+100 <= mouse[1] <= height/2+140: #settings
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2 + 100,140,40])

            screen.blit(big_text[1] , (width/2 - 150, 200)) #paused

            txtScore = smallfont.render(f'score:{score}', True, (255, 255, 255))

            screen.blit(txtScore, (width/2 - 50, 300))    

                

            screen.blit(text[2] , (width/2 - 58,height/2 + 104)) #settings

            screen.blit(text[0] , (width/2 - 30,height/2 + 4)) #play
            
            screen.blit(text[1] , (width/2 - 30,height/2 + 204)) #quit


            #actions

            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 - 70 <= mouse[0] <= width/2+70 and height/2+200 <= mouse[1] <= height/2+240: #quit
                    menu = False
                    running = False

                elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: #play
                    score = 0
                    playing = True
                    menu = False

                elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+100 <= mouse[1] <= height/2+140: #settings
                    settings = True
                    menu = False

        elif paused:
            if width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: #play
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2,140,40])

            elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+100 <= mouse[1] <= height/2+240: #quit
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2 + 100,140,40])

            screen.blit(big_text[0] , (width/2 - 100, 200)) #paused

            screen.blit(text[0] , (width/2 - 30,height/2 + 4)) #play

            screen.blit(text[1] , (width/2 - 30,height/2 + 104)) #quit


            #actions

            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 - 70 <= mouse[0] <= width/2+70 and height/2+100 <= mouse[1] <= height/2+140: #quit
                    enemiesReset()
                    score = 0
                    paused = False
                    time.sleep(0.1)
                    

                elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: #play
                    playing = True
                    menu = False
            
        else:      
        
            if width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: #play
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2,140,40])

            elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+200 <= mouse[1] <= height/2+240: #quit
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2 + 200,140,40])
            
            elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+100 <= mouse[1] <= height/2+140: #settings
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 70,height/2 + 100,140,40])

            
            title = boldfont.render("Meteor Mayhem", True, (255, 255, 255))

            screen.blit(title, (width/2 - 320, 250))

            screen.blit(text[2] , (width/2 - 58,height/2 + 104)) #settings

            screen.blit(text[0] , (width/2 - 30,height/2 + 4)) #play
            
            screen.blit(text[1] , (width/2 - 30,height/2 + 204)) #quit


            #actions

            if event.type == pygame.MOUSEBUTTONDOWN:
                if width/2 - 70 <= mouse[0] <= width/2+70 and height/2+200 <= mouse[1] <= height/2+240: #quit
                    menu = False
                    running = False

                elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2 <= mouse[1] <= height/2+40: #play
                    playing = True
                    menu = False

                elif width/2 - 70 <= mouse[0] <= width/2+70 and height/2+100 <= mouse[1] <= height/2+140: #settings
                    settings = True
                    menu = False
            
        dt = clock.tick(60)

        pygame.display.flip()

    while settings:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")

        if width/2 - 70 <= mouse[0] <= width/2+70 and height/2+300 <= mouse[1] <= height/2+340: #esc
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 35,height/2 + 300,60,40])

        elif width/2 - 136 <= mouse[0] <= width/2 - 74 and height/2+244 <= mouse[1] <= height/2+294: #speed of player +
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 135,height/2 + 244,60,40])
        elif width/2 + 74 <= mouse[0] <= width/2 + 136 and height/2+244 <= mouse[1] <= height/2+294: #speed of player -
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 + 74,height/2 + 244,60,40])

        elif width/2 - 136 <= mouse[0] <= width/2 - 74 and height/2+144 <= mouse[1] <= height/2+194: #speed of asteroid +
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 135,height/2 + 144,60,40])
        elif width/2 + 74 <= mouse[0] <= width/2 + 136 and height/2+144 <= mouse[1] <= height/2+194: #speed of asteroid -
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 + 74,height/2 + 144,60,40])

        elif width/2 - 136 <= mouse[0] <= width/2 - 74 and height/2+44 <= mouse[1] <= height/2+94: #amount of asteroids +
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 - 135,height/2 + 44,60,40])
        elif width/2 + 74 <= mouse[0] <= width/2 + 136 and height/2+44 <= mouse[1] <= height/2+94: #amount of asteroids -
                pygame.draw.rect(screen,(69 ,69 ,69),[width/2 + 74,height/2 + 44,60,40])


                
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 - 70 <= mouse[0] <= width/2+70 and height/2+300 <= mouse[1] <= height/2+340: #esc
                
                settings = False
                menu = True
            elif width/2 - 136 <= mouse[0] <= width/2 - 74 and height/2+244 <= mouse[1] <= height/2+294: #speed of player -
                    if not clicking and player_speed > 1:
                        player_speed -= 1
            elif width/2 + 74 <= mouse[0] <= width/2 + 136 and height/2+244 <= mouse[1] <= height/2+294: #speed of player +
                    if not clicking:
                    
                        player_speed += 1

            elif width/2 - 136 <= mouse[0] <= width/2 - 74 and height/2+144 <= mouse[1] <= height/2+194: #speed of asteroid -
                    if not clicking and asteroid_speed > 1:
                    
                        asteroid_speed -= 1
            elif width/2 + 74 <= mouse[0] <= width/2 + 136 and height/2+144 <= mouse[1] <= height/2+194: #speed of asteroid +
                    if not clicking: 
                    
                        asteroid_speed += 1

            elif width/2 - 136 <= mouse[0] <= width/2 - 74 and height/2+44 <= mouse[1] <= height/2+94: #amount of asteroids -
                    if not clicking and enemiesNum > 1:
                    
                        enemiesNum -= 1
            elif width/2 + 74 <= mouse[0] <= width/2 + 136 and height/2+44 <= mouse[1] <= height/2+94: #amount of asteroids +
                    if not clicking:
                         
                        enemiesNum += 1
            clicking = True

        if event.type == pygame.MOUSEBUTTONUP:
            clicking = False

        screen.blit(text[3] , (width/2 - 140,height/2 + 4)) #amount of asteroids
        screen.blit(smallfont.render(f'{enemiesNum}', True, "white") , (width/2 - 20,height/2 + 44)) #amount
        
        screen.blit(minus , (width/2 - 110,height/2 + 44)) #minus
        screen.blit(plus , (width/2 + 95,height/2 + 44)) #plus


        screen.blit(text[4] , (width/2 - 130,height/2 + 104)) #speed of asteroids
        screen.blit(smallfont.render(f'{asteroid_speed}', True, "white") , (width/2 - 20,height/2 + 144)) #amount

        screen.blit(minus , (width/2 - 110,height/2 + 144)) #minus
        screen.blit(plus , (width/2 + 95,height/2 + 144)) #plus

        screen.blit(text[5] , (width/2 - 115,height/2 + 204)) #speed of player
        screen.blit(smallfont.render(f'{player_speed}', True, "white") , (width/2 - 20,height/2 + 244)) #amount

        screen.blit(minus , (width/2 - 110,height/2 + 244)) #minus
        screen.blit(plus , (width/2 + 95,height/2 + 244)) #plus

        screen.blit(text[6] , (width/2 - 30,height/2 + 304)) #esc

        mouse = pygame.mouse.get_pos()  
        
        

        pygame.display.flip()

        dt = clock.tick(60)

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if enemiesNum > len(enemies):
             newEnemies = enemiesNum - len(enemies)
             for e in range(newEnemies):
                enemies.append([width + random.randint(0, 500),random.randint(80, 720),0])
    
        screen.fill("black")

        screen.blit(background, (0, 0, height, width))
    
        screen.blit(plane_img, (plane_x, plane_y))
        for e in range(enemiesNum):
            
            screen.blit(asteroid_img, (enemies[e][0], enemies[e][1]))
           
        
        

        keys = pygame.key.get_pressed()
        

        if keys[pygame.K_w]: #Up
            if plane_y >= 0:
                plane_y -=  player_speed
        if keys[pygame.K_s]: #Down
            if plane_y <= height - 50:
                plane_y +=  player_speed
        if keys[pygame.K_a]: #Left
            if plane_x >= 0:
                plane_x -=  player_speed
        if keys[pygame.K_d]: #Right
            if plane_x <= width - 100:
                plane_x +=  player_speed
        if keys[pygame.K_SPACE] or event.type == pygame.MOUSEBUTTONDOWN: #Shoot
            if not shooting:
                pygame.mixer.Sound.play(lazer_sound)
                
                shooting = True
                fire = True
        if keys[pygame.K_ESCAPE]: #Esc
            playing = False
            paused = True
            menu = True
    
        
            

        if shooting:
            lazer += 50
            if fire:
                lazer_y = plane_y + 35
                lazer_x = plane_x + 35
                fire = False
            pygame.draw.rect(screen, (255, 0, 0), (lazer_x + lazer , lazer_y, lazer/2 , 5))
            if lazer > width:
                lazer = 0
                shooting = False
                fire = False
            for e in range(len(enemies)):
                
                if lazer_y >= enemies[e][1] and lazer_y <= enemies[e][1] + 100 and lazer_x + lazer *2 >= enemies[e][0] and lazer_x <= enemies[e][0]:
                    pygame.mixer.Sound.play(hit_sound)
                    score += 1
                    enemies[e][1] = random.randint(80, 720)
                    enemies[e][0] = width + random.randint(0, 500)
                    enemies[e][2] = random.randint(0, 6)
            pygame.draw.rect(screen, (0, 255, 0), (0, 0, (lazer) , 15))
                    
        txtScore = smallfont.render(f'score:{score}', True, (255, 255, 255))

        screen.blit(txtScore, (50, 50))            
            


        for e in range(len(enemies)):
            if enemies[e][2] == 1: #Going down
                if enemies[e][1] >= height - 100:
                    enemies[e][2] = 2
                enemies[e][1] += 2
            if enemies[e][2] == 2: #Going up
                if enemies[e][1] <= 0:
                    enemies[e][2] = 1
                enemies[e][1] -= 2

            if enemies[e][2] == 3: #Going fast
                enemies[e][0] -= asteroid_speed * 2

            enemies[e][0] -= asteroid_speed
            if enemies[e][0] <= 0: #game over
                enemiesReset()
                playing = False
                menu = True
                game_over = True
        
        pygame.display.flip()

        
        dt = clock.tick(60)
