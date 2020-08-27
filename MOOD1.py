# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:40:06 2020

@author: MAJOJU KRISHNA SAI PRAHLAD 
A  very beginner game to understand pygame explorers 
"""

import pygame as py 
py.init()
#setting the window (interface to be displayed)
mode = py.display.set_mode((700,500))
py.display.set_caption("GET YOUR MOOD")
#defining colors 
white = (255, 255, 255) 
green = (0, 255, 0)
blue = (0, 0, 128)
#setting background for the window 
bg=py.image.load('bg2.png')
#font settings 
#selection of type of font 
font = py.font.SysFont('Times New Roman', 32) 
text = font.render('SELECT YOUR MOOD',True, green, blue)
font2 = py.font.SysFont('Times New Roman', 18)
#getting into the text fields 
text2 = font2.render('FUN',True, green, blue)
text3 = font2.render('BORED',True , green,blue)
text4 = font2.render('SAD',True,green,blue)
textRect = text.get_rect() 
textRect2 = text2.get_rect() 
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect.center= (350,20)
textRect2.center = (200,50)
textRect3.center = (330,50)
textRect4.center = (460,50)
#UI  part is completed
#Setting the images(characters to be played)
Right = [py.image.load('R1.png'),py.image.load('R2.png'),py.image.load('R3.png'),py.image.load('R4.png'),py.image.load('R5.png'),py.image.load('R6.png'),py.image.load('R7.png'),py.image.load('R8.png'),py.image.load('R9.png')]
Left = [py.image.load('L1.png'),py.image.load('L2.png'),py.image.load('L3.png'),py.image.load('L4.png'),py.image.load('L5.png'),py.image.load('L6.png'),py.image.load('L7.png'),py.image.load('L8.png'),py.image.load('L9.png')] 
#Characters to be included in the game 
char1= py.image.load('standing1.jpg')  # 2 runners are included 
char2= py.image.load('standing2.jpg')
class player1(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.walk=0
        self.vel=2
        self.left=False
        self.right=False 
        self.jump=False
        self.count1=10
        self.c1=10
    #function for activities 
    def draw(self,mode):
        if self.walk + 1 >=27:
            self.walk = 0
        if self.left :
            mode.blit(Left[self.walk//3],(self.x,self.y))
            self.walk+=1
        elif self.right :
            mode.blit(Right[self.walk//3],(self.x,self.y))
            self.walk+=1
        else :
            mode.blit(char1,(self.x,self.y))
#completed the code for class of player1
#class for 2nd character (player) 
class player2(object):
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width 
        self.height=height 
        self.left=False
        self.right=False 
        self.jump=False 
        self.vel=2
        self.walk=0
        self.count2=10 
        self.c2=10
    #function for activities 
    def draw(self,mode):
        if self.walk + 1 >=27:
            self.walk = 0
        if self.left :
            mode.blit(Left[self.walk//3],(self.x,self.y))
            self.walk+=1
        elif self.right :
            mode.blit(Right[self.walk//3],(self.x,self.y))
            self.walk+=1
        else :
            mode.blit(char2,(self.x , self.y))
def redrawGameWindow():
    p1.draw(mode)
    p2.draw(mode)
    py.display.update()
#defining the objects for Two players and also the initial position into the window 
p1=player1(200,400,64,64)
p2=player2(400,400,64,64)
run=True 
while run:
    #Setting the back groud image for window 
    mode.blit(bg,(0,0))
    #getting the text fields onto the window 
    mode.blit(text, textRect) 
    #drawing circles (moods(colors))
    py.draw.circle(mode,green,(200,80),15)
    mode.blit(text2, textRect2)
    mode.blit(text3, textRect3)
    py.draw.circle(mode,white,(330,80),15)
    mode.blit(text4, textRect4)
    py.draw.circle(mode,blue,(460,80),15)
    for event in py.event.get():
        #Condition forclosing the window (if you miss this line the window never closes )
        if event.type == py.QUIT:
            run=False
    #method to keyboard events 
    keys = py.key.get_pressed()
    if keys[py.K_y]:
        print("YEllow ismpresed")
        #methods to play music 
        music=py.mixer.music.load('music.mp3')
        py.mixer.music.play()
    if keys[py.K_LEFT] and p1.x>p1.vel and p2.x>p2.vel:
        p1.x-=p1.vel
        #Getting the moments of right and left moments 
        p1.left=True
        p1.right=False
        p2.right=True
        p2.x+=p2.vel
        p2.left=False
    elif keys[py.K_RIGHT] and p1.x<700 - p1.vel - p1.width and p2.x<700 - p2.vel - p2.width:
        p1.x+=p1.vel
        p1.right=True
        p1.left=False
        p2.left=True
        p2.x-=p2.vel
        p2.right=False
    else:
        p1.right=False
        p1.left=False
        p2.left=False 
        p2.right=False 
        p1.walk=0
        p2.walk=0
    if keys[py.K_w]:
        print("White is pressed")
    if not p1.jump:
        if keys[py.K_SPACE]:
            #Making the moment constant by the below count and multplication operations 
            p1.jump=True
            p2.jump=True
            p1.right=False
            p2.right=False
            p1.left=False
            p2.left=False 
            p1.walk = 0
            p2.walk = 0
    else :
         if p1.c1 >= -8 and p2.c2 >=-8:
             n=1
             if p1.c1 <0 and p2.c2 <0:
                 n=-1
             p1.y-=(p1.c1 ** 2)*0.05 *n
             p1.x+=(p1.c1 ** 2)*0.05 *n
             p2.y-=(p2.c2 ** 2)*0.05 *n
             p2.x-=(p2.c2 ** 2)*0.05 *n
             p1.c1 -= 1
             p2.c2 -= 1
         else :
             p1.c1=10
             p2.c2=10
             p1.jump=False
             p2.jump=False
    if keys[py.K_b]:
        print("Blue is pressed")
    if not p1.jump:
        if keys[py.K_DOWN]:
            #making the moment to jump opposite to each player such that tehy can reach the flag 
            p1.jump=True
            p2.jump=True
            p1.right=False
            p2.right=False
            p1.left=True
            p2.left=True
            p1.walk = 0
            p2.walk = 0
    else :
         if p1.count1 <= -8 and p2.count2 <=-8:
             n=1
             if p1.count1 >0 and p2.count2 >0:
                 n=-1
                 #As you increase this number the speed and height of the player while jumping increases 
             p1.y+=(p1.count1 ** 2)*0.05 *n
             p1.x+=(p1.count1 ** 2)*0.05 *n
             p2.y+=(p2.count2 ** 2)*0.05 *n
             p2.x-=(p2.count2 ** 2)*0.05 *n
             p1.count1 -= 1
             p2.count2 -= 1
         else :
             p1.count1=10
             p2.count2=10
             p1.jump=False
             p2.jump=False
    #updating all these operations on to the window by calling this function
    redrawGameWindow()
py.quit()