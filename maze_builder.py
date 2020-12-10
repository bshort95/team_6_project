from shape import Shape
from connected import Connected
import random
class Maze:
    def __init__(self, size):
        self.size = size
        self.connect = Connected((((size*3)+2)*((size*3)+2)))
        self.start_c = 0
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

        endy = (self.size*3) + 1
        endx = midpoint
        

        self.maze[startx][starty] = 0
        self.maze[startx][starty+1] = 0
        self.maze[startx][starty+2] = 0
        self.maze[endx][endy] = 0 
        self.maze[endx][endy-1] = 0 
        self.maze[endx][endy-2] = 0 

        self.connect.connect(((startx * ((self.size*3) + 2))+ starty),((startx * ((self.size*3) + 2))+starty)+1)
        self.connect.connect(((endx * ((self.size*3) + 2))+ endy),((endx * ((self.size*3) + 2))+endy)-1)
        
        self.start_c = ((startx * ((self.size*3) + 2))+ starty)
        self.end_c = ((endx * ((self.size*3) + 2))+ endy)

        
       


    def dis_maze(self):
         for x in range(0,((self.size*3)+2)):
            for y in range(0,((self.size*3)+2)):
                print(self.maze[x][y], end = ' ')
            print('\n')


    def get_maze(self):
        return self.maze
                
    def maze_runner(self):
        size = ((self.size *3) + 2)
        for y in range(0, size):
            for x in range(0, size):
                if y != size -1 and x != size -1 :
                    if y != (size -1):              
                        if self.maze[x][y] == 0 and self.maze[x][y+1] == 0:
                            self.connect.connect(((x * size)+y),((x * size)+y)+1)
                    if x != ((self.size*3)+1):
                        if self.maze[x][y] == 0 and self.maze[x+1][y] == 0:
                            self.connect.connect(((x * size)+y),((x * size)+y)+ size)

    def is_maze_passable(self):
        
        self.maze_runner()
        return self.connect.isConnected(self.start_c,self.end_c)
        











