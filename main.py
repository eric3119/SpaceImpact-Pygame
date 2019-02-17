#!/usr/bin/env python

import pygame

class Shot:
    """docstring for Shot"""
    
    ypos = 0
    xpos = 0

    def __init__(self, arg):
        super(Shot, self).__init__()
        self.arg = arg


def main():
    
    pygame.init()
    
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Space Impact")
    
    screen_width = 480
    screen_height = 320
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    ship = pygame.image.load("spaceship.png")
    shot = pygame.image.load("shot.png")
    
    # set the colorkey, so the pink border is not visible anymore
    # ship.set_colorkey((255,0,255))
    
    #initial position
    xpos = 20
    ypos = screen_height // 2 - 20
    
    step_x = 5
    step_y = 5
    
    screen.blit(ship, (xpos, ypos))
    
    pygame.display.flip()
    
    # a clock for controlling the fps
    clock = pygame.time.Clock()
    
    running = True

    still_down = False
    key_pressed = None

    xmax = screen_width - 54 #spaceship width
    ymax = screen_height - 40 #spaceship height
    
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
                #print("shot")

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
        
        screen.blit(ship, (xpos, ypos))
        screen.blit(shot, (xpos+54, ypos+17))
        
        pygame.display.flip()
        
        clock.tick(30)#fps
            
if __name__=="__main__":
    main()