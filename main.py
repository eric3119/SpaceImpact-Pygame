#!/usr/bin/env python

import pygame

class Shot(object):
    """docstring for Shot"""

    
    def __init__(self, arg):
        super(Shot, self).__init__()
        self.arg = arg


def main():
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("Space Impact")
    
    # create a surface on screen that has the size of 240 x 180
    screen_width = 480
    screen_height = 320
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # load image (it is in same directory)
    ship = pygame.image.load("spaceship.png")
    shot = pygame.image.load("shot.png")
    # set the colorkey, so the pink border is not visible anymore
    ship.set_colorkey((255,0,255))
    # set the alpha value to 128 (0 fully transparent, 255 opaque)
    
    #bgd_image = pygame.image.load("background.png")
    
    # blit image(s) to screen
    #screen.blit(bgd_image,(0,0)) # first background
    # instead of blitting the background image you could fill it 
    # (uncomment the next line to do so)
    #screen.fill((0,0,0))
    
    
    # define the position of the smily
    xpos = 50
    ypos = 50
    # how many pixels we move our smily each frame
    step_x = 5
    step_y = 5
    
    # and blit it on screen
    screen.blit(ship, (xpos, ypos))
    
    # update the screen to make the changes visible (fullscreen update)
    pygame.display.flip()
    
    # a clock for controlling the fps later
    clock = pygame.time.Clock()
    
    # define a variable to control the main loop
    running = True
    still_down = False
    key_pressed = None
    # main loop
    while running:
        # event handling, gets all event from the eventqueue
        # for event in pygame.event.get():
        #     # only do something if the event if of type QUIT
        #     if event.type == pygame.QUIT:
        #         # change the value to False, to exit the main loop
        #         running = False
        #     # check for keypress and check if it was Esc
        #     if event.type == pygame.KEYUP:
        #         print("up")
        #         still_down = False  

        #     if event.type == pygame.KEYDOWN:
        #         print("down")
                
        #         still_down = True                
        #         key_pressed = event.key

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
                print("shot")
                evento = None
            if evento:
                if still_down:                
                    pygame.event.post(evento)
                else:
                    still_down = True                
                    arrow_pressed = evento.key               

        if still_down:
            if arrow_pressed == pygame.K_UP:
                ypos -= step_y                    
            elif arrow_pressed == pygame.K_DOWN:
                ypos += step_y 
            elif arrow_pressed == pygame.K_LEFT:
                xpos -= step_x 
            elif arrow_pressed == pygame.K_RIGHT:
                xpos += step_x      
        # check if the smily is still on screen, if not change direction
        # if xpos>screen_width-64 or xpos<0:
        #     step_x = -step_x
        # if ypos>screen_height-64 or ypos<0:
        #     step_y = -step_y
        # # update the position of the smily
        # xpos += step_x # move it to the right
        # ypos += step_y # move it down
        
        screen.fill((116,166,129))
        # first erase the screen (just blit the background over anything on screen)
     #   screen.blit(bgd_image, (0,0))
        # now blit the smily on screen
        screen.blit(ship, (xpos, ypos))
        screen.blit(shot, (xpos+54, ypos+17))
        # and update the screen (dont forget that!)
        pygame.display.flip()
        
        # this will slow it down to 10 fps, so you can watch it, 
        # otherwise it would run too fast
        clock.tick(20)
            
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()