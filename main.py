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
    
    # set the colorkey, so the pink border is not visible anymore
    # ship.set_colorkey((255,0,255))
    
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
    enemies = []
    enemy_limit = 3
    enemy_control = 0 #time
    collisions = [[0 for x in range(screen_width)] for y in range(screen_height)]

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

        if len(enemies) < enemy_limit:
            enemies.append(enemy.Enemy(xpos = screen_width, ypos= random.random()*screen_height))
        
        for enem in enemies:
            screen.blit(enemy_img, (enem.xpos, enem.ypos))
            enem.update()
            #colision enemy ship
            if enem.xpos < xpos + ship_img.get_width() and enem.xpos + ship_img.get_height() > xpos and enem.ypos < ypos + ship_img.get_height() and ship_img.get_width() + enem.ypos > ypos:
                running = False
            #colision enemy shot
            for projec in shots:
                if projec.xpos < enem.xpos + enemy_img.get_width() and projec.xpos + shot_img.get_width() > enem.xpos and projec.ypos < enem.ypos + enemy_img.get_height() and shot_img.get_width() + projec.ypos > enem.ypos:
                    enem.destroy()
                    projec.destroy()

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