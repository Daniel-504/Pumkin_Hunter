import pygame
pygame.init()
import random
from pygame import mixer

small_font=pygame.font.SysFont("Chiller",35)
medium_font=pygame.font.SysFont("Chiller",100)
big_font=pygame.font.SysFont("Chiller",200)
medium_font=pygame.font.SysFont("comicsansms", 72)
#colors
red=(255,0,0)
dark_red=(155,0,0)
green=(0,255,0)
blue=(0,0,255)
gray=(25,25,25)
brick_color=(200,100,100)
black=(0,0,0)
yellow=(255,255,0)
purple=(255,0,255)






def print_big(my_str,color,str_x,str_y):
    str_x=int(str_x)
    str_y=int(str_y)
    mytext=big_font.render(my_str,1,color)
    win.blit(mytext,(str_x,str_y))
def print_med(my_str,color,str_x,str_y):
    str_x=int(str_x)
    str_y=int(str_y)
    mytext=medium_font.render(my_str,1,color)
    win.blit(mytext,(str_x,str_y))
def print_small(my_str,color,str_x,str_y):
    str_x=int(str_x)
    str_y=int(str_y)
    mytext=small_font.render(my_str,1,color)
    win.blit(mytext,(str_x,str_y))

def select_player():
    pygame.draw.rect(win,black,(0,0,1200,800))
    wait=True
    choise=1  
    while wait:
        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
        pygame.time.delay(50)
        print_med("Emma , the Pumpkin-hunter:",red,10,50)
        print_med("Please select your character:",red,10,200)
        if choise == 1:
            print_small("Emma",red,50,600)
            print_small("Eddie",dark_red,200,600)
        if choise == 2:
            print_small("Emma",dark_red,50,600)
            print_small("Eddie",red,200,600)
        if choise ==1:
            win.blit(emma_front,(50,500))
        else:
            win.blit(emma_front_gray,(50,500))
        if choise ==2:
            win.blit(eddie_front,(200,500))
        else:
            win.blit(eddie_front_gray,(200,500))
        pygame.display.update()
        
        # keyboard keys check
        keys= pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:    
          choise=choise-1
        if keys[pygame.K_RIGHT]:
            choise+=1
        if keys[pygame.K_UP]:
            choise=choise-1
        if keys[pygame.K_DOWN]:
             choise+=1
        if keys[pygame.K_ESCAPE]:
            wait=False
            
        if  choise>2:
            choise=2
        if choise<1:
            choise=1
        if keys[pygame.K_RETURN]:
            if choise==1:
                return "emma"
            if choise==2:
                return "eddie"

#picture files
full_heart=pygame.image.load("full_heart.png")
lose_heart=pygame.image.load("lose_heart.png")
pumpkin=pygame.image.load("pumpkin.png")
eddie_back=pygame.image.load("eddie_back.png")
eddie_right=pygame.image.load("eddie_right.png")
eddie_left=pygame.image.load("eddie_left.png")
eddie_front=pygame.image.load("eddie_front.png")
eddie=eddie_front
eddie_front_gray=pygame.image.load("eddie_front_gray.png")
emma_front=pygame.image.load("emma_front.png")
emma_right=pygame.image.load("emma_right.png")
emma_left=pygame.image.load("emma_left.png")
emma_back=pygame.image.load("emma_back.png")
emma=emma_front
emma_front_gray=pygame.image.load("emma_front_gray.png")
ghost_left=pygame.image.load("ghost_left.png")
ghost_right=pygame.image.load("ghost_right.png")
ghost=ghost_left
ghost2_left=pygame.image.load("ghost2_left.png")
ghost2_right=pygame.image.load("ghost2_right.png")
ghost2=ghost2_left
level1bg=pygame.image.load("bg1200x600.png")
bg=level1bg

#open window
win_w=1200
win_h=800
win=pygame.display.set_mode((win_w,win_h))
pygame.display.set_caption("Emma , the Pumpkin-hunter")

toplist=[30,20,10]
topnames=["Scare Crow","Ghost","Black Raven"]
mainloop = True


while mainloop:
    


    life=4
    score=0
    score_map1=100
    score_map2=400
    player=select_player()
    x= 50
    y= 50
    x_enemy1=400
    y_enemy1= 300
    x_enemy2=1000
    y_enemy2= 500
    w= 60
    h=90
    speed=10
    speed_enemy1=3
    speed_enemy2=4
    color_red=100
    x_pumpkin=random.randint(0,1200)
    y_pumpkin=random.randint(70,500)
    level=1

    #sound files
    game_over=mixer.Sound("game_over.wav")
    win_=mixer.Sound("win_.wav")

    pygame.mixer.music.load("Halloween.mp3")
    pygame.mixer.music.play(-1)

    #here drawing the map
    def draw_map():
        #win.fill((0,0,0))
        win.blit(bg,(0,70))
        for i in range(5,1250,70):
            pygame.draw.rect(win,brick_color,(i,5,65,30))
            pygame.draw.rect(win,brick_color,(i-33,40,65,30))
            pygame.draw.rect(win,brick_color,(i,605,65,30))
            pygame.draw.rect(win,brick_color,(i-33,640,65,30))
        if score >= score_map1:
            pygame.draw.rect(win,black,(550,5,100,70))
            print_small("Exit",green,655,1)
            print_small("Exit",green,505,1)
            
        pygame.draw.rect(win,gray,(5,675,1190,120))
        win.blit(pumpkin,(x_pumpkin,y_pumpkin))
        for i in range(1,5,1):   
            if life >= i :
                win.blit(full_heart,(int(80+((i-1)*40)),int(win_h*0.85)))
            if life < i :
                win.blit(lose_heart,(int(80+((i-1)*40)),int(win_h*0.85)))
        print_small("Life:",red,10,win_h*0.85)
        print_small("Score:"+str(score),purple,10,win_h*0.90)        
        if player == "emma":
            win.blit(emma,(int(x),int(y)))
        else:
            win.blit(eddie,(int(x),int(y)))
        win.blit(ghost,(int(x_enemy1),int(y_enemy1)))
        print_small(player,green,800,1)
       
        
        pygame.display.update()
    def draw_map2():
        win.fill((0,0,0))
        
        for i in range(5,1250,70):
            pygame.draw.rect(win,brick_color,(i,5,65,30))
            pygame.draw.rect(win,brick_color,(i-33,40,65,30))
            pygame.draw.rect(win,brick_color,(i,605,65,30))
            pygame.draw.rect(win,brick_color,(i-33,640,65,30))
        if score >= score_map2:
            pygame.draw.rect(win,black,(550,5,100,70))
            print_small("Exit",green,655,1)
            print_small("Exit",green,505,1)            
        pygame.draw.rect(win,gray,(5,675,1190,120))
        win.blit(pumpkin,(x_pumpkin,y_pumpkin))
        for i in range(1,8,1):   
            if life >= i :
                win.blit(full_heart,(int(80+((i-1)*40)),int(win_h*0.85)))
            if life < i :
                win.blit(lose_heart,(int(80+((i-1)*40)),int(win_h*0.85))) 
        print_small("Life:",red,10,win_h*0.85)
        print_small("Score:"+str(score),purple,10,win_h*0.90)        
        if player == "emma":
            win.blit(emma,(int(x),int(y)))
        else:
            win.blit(eddie,(int(x),int(y)))
        win.blit(ghost,(int(x_enemy1),int(y_enemy1)))
        win.blit(ghost2,(int(x_enemy2),int(y_enemy2)))
        pygame.display.update()
        
        
        

    def keyboard():
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x=x-speed
        if keys[pygame.K_RIGHT]:
            x=x+speed
        if keys[pygame.K_UP]:
            y=y-speed
        if keys[pygame.K_DOWN]:
            y=y+speed

    run=True
    while run:
        #pygame.time.delay(20)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
                
        draw_map()
        
        # keyboard keys check
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:    
            x=x-speed
            if player == "emma":
                emma=emma_left
            else:
                eddie=eddie_left
        if keys[pygame.K_RIGHT]:
            x=x+speed
            if player == "emma":
                emma=emma_right
            else:
                eddie=eddie_right
        if keys[pygame.K_UP]:
            y=y-speed
            if player == "emma":
                emma=emma_back
            else:
                eddie=eddie_back
        if keys[pygame.K_DOWN]:
            y=y+speed
            if player == "emma":
                emma=emma_front
            else:
                eddie=eddie_front
        if keys[pygame.K_ESCAPE]:
            run=False
            
        #logic part of program
        #logic/map ends
            
        if x>(win_w+w/2):
            x=-1*w/2
        if x<-1*w/2:
            x=win_w+w/2
        if (y<70 and x<550) or (y<70 and x>610):
            y=70
        if y<70 and y>60 and x>=550 and x<=610 and score < score_map1:
            y=70
        if y>605-h:
            y=605-h
        if y<=60:
            if x>610:
                x=610
            if x<550:
                x=550
        if y<-60:
            run = False
            level+=1
            score=score+(10*life)
            
        
        #logic part of program
        #logic/enemy
            
        if x>x_enemy1:
            x_enemy1+=speed_enemy1
            ghost=ghost_right
        if y>y_enemy1:
            y_enemy1+=speed_enemy1
        if x<x_enemy1:
            x_enemy1-=speed_enemy1
            ghost=ghost_left
        if y<y_enemy1:
            y_enemy1-=speed_enemy1
        if (x>= x_enemy1-w) and( x<=x_enemy1+w) and (y>= y_enemy1-h) and( y<=y_enemy1+h):
            x_enemy1=random.randint(1,2)
            if player == "emma":
                help_me=mixer.Sound("girl_help.wav")
            else:
                help_me=mixer.Sound("boy_help.wav")
            life-=1
            if life > 0:
                help_me.play()
            if life <= 0:
                run = False
            if x_enemy1 == 1:
                x_enemy1 = -100
            else:
                x_enemy1 = 1300
            y_enemy1=random.randint(70,605)

        #logic part of program
        #logic/pumpkin
        if (x>= x_pumpkin-w) and( x<=x_pumpkin+w) and (y>= y_pumpkin-w) and( y<=y_pumpkin+w):
            if player == "emma":
                got_pumpkin=mixer.Sound("girl_pumpkin.wav")
            else:
                got_pumpkin=mixer.Sound("boy_pumpkin.wav")
            got_pumpkin.play()
            x_pumpkin=random.randint(0,1200)
            y_pumpkin=random.randint(70,500)
            score+=10

        

            
            
          
       
        draw_map()
        
    x= 50
    y= 50
    x_enemy1=400
    y_enemy1= 300
    x_enemy2=1000
    y_enemy2= 500
    w= 60
    h=90
    speed=10
    speed_enemy1=2
    speed_enemy2=4
    color_red=100
    x_pumpkin=random.randint(0,1200)
    y_pumpkin=random.randint(70,500)
    life+=3
    if life > 7:
        life = 7
    while level==2:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type  == pygame.QUIT:
                run = False
                
        draw_map2()
        
        # keyboard keys check
        keys=pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:    
            x=x-speed
            if player == "emma":
                emma=emma_left
            else:
                eddie=eddie_left
        if keys[pygame.K_RIGHT]:
            x=x+speed
            if player == "emma":
                emma=emma_right
            else:
                eddie=eddie_right
        if keys[pygame.K_UP]:
            y=y-speed
            if player == "emma":
                emma=emma_back
            else:
                eddie=eddie_back
        if keys[pygame.K_DOWN]:
            y=y+speed
            if player == "emma":
                emma=emma_front
            else:
                eddie=eddie_front
        if keys[pygame.K_ESCAPE]:
            level=1
            
        #logic part of program
        #logic/map ends
            
        if x>(win_w+w/2):
            x=-1*w/2
        if x<-1*w/2:
            x=win_w+w/2
        if (y<70 and x<550) or (y<70 and x>610):
            y=70
        if y<70 and y>60 and x>=550 and x<=610 and score < score_map1:
            y=70
        if y>605-h:
            y=605-h
        if y<=60:
            if x>610:
                x=610
            if x<550:
                x=550
        if y<-60:
            level+=1
            score=score+(10*life)
            
        
        #logic part of program
        #logic/enemy
            
        if x>x_enemy1:
            x_enemy1+=speed_enemy1
            ghost=ghost_right
        if y>y_enemy1:
            y_enemy1+=speed_enemy1
        if x<x_enemy1:
            x_enemy1-=speed_enemy1
            ghost=ghost_left
        if y<y_enemy1:
            y_enemy1-=speed_enemy1
        if (x>= x_enemy1-w) and( x<=x_enemy1+w) and (y>= y_enemy1-h) and( y<=y_enemy1+h):
            x_enemy1=random.randint(1,2)
            if player == "emma":
                help_me=mixer.Sound("girl_help.wav")
            else:
                help_me=mixer.Sound("boy_help.wav")
            life-=1
        if x>x_enemy2:
            x_enemy2+=speed_enemy2
            ghost2=ghost2_right
        if y>y_enemy2:
            y_enemy2+=speed_enemy1
        if x<x_enemy2:
            x_enemy2-=speed_enemy2
            ghost2=ghost2_left
        if y<y_enemy2:
            y_enemy2-=speed_enemy1
        if (x>= x_enemy2-w) and( x<=x_enemy2+w) and (y>= y_enemy2-h) and( y<=y_enemy2+h):
            x_enemy2=random.randint(1,2)
            if player == "emma":
                help_me=mixer.Sound("girl_help.wav")
            else:
                help_me=mixer.Sound("boy_help.wav")
            life-=1
            if life > 0:
                help_me.play()
            if life <= 0:
                level = 1
            if x_enemy1 == 1:
                x_enemy1 = -100
            else:
                x_enemy1 = 1300
            y_enemy1=random.randint(70,605)

        #logic part of program
        #logic/pumpkin
        if (x>= x_pumpkin-w) and( x<=x_pumpkin+w) and (y>= y_pumpkin-w) and( y<=y_pumpkin+w):
            if player == "emma":
                got_pumpkin=mixer.Sound("girl_pumpkin.wav")
            else:
                got_pumpkin=mixer.Sound("boy_pumpkin.wav")
            got_pumpkin.play()
            x_pumpkin=random.randint(0,1200)
            y_pumpkin=random.randint(70,500)
            score+=10

        
        #logic part of program
        #logic/pumpkin

        if (score % 50 == 0 ) and (score > 0): 
           speed_enemy2+=1
           score+=10
            
            
          
       
        draw_map2()
        


    pygame.draw.rect(win,(0,0,0),(0,0,win_w,win_h))
    if y>0:
        print_big("Game Over",red,win_w/4,win_h/3)
    else:
        print_big("You Win!!!!!",red,win_w/4,win_h/3)
        
    print_big("Score:"+str(score),purple,win_w/4,win_h/3+150)


    pygame.display.update()
    if y >0:
        game_over.play()
    else:
        win_.play()
    pygame.time.delay(4000)

    pygame.draw.rect(win,black,(0,0,win_w,win_h))

    #logical check for scores

    if toplist[0] > score and toplist[1] > score and toplist[2] > score:
        print_med("Need more Pumpkin.", red,100,50)
        
    if toplist[0] > score and toplist[1] > score and toplist[2] <= score:
        print_med("You are on the 3. place!! Congrat!", red,100,50)
        toplist[2] = score
        topnames[2] = player
        
    if toplist[0] > score and toplist[1] <= score and toplist[2] < score:
        print_med("You are on the 2. place!! Congrat!", red,100,100)
        toplist[2]=toplist[1]
        toplist[1]=score
        topnames[2] = topnames[1]
        topnames[1] = player
        
        
    if toplist[0] <= score and toplist[1] < score and toplist[2] < score:
        print_med("You are on the 1. place!! Congrat!", red,100,100)
        toplist[2]=toplist[1]
        toplist[1]=toplist[0]
        toplist[0]=score
        topnames[2] = topnames[1]
        topnames[1] = topnames[0]
        topnames[0] = player

    print_med("1.Place:", red,50,350)
    print_med(topnames[0], red,400,350)
    print_med(str(toplist[0]), red,750,350)
    print_med("2.Place:", red,50,500)
    print_med(topnames[1], red,400,500)
    print_med(str(toplist[1]), red,750,500)
    print_med("3.Place:", red,50,650)
    print_med(topnames[2], red,400,650)
    print_med(str(toplist[2]), red,750,650)


    pygame.display.update()
    pygame.time.delay(4000)


pygame.quit()


