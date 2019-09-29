import socket, threading
import pygame
import sys
import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
import RPi.GPIO as GPIO


max_value = 2000 #change this if your ESC's max value is different or leave it be
middle_value = 900
min_value = 700  #change this if your ESC's min value is different or leave it be

ESC=19 #Connect the ESC in this GPIO pin 
SPEED = 900
pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 
pi.set_servo_pulsewidth(ESC, max_value)
time.sleep(1)
pi.set_servo_pulsewidth(ESC, min_value)
time.sleep(1)
pi.set_servo_pulsewidth(ESC, min_value)
#control() 







class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
    def run(self):
        print ("Connection from : ", clientAddress)
        #self.csocket.send(bytes("Hi, This is from Server..",'utf-8'))
        SPEED = 900
        msg = ''
        middle_value = 900
        max_value = 160
        while True:
            
            data = self.csocket.recv(2048)
            msg = data.decode()
            if msg=='start':
              pi.set_servo_pulsewidth(ESC, SPEED)

            #print ("from client", msg)
            #self.csocket.send(bytes(msg,'UTF-8'))

            if msg=='stop':
              pi.set_servo_pulsewidth(ESC, 0)
              #pi.stop()

            if msg=='UPKEY':
              #SPEED += 1     # incrementing the speed 
              #pi.set_servo_pulsewidth(ESC, SPEED)
              pi.set_servo_pulsewidth(ESC, max_value)
              #if SPEED == 1500
               #  pi.set_servo_pulsewidth(ESC, max_value)
           # if msg=='UPKEYREALEASE':
              #SPEED =      # incrementing the speed 
              #pi.set_servo_pulsewidth(ESC, SPEED)


            if msg=='DOWNKEY':
              SPEED -= 1     # incrementing the speed 
              pi.set_servo_pulsewidth(ESC, SPEED)

            if msg=='NEUTRAL':
              #SPEED -= 10     # NEUTRAL speed 
              pi.set_servo_pulsewidth(ESC, middle_value)

            if msg=='bye':
                break
            print ("from client", msg)
            self.csocket.send(bytes(msg,'UTF-8'))





        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "192.168.1.58"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(1)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()
