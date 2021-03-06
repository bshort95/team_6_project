import pygame, sys, random
from maze_builder import Maze
import socket
from _thread import *
from network import Network


# settiing up the game
size = 12
pygame.init()
screen = pygame.display.set_mode((1500,760))


# game variables

walls = pygame.image.load('wall_block.png')
terminal = pygame.image.load('terminal.png')
floor = pygame.image.load('floor_block.png')
p_img = pygame.image.load('front.png')
shadow = pygame.image.load('shadow.png')




# building the maze and making sure it is passable

bob = Maze(size)
joe = Maze(size)
bob.base_maze_builder()
bob.maze_builder()
while bob.is_maze_passable() == False: 
    bob.base_maze_builder()
    bob.maze_builder()
    
l_maze = bob.get_maze()
r_maze = bob.get_maze()

l_maze[18][37]=0
l_maze[18][36]=0
l_maze[20][37]=0
l_maze[20][36]=0

r_maze[18][0]=0
r_maze[18][1]=0
r_maze[20][0]=0
r_maze[20][1]=0


# player class
class Player():
    def __init__(self, x, y, width, height, ammo, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.ammo = ammo
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        #pygame.draw.rect(win, self.color, self.rect)
        screen.blit(p_img,(self.x - 6, self.y - 6))

    
    def move(self, key1 , key2):
        keys = pygame.key.get_pressed()

        

        if keys[pygame.K_LEFT] and key1 != 1 :
            self.x -= self.vel
        
        if keys[pygame.K_RIGHT] and key1 != 2 :
            self.x += self.vel

        if keys[pygame.K_UP] and key2 != 1 :
            self.y -= self.vel

        if keys[pygame.K_DOWN] and key2 != 2 :
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)


# Communication Functions
def read_pos(str):
    if str is not None:
        str = str.split(",")
        return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(screen, player, player2):
    #win.fill((255,255,255))
    player.draw(screen)
    player2.draw(screen)
   

# check colisions on the x axis
def checkColx(map, pos_x, pos_y, size):

    if pos_x > 760:
        pos_x = pos_x - 740
    size = (size * 3) + 2
    pos_x = pos_x - 20
    pos_y = pos_y - 20
    var = 0
    for y in range(size):
        for x in range(size):
            if map[y][x] == 1  and (pos_x - 1 < x *20 and pos_x - 1> (x * 20) - 20) and (pos_y < y* 20 and pos_y > (y * 20) - 20):
               
                var = 1
                p.x += 2

            if map[y][x] == 1  and (pos_x + 15 < x* 20 and pos_x + 15 > (x * 20) - 20) and (pos_y < y* 20 and pos_y > (y * 20) - 20):
               
                var = 2
                p.x -= 2
    return var



# check colisions on the y axis

def checkColy(map, pos_x, pos_y, size):

    if pos_x > 760:
        pos_x = pos_x - 740
    size = (size * 3) + 2
    pos_x = pos_x - 20
    pos_y = pos_y - 20
    var = 0
    for y in range(size):
        for x in range(size):
            if map[y][x] == 1  and (pos_y - 1 < y *20 and pos_y - 1 > (y * 20) - 20) and (pos_x < x* 20 and pos_x > (x * 20) - 20):
                
                var = 1
                p.y += 2

            if map[y][x] == 1  and (pos_y + 15 < y* 20 and pos_y + 15 > (y * 20) - 20) and (pos_x < x* 20 and pos_x > (x * 20) - 20):
               
                var = 2 
                p.y -=2    
    return var


# setting up network
n = Network()
startPos = read_pos(n.getPos())
p = Player(startPos[0], startPos[1], 15, 15, 0, (0,255,34))
p2 = Player(0, 0, 15, 15, 0, (200,0,255))




clock = pygame.time.Clock()


# game loop
while True:
    clock.tick(60)
    p2Pos = read_pos(n.send(make_pos((p.x, p.y))))
    p2.x = p2Pos[0]
    p2.y = p2Pos[1]

    screen.blit(floor,(0,0))

 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
      
  
    

    #draws map on screen
    for y in range(0, (size*3)+2):
        for x in range(0, (size*3)+2):
            if l_maze[x][y] == 1:
                screen.blit(walls,(y*20,x*20))    
            elif l_maze[x][y] == 3:
                screen.blit(terminal,(y*20,x*20))
            
            if r_maze[x][y] == 1:
                screen.blit(walls,((y*20)+740,x*20))    
            elif r_maze[x][y] == 3:
                screen.blit(terminal,((y*20)+740,x*20))
     
    p.move(checkColx(l_maze,p.x,p.y,size),checkColy(l_maze,p.x,p.y,size))
    
    p2.update()
    redrawWindow(screen, p, p2)

    pygame.display.update()
    
