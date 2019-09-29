import pygame
from pygame.locals import *
import cv2
import numpy as np
import sys
import socket

camera = cv2.VideoCapture("udp://@192.168.1.58:5000?overrun_nonfatal=1&fifo_size=5000000")
pygame.init()
pygame.display.set_caption("OpenCV camera stream on Pygame")
screen = pygame.display.set_mode([640,480])
SERVER = "192.168.1.58"
PORT = 8080
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
client.sendall(bytes("This is from Client",'UTF-8'))



try:
   run = True

   while run:
       #pygame.time.delay(100)
       ret, frame = camera.read()
       screen.fill([0,0,0])
       frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
       frame = np.rot90(frame)
       frame = pygame.surfarray.make_surface(frame)
       screen.blit(frame, (0,0))
       pygame.display.update()
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False
           if event.type == KEYUP and event.key == K_UP:
               print ("okUPrealeased")
               in_data =  client.recv(2048)
               #print("From Server :" ,in_data.decode())
               out_data = ("NEUTRAL")
               client.sendall(bytes(out_data,'UTF-8'))
           if event.type == KEYUP and event.key == K_DOWN:
               print ("okDownrealeased")
               in_data =  client.recv(2048)
               #print("From Server :" ,in_data.decode())
               out_data = ("NEUTRAL")
               client.sendall(bytes(out_data,'UTF-8'))
       keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

    


       if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
          print ("okleft")
       if keys[pygame.K_RIGHT]:
          print ("okright")
       if keys[pygame.K_UP]:
          print ("okup")
          in_data =  client.recv(2048)
       #print("From Server :" ,in_data.decode())
          out_data = ("UPKEY")
          client.sendall(bytes(out_data,'UTF-8'))
       if keys[pygame.K_DOWN]:
          print ("okdown")
          in_data =  client.recv(2048)
       #print("From Server :" ,in_data.decode())
          out_data = ("DOWNKEY")
          client.sendall(bytes(out_data,'UTF-8'))
       if keys[pygame.K_t]:
          print ("okTpressed")
          in_data =  client.recv(2048)
          #print("From Server :" ,in_data.decode())
          out_data = ("start")
          client.sendall(bytes(out_data,'UTF-8'))
       if keys[pygame.K_l]:
          print ("okLpressed")
          in_data =  client.recv(2048)
          #print("From Server :" ,in_data.decode())
          out_data = ("stop")
          client.sendall(bytes(out_data,'UTF-8'))
    #if not keys[pygame.K_l]:
     #  in_data =  client.recv(2048)
       #print("From Server :" ,in_data.decode())
      # out_data = ("neutral")
       #client.sendall(bytes(out_data,'UTF-8'))

    #pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    #pygame.display.update() 
except (KeyboardInterrupt,SystemExit):
            pygame.quit()
            cv2.destroyAllWindows()

