from shape import Shape
from connected import Connected
import random
class Maze:
    def __init__(self, size):
        self.size = size
        self.connect = Connected((((size*3)+2)*((size*3)+2)))
        self.start_c = 0
        self.term1 = 0
        self.term2 = 0
        self.term3 = 0
        self.end_c = 0
        self.base = [[Shape("temp",[[1,1,1],[1,1,1],[1,1,1]],False,False) for x in range(0, size)] for y in range(0,size)]
        self.maze = [[ 1 for x in range(0,((size *3) +2))] for y in range(0,((size *3) +2))]
               



        
    def base_maze_builder(self):
       
        plus_shape_r = Shape("plus_r",[[1,0,1],[1,0,0],[1,0,1]],True,True)
        plus_shape = Shape("plus",[[1,0,1],[0,0,0],[1,0,1]],False,True)
        v_line_shape = Shape("vline",[[1,0,1],[1,0,1],[1,0,1]],True,False)
        h_line_shape = Shape("hline",[[1,1,1],[0,0,0],[1,1,1]],False,True)
        el_shape = Shape("el_shape",[[1,0,1],[1,0,0],[1,1,1]],False,True)
        inv_el_shape = Shape("inv_el_shape",[[1,1,1],[1,0,0],[1,0,1]],True,True)
        inv_re_el_shape = Shape("inv_re_el_shape",[[1,1,1],[0,0,1],[1,0,1]],True,False)
        halve_plus_shape = Shape("halve_plus_shape",[[1,0,1],[0,0,1],[1,0,1]],True,False)
        
        top_o_side_o = [plus_shape,halve_plus_shape]
        top_o_side_c = [plus_shape,v_line_shape,plus_shape_r]
        top_c_side_o = [plus_shape,h_line_shape, inv_re_el_shape]
        top_c_side_c = [h_line_shape,el_shape,inv_el_shape,halve_plus_shape]


        for y in range(0,self.size):
            for x in range(0,self.size):
                if x == 0 and y == 0:
                    self.base[x][y] = inv_el_shape
                elif x == 0:
                    if self.base[x][y-1].is_side_open() == True:
                        self.base[x][y] =  top_c_side_o[random.randrange(0,3)]
                        
                    else:
                        self.base[x][y] =  top_c_side_c[random.randrange(0,4)]
                    
                elif y == 0:
                    if self.base[x-1][y].is_top_open() == True:
                        self.base[x][y] =  top_o_side_c[random.randrange(0,3)]     
                    else:
                        self.base[x][y] =  top_c_side_c[random.randrange(0,4)]     
                else:
                    if self.base[x-1][y].is_top_open() == True and self.base[x][y-1].is_side_open() == True:
                        self.base[x][y] =  top_o_side_o[random.randrange(0,2)]
                        while self.base[x][y-1].get_id() == self.base[x][y].get_id(): 
                            self.base[x][y] =  top_o_side_o[random.randrange(0,2)]
                         
                    if self.base[x-1][y].is_top_open() == True and self.base[x][y-1].is_side_open() == False:
                        self.base[x][y] =  top_o_side_c[random.randrange(0,3)]
                        while self.base[x][y-1].get_id() == self.base[x][y].get_id(): 
                            self.base[x][y] =  top_o_side_c[random.randrange(0,3)]
                    
                    
                    if self.base[x-1][y].is_top_open() == False and self.base[x][y-1].is_side_open() == True:
                        self.base[x][y] =  top_c_side_o[random.randrange(0,3)]
                        while self.base[x][y-1].get_id() == self.base[x][y].get_id(): 
                            self.base[x][y] =  top_c_side_o[random.randrange(0,3)]
                    
                    
                    if self.base[x-1][y].is_top_open() == False and self.base[x][y-1].is_side_open() == False:
                        self.base[x][y] =  top_c_side_c[random.randrange(0,4)]
                        while self.base[x][y-1].get_id() == self.base[x][y].get_id(): 
                            self.base[x][y] = top_c_side_c[random.randrange(0,4)]

    def disp(self):
        for y in range(0,self.size):
            for x in range(0,self.size):
                if self.base[x][y].get_id() == "plus":
                    print("+" , end=' ')
                if self.base[x][y].get_id() == "vline":
                    print("|", end=' ')
                if self.base[x][y].get_id() == "hline":
                    print("-", end=' ')
                if self.base[x][y].get_id() == "el_shape":
                    print("[", end=' ')
                if self.base[x][y].get_id() == "inv_el_shape":
                    print("{", end=' ')
                if self.base[x][y].get_id() == "re_el_shape":
                    print("]", end=' ')
                if self.base[x][y].get_id() == "inv_re_el_shape":
                    print("}", end=' ')
                if self.base[x][y].get_id() == "halve_plus_shape":
                    print("%", end=' ')
                if self.base[x][y].get_id() == "temp":
                    print("e", end=' ')
            print("\n")  

    def maze_builder(self):
        for y in range(0,self.size):
            for x in range(0,self.size):
                    temp = self.base[x][y].get_shape()        
                    
                    temp1 = temp[0][0]
                    temp2 = temp[0][1]
                    temp3 = temp[0][2]
                    temp4 = temp[1][0]
                    temp5 = temp[1][1]
                    temp6 = temp[1][2]
                    temp7 = temp[2][0]
                    temp8 = temp[2][1]
                    temp9 = temp[2][2]

                    
                    self.maze[(x*3)+1][(y*3)+1] = temp1 
                    self.maze[(x*3)+1][(y*3)+2] = temp2
                    self.maze[(x*3)+1][(y*3)+3] = temp3
                    self.maze[(x*3)+2][(y*3)+1] = temp4
                    self.maze[(x*3)+2][(y*3)+2] = temp5
                    self.maze[(x*3)+2][(y*3)+3] = temp6
                    self.maze[(x*3)+3][(y*3)+1] = temp7
                    self.maze[(x*3)+3][(y*3)+2] = temp8
                    self.maze[(x*3)+3][(y*3)+3] = temp9
        
        


        
        midpoint = int(((self.size * 3) + 2)/2) 
        
        
        starty = 0
        startx = midpoint

        endy = self.size*3 + 1
        endx = midpoint
        

        self.maze[startx][starty] = 0
        self.maze[startx][starty+1] = 0
        self.maze[startx][starty+2] = 0
        self.maze[endx][endy] = 0 
        self.maze[endx][endy-1] = 0 
        self.maze[endx][endy-2] = 0 

        self.connect.connect(((startx - 1) *((self.size*3) + 2))+(starty), (startx -1)*((self.size*3) + 2)+(starty+1))
        self.connect.connect(((endx - 1)*((self.size*3) + 2))+(endy-1), (endx -1) *((self.size*3) + 2) + (endy))
        
        self.start_c = ((startx - 1) *((self.size*3) + 2))+(starty)
        self.end_c = ((endx -1) *((self.size*3) + 2)) + (endy)

        
        terminalx1 = random.randrange( 4 ,(((self.size * 3) + 2)-4))
        terminaly1 = random.randrange( 4 ,(((self.size * 3) + 2)-4))
        self.maze[terminalx1][terminaly1] = 3

        self.term1 = ((terminalx1 - 1) *((self.size*3) + 2))+(terminaly1)


        terminalx2 = random.randrange( 4 ,(((self.size * 3) + 2)-4))
        terminaly2 = random.randrange( 4 ,(((self.size * 3) + 2)-4))
        self.maze[terminalx2][terminaly2] = 3

        self.term2 = ((terminalx2 - 1) *((self.size*3) + 2))+(terminaly2)

        terminalx3 = random.randrange( 4 ,(((self.size * 3) + 2)-4))
        terminaly3 = random.randrange( 4 ,(((self.size * 3) + 2)-4))
        self.maze[terminalx3][terminaly3] = 3
        
        self.term3 = ((terminalx3 - 1) *((self.size*3) + 2))+(terminaly3)
    


    def dis_maze(self):
         for y in range(0,((self.size*3)+2)):
            for x in range(0,((self.size*3)+2)):
                print(self.maze[x][y], end = ' ')
            print('\n')


    def get_maze(self):
        return self.maze
                
    def maze_runner(self):
         for y in range(0, ((self.size*3)+2)):
            for x in range(0, ((self.size*3)+2)):
                if y != ((self.size*3)+1) and x != ((self.size*3)+1):
                    if y != ((self.size*3)+1):    
                        #print(y+1)           
                        if self.maze[x][y] == 0 and self.maze[x][y+1] == 0:
                            self.connect.connect(((x-1) *((self.size*3) +2) + y), (x-1) *((self.size*3) +2) + y+1)
                    if x != ((self.size*3)+1):
                        #print(x)
                        #print(y)
                        #print(x *((self.size*3) +2) + y)
                        if self.maze[x][y] == 0 and self.maze[x+1][y] == 0:
                            self.connect.connect((x-1) *((self.size*3) +2) + y,(x *((self.size*3) +2) + y))
                #print((x)*(self.size*3) + (y))    

    def is_maze_passable(self):
        
        self.maze_runner()
        return self.connect.isConnected(self.start_c,self.end_c) and self.connect.isConnected(self.start_c,self.term1) and self.connect.isConnected(self.start_c,self.term2) and self.connect.isConnected(self.start_c,self.term3)
        

        













