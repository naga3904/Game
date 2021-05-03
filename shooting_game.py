import pygame
import random
import math
#initialize a pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("space_invaders")
icon=pygame.image.load("battleship.png")
pygame.display.set_icon(icon)
backgroundImg=pygame.image.load("3680341.jpg")
vel=5
width=64
height=64
playerImg=pygame.image.load("battleship.png")
enemyImg=[]
enemyX=[]
enemyY=[]
enemyX_change=[]
enemyY_change=[]
no_of_enemies=10
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load("transport.png"))
    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)
bulletImg=pygame.image.load("miscellaneous.png")
bulletX=0
bulletY=480
bulletX_change=2
bulletY_change=15
bullet_state='ready'
#score
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

playerX=360
playerY=490
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
def iscollision(a,b,c,d):
    distance=math.sqrt((math.pow(enemyX[i]-bulletX,2))+(math.pow(enemyY[i]-bulletY,2)))
    if distance<=27:
        return True
    else:
        return False
def show_score(x,y):
    score=font.render("score:"+str(score_value),True,(0,255,0))
    screen.blit(score,(x,y))

running=True
while running:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and playerX>vel:
        playerX-=vel
    if keys[pygame.K_RIGHT] and playerX<800-width-vel:
        playerX+=vel
    if keys[pygame.K_SPACE]:
        if bullet_state is "ready":
            bulletX=playerX
            fire_bullet(bulletX,bulletY)


    screen.fill((0,0,0))
    screen.blit(backgroundImg,(0,0))
    for i in range(no_of_enemies):
        enemyX[i]+=enemyX_change[i]
        if enemyX[i]<=0:
            enemyX_change[i]=2
            enemyY[i]+=enemyY_change[i]
        if enemyX[i]>=736:
            enemyX_change[i]=-2
            enemyY[i]+=enemyY_change[i]

        collision=iscollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY=480
            bullet_state="ready"
            score_value+=1
            enemyX[i]=random.randint(0,800)
            enemyY[i]=random.randint(50,150)
        enemy(enemyX[i],enemyY[i],i)
    if bulletY<=0:
        bulletY=480
        bullet_state='ready'
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY-=bulletY_change
    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()
