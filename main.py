#!/usr/bin/env python
__author__    = "$Author: DR0ID $"
__version__   = "$Revision: 112 $"
__date__      = "$Date: 2007-04-03 18:09:43 +0200 (Di, 03 Apr 2007) $"
__license__   = 'public domain'
__copyright__ = "DR0ID (c) 2007   http://mypage.bluewin.ch/DR0ID"


import pygame

def main():
    
    # initialize the pygame module
    pygame.init()
    
    # load and set the logo
    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("movement")
    
    # create a surface on screen that has the size of 240 x 180
    screen_width = 480
    screen_height = 320
    screen = pygame.display.set_mode((screen_width, screen_height))
    
    # load image (it is in same directory)
    image = pygame.image.load("space.png")
    # set the colorkey, so the pink border is not visible anymore
    image.set_colorkey((255,0,255))
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
    screen.blit(image, (xpos, ypos))
    
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
            print("up")
            still_down = False

        if evento.type == pygame.KEYDOWN:
            print("down")
            if still_down:                
                pygame.event.post(evento)
            else:
                still_down = True                
                key_pressed = evento.key               

        if still_down:
            print("action")
            if key_pressed == pygame.K_ESCAPE:
                running = False
            elif key_pressed == pygame.K_UP:
                ypos -= step_y                    
            elif key_pressed == pygame.K_DOWN:
                ypos += step_y 
            elif key_pressed == pygame.K_LEFT:
                xpos -= step_x 
            elif key_pressed == pygame.K_RIGHT:
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
        screen.blit(image, (xpos, ypos))
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