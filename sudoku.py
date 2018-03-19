import time,matplotlib as plt
import pandas as pd
global nodes
class sudoku:
    def __init__(self,puzzle_name):
        self.puzzle_name=puzzle_name
        self.puzzle=self.read_puzzle(self.puzzle_name)
        self.empty_cells=self.zero_cells(self.puzzle)
      #  print(self.empty_cells)
    def timed_BT(self):
        st=time.time()
        if self.simpleBT(self.empty_cells):
            tt=time.time()-st
        #print(tt)
        return tt
    def plot(self,t):
        plt.plot(t[0], [i in range(len(t[0]))], 'r--', t[1], [i in range(len(t[1]))], 'bs', t[2], [i in range(len(t[2]))], 'g^')
        plt.show()
    def timed_MRV_BT_FC(self):
        st=time.time()
        if self.MRV_BT_FC():
            tt=time.time()-st
        return tt               
    def zero_cells(self,puzzle):
        empty_cells=[]
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j]==0:
                    empty_cells.append((i,j))
        return empty_cells
    def read_puzzle(self,puzzle_name):
        fl=open(puzzle_name,'r')
        puzzle=[]
        s=fl.readlines()
        for i in s:
            puzzle.append([int(j) for j in i.split()])
        return puzzle    
    def print_puzzle(self,puzzle):
        for i in puzzle:
            for j in i:                
                print(j," ",end=" ")
            print()
    def write_puzzle(self,puzzle_name):
        op=''
        for i in self.puzzle:
            for j in i:
                op+=j
                op+=' '
            op+='\n'
        fl=open(puzzle_name,'w')
        fl.write(op)
        fl.close()
    def get_row(self,puzzle,cell):
        return puzzle[cell[0]]        
    def get_col(self,puzzle,cell):
        return [puzzle[i][cell[1]] for i in range(0,9)]
    def get_center(self,cell):
        if(cell[0]<3):
            c_r=1
        elif cell[0]<6:
            c_r=4
        else:
            c_r=7
        if(cell[1]<3):
            c_c=1
        elif cell[1]<6:
            c_c=4
        else:
            c_c=7
        return c_r,c_c
    def get_cell(self,puzzle,cell):
        c_r,c_c=self.get_center(cell)
        #print(c_r,c_c)
        return [puzzle[c_r][c_c],puzzle[c_r-1][c_c-1],puzzle[c_r-1][c_c],puzzle[c_r-1][c_c+1],puzzle[c_r][c_c-1],puzzle[c_r][c_c+1],puzzle[c_r+1][c_c-1],puzzle[c_r+1][c_c],puzzle[c_r+1][c_c+1]]
    def cell_check(self,puzzle,cell,value):
        row=self.get_row(puzzle,cell)
        col=self.get_col(puzzle,cell)
        cell=self.get_cell(puzzle,cell)
        #print(cell)
        if value in row or value in col or value in cell:
            return False
        return True
    def goal_state(self,puzzle):
        for i in range(9):
            s=self.get_row(puzzle,(i,0))
            c=self.get_col(puzzle,(0,i))
          #  print(s,c)
            if sum(s)!=45 or sum(c)!=45:
                return False
        cnt=[(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        for i in cnt:
            c_r=i[0]
            c_c=i[1]
            s=puzzle[c_r][c_c]+puzzle[c_r-1][c_c-1]+puzzle[c_r-1][c_c]+puzzle[c_r-1][c_c+1]+puzzle[c_r][c_c-1]+puzzle[c_r][c_c+1]+puzzle[c_r+1][c_c-1]+puzzle[c_r+1][c_c]+puzzle[c_r+1][c_c+1]
           # print(s)        
            if s!=45:
                return False
        return True
    def simpleBT(self,empty_cells):
        if self.goal_state(self.puzzle):
      #      self.print_puzzle(self.puzzle)
            return True
        else:
            global nodes
            nodes+=1 
            c_cell=empty_cells[0]
            for i in range(1,10):
               
              #  print(c_cell,i)
                if self.cell_check(self.puzzle,c_cell,i):
                    self.puzzle[c_cell[0]][c_cell[1]]=i

                    if self.simpleBT(empty_cells[1:]):
                        return True
                self.puzzle[c_cell[0]][c_cell[1]]=0
        return False
    def legal_values(self,puzzle,cell):
        row=self.get_row(puzzle,cell)
        col=self.get_col(puzzle,cell)
        cell=self.get_cell(puzzle,cell)
        all=set(row).union(set(col)).union(set(cell))
        ans=[]
        for i in range(1,10):
            if i not in all:
                ans.append(i)
        return ans
    def zero_cells_mrv(self,puzzle):
        empty_cells=[]
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j]==0:
                    l_v=self.legal_values(puzzle,(i,j))
                    empty_cells.append((len(l_v),(i,j),l_v))
        return sorted(empty_cells)
    def MRV_BT_FC(self):
        if self.goal_state(self.puzzle):
            #self.print_puzzle(self.puzzle)
            return True
        else:
            global nodes
            nodes+=1
            MRV_FC=self.zero_cells_mrv(self.puzzle)[0]
            #print(MRV_FC)
            for legal_value in MRV_FC[2]:
                self.puzzle[MRV_FC[1][0]][MRV_FC[1][1]]=legal_value           
                if self.MRV_BT_FC():
                    return True
                self.puzzle[MRV_FC[1][0]][MRV_FC[1][1]]=0
        return False
'''
    def probablity_update_zero_row(probablity,cell,value):
        for i in range(9):
            if (cell[0],i)!=cell:
                probablity[cell[0],i][value-1]=(0,False)
            else:
                probablity[cell[0],i][value-1]=(1,True)
        return probablity
    def probablity_update_zero_col(probablity,cell,value):
        for i in range(9):
            if (i,cell[1])!=cell:
                probablity[i,cell[1]]=[value-1]=(0,False)
            else:
                probablity[i,cell[1]]=[value-1]=(1,False)
        return probablity
    def probablity_update_zero_cell(probablity,cell,value):
        c_r,c_c=self.get_center(cell)
        block=[(c_r,c_c),(c_r-1,c_c-1),(c_r-1,c_c),(c_r-1,c_c+1),(c_r,c_c-1),(c_r,c_c+1),(c_r+1,c_c-1),(c_r+1,c_c),(c_r+1,c_c+1)]
        for i in block:
            if i!=cell:
                probablity[i][value-1]=(0,False)
            else:
                probablity[i][value-1]=(1,False)
        return probablity

    def probablity_init(self,puzzle)
        probablity={}
        #by default every probablit is zero except for fixed variables
        #for vixed varaibles, their probablity is 1 for position-1 and rest all is zero
        #False means the probality cannot me modified and true means it can be modified
        
        for i in range(9):
            for j in range(9):
                if puzzle[i][j]!=0:
                    p=[(0,False) for i in range(9)]
                    p[puzzle[i][j]-1]=(1,False)
                    probablity[(i,j)]=p
                else:
                    probablity[(i,j)]=[0 for j in range(9)]
        for i in range(9):
            for j in range(9):
                if puzzle[i][j]!=0:

        
        #return probablity
    def probality_fill(self,puzzle):
        for i in range(9):
            for j in range(9):
                if 
s=sudoku('puzzle3.txt').MRV_BT_FC()
s=sudoku('puzzle3.txt')
s.print_puzzle(s.puzzle)
d={}
for i in range(9):
	for j in range(9):
		p=[-1 for k in range(9)]
		d[(i,j)]=p
for i in range(9):
	for j in range(9):
		if s.puzzle[i][j]!=0:
			p=[0 for k in range(9)]
			p[s.puzzle[i][j]-1]=1
			d[(i,j)]=p
		
for i in range(9):
	for j in range(9):
		if s.puzzle[i][j]!=0:
			for k in d:
				if k[0]==i or k[1]==j:					
					if (i,j)!=k:
						d[k][s.puzzle[i][j]-1]=0

import pandas as pd
dfinal={}

df = pd.DataFrame(data=d)
df = (df.T)
df.to_csv('dict1.xlsx')
#print(s.MRV_BT_FC(s.empty_cells))
'''
import os
t='/home/shivam/Projects/sudokus/'
os.chdir(t)
dr=os.listdir()
st_bt={}
st_mvr={}

fn=0
for dir in dr:
    st_bt[dir]=[]
    st_mvr[dir]=[]
for dir in sorted(dr):
    os.chdir(dir)    
    for files in os.listdir():
        print(fn,' ',files)
        fn+=1
        s=sudoku(files)
        nodes=0
        ts=s.timed_BT()
        st_bt[dir].append((ts,nodes))
        nodes=0
        s=sudoku(files)
        ts=s.timed_MRV_BT_FC()
        st_mvr[dir].append((ts,nodes))
    os.chdir(t)


sps_mv={}
spt_mv={}

for i in st_mvr:
    a=[]
    b=[]
    for v in st_mvr[i]:
        b.append(v[0])
        a.append(v[1])
    sps_mv[i]=a
    spt_mv[i]=b    

sps_bt={}
spt_bt={}
for i in st_bt:
    a=[]
    b=[]
    for v in st_bt[i]:
        b.append(v[0])
        a.append(v[1])
    sps_bt[i]=a
    spt_bt[i]=b


df=pd.DataFrame(sps_bt)
df.to_csv('Steps_BT')
df=pd.DataFrame(spt_bt)
df.to_csv('Time_BT')

df=pd.DataFrame(sps_mv)
df.to_csv('Steps_MVR')
df=pd.DataFrame(spt_mv)
df.to_csv('Time_MVR')
