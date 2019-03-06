#!/usr/bin/env python

import pygame
import shot
import enemy
import random

def main():
    
    pygame.init()
    
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Space Impact")
    
    screen_width = 480
    screen_height = 320
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    ship_img = pygame.image.load("spaceship.png")
    enemy_img = pygame.image.load("enemy.png")
    shot_img = pygame.image.load("shot.png")
        
    #initial position
    xpos = 20
    ypos = screen_height // 2 - 20
    
    step_x = 5
    step_y = 5
    
    screen.blit(ship_img, (xpos, ypos))
    
    pygame.display.flip()
    
    # a clock for controlling the fps
    clock = pygame.time.Clock()
    
    running = True

    shots = []

    display_score = pygame.font.Font(pygame.font.get_default_font(), 20)
    score = 0
    
    enemies = []
    enemy_time = 400
    enemy_control = 0 #time    
    enemy_max_speed = 5    

    still_down = False
    key_pressed = None

    xmax = screen_width - ship_img.get_width() #spaceship width
    ymax = screen_height - ship_img.get_height() #spaceship height
    
    while running:
        
        evento = pygame.event.poll()

        if evento.type == pygame.QUIT:            
            running = False
            
        if evento.type == pygame.KEYUP:
            if evento.key != pygame.K_SPACE:
                still_down = False

        if evento.type == pygame.KEYDOWN:
            
            if evento.key == pygame.K_ESCAPE:
                running = False                

            if evento.key == pygame.K_SPACE:
                shots.append(shot.Shot(xpos+ship_img.get_width(), ypos+(ship_img.get_height()//2 - shot_img.get_height()//2)))
                evento = None
            if evento:
                if still_down:                
                    pygame.event.post(evento)
                else:
                    still_down = True                
                    arrow_pressed = evento.key               

        if still_down:
            if arrow_pressed == pygame.K_UP and ypos > 0:
                ypos -= step_y                    
            elif arrow_pressed == pygame.K_DOWN and ypos < ymax:
                ypos += step_y 
            elif arrow_pressed == pygame.K_LEFT and xpos > 0:
                xpos -= step_x 
            elif arrow_pressed == pygame.K_RIGHT and xpos < xmax:
                xpos += step_x      
                
        screen.fill((116,166,129))
        
        screen.blit(ship_img, (xpos, ypos))

        for projec in shots:
            screen.blit(shot_img, (projec.xpos, projec.ypos))
            projec.update(boundary = screen_width)
        
        if (pygame.time.get_ticks() - enemy_control) >= enemy_time:            
            enemy_control = pygame.time.get_ticks()
            enemies.append(enemy.Enemy(xpos = screen_width, ypos= random.random()*(screen_height-enemy_img.get_height()), speed=(random.random()+1)*enemy_max_speed))
        
        for target in enemies:
            screen.blit(enemy_img, (target.xpos, target.ypos))
            target.update()
            #colision enemy ship
            if target.xpos < xpos + ship_img.get_width() and target.xpos + ship_img.get_height() > xpos and target.ypos < ypos + ship_img.get_height() and ship_img.get_width() + target.ypos > ypos:
                running = False
            #colision enemy shot
            for projec in shots:
                if projec.xpos < target.xpos + enemy_img.get_width() and projec.xpos + shot_img.get_width() > target.xpos and projec.ypos < target.ypos + enemy_img.get_height() and shot_img.get_width() + projec.ypos > target.ypos:
                    target.destroy()
                    projec.destroy()
                    score+=1                    

        f = display_score.render("Destruidos: "+str(score), True, [0, 0, 0], [116,166,129])

        screen.blit(f, ((screen_width//2)-(display_score.size("Destruidos: "+str(score))[0]//2),0))
        pygame.display.flip()

        for i in range(len(shots)):
            try:
                if not shots[i].isOnScreen():
                    del shots[i]
            except IndexError:
                pass
        for i in range(len(enemies)):
            try:
                if not enemies[i].isOnScreen():
                    del enemies[i]
            except IndexError:
                pass
        
        
        clock.tick(30)#fps
    #end running    
if __name__=="__main__":    
    main()