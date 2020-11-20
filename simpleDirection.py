import pygame
from jetbot import Robot


robot = Robot()
maxSpeed = 0.3
   
pygame.init() 
   
win = pygame.display.set_mode((500, 500)) 
  
pygame.display.set_caption("Moving the JetBot") 
  
run = True

  
# infinite loop   
while run: 

    pygame.time.delay(10) 
  
    for event in pygame.event.get(): 
     
        if event.type == pygame.QUIT: 
            # it will make exit the while loop
            robot.stop
            print("quit")
            run = False
            
    keys = pygame.key.get_pressed() 
  
    if keys[pygame.K_LEFT] :
        print("left")
        robot.left (maxSpeed)
  
    if keys[pygame.K_RIGHT] :
        print("right")
        robot.right (maxSpeed)
  
    if keys[pygame.K_UP] : 
        print("forward")
        robot.forward (maxSpeed)

    if keys[pygame.K_DOWN] : 
        print("backward")
        robot.backward (maxSpeed)    
  
    if keys[pygame.K_SPACE] :
        print("stop")
        robot.set_motors(0,0)
  
     #pygame.display.update() 

pygame.quit()  
