import pandas as pd
import numpy,time,os
class sudoku:
    def __init__(self,puzzle_name,n):
        self.n=n        
        self.space=[(i,j) for i in range(self.n) for j in range(self.n)]        
        self.puzzle=self.read_puzzle(puzzle_name)
        self.counter=self.count()
        #self.probab=self.probablity_init()
    def count(self):
        #to count the number of digits that are yet to come in the sudoku.
        
        self.counter={}
        for i in range(self.n):
            self.counter[i+1]=9        
        for val in self.space:
            if self.puzzle[val[0]][val[1]]!=0:
                self.counter[self.puzzle[val[0]][val[1]]]-=1
        return self.counter
    def goal_state(self,puzzle):
        for i in range(9):
            s=self.get_row(puzzle,(i,0))
            c=self.get_col(puzzle,(0,i))
          #  print(s,c)
            if sum(s)!=45 or sum(c)!=45:
                #print(i,sum(s),sum(c))
                return False
        cnt=[(1,1),(1,4),(1,7),(4,1),(4,4),(4,7),(7,1),(7,4),(7,7)]
        for i in cnt:
            c_r=i[0]
            c_c=i[1]
            s=puzzle[c_r][c_c]+puzzle[c_r-1][c_c-1]+puzzle[c_r-1][c_c]+puzzle[c_r-1][c_c+1]+puzzle[c_r][c_c-1]+puzzle[c_r][c_c+1]+puzzle[c_r+1][c_c-1]+puzzle[c_r+1][c_c]+puzzle[c_r+1][c_c+1]
      
            if s!=45:
                #print(i,s)
                return False
        return True
    def get_row(self,puzzle,cell):
        return puzzle[cell[0]]        
    def get_col(self,puzzle,cell):
        return [puzzle[i][cell[1]] for i in range(0,9)]
    def get_cell(self,puzzle,cell):
        c_r,c_c=self.get_center(cell)
        return [puzzle[c_r][c_c],puzzle[c_r-1][c_c-1],puzzle[c_r-1][c_c],puzzle[c_r-1][c_c+1],puzzle[c_r][c_c-1],puzzle[c_r][c_c+1],puzzle[c_r+1][c_c-1],puzzle[c_r+1][c_c],puzzle[c_r+1][c_c+1]]
    def feynBT(self):
        if self.goal_state(self.puzzle):
      #      self.print_puzzle(self.puzzle)
            return True
        else:

            c_cell=empty_cells[0]
            for i in range(1,10):
              #  print(c_cell,i)
                if self.cell_check(self.puzzle,c_cell,i):
                    self.puzzle[c_cell[0]][c_cell[1]]=i

                    if self.simpleBT(empty_cells[1:]):
                        return True
                self.puzzle[c_cell[0]][c_cell[1]]=0
        return False

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
    def probablity_init(self):
        probab={}
        #for all 81 values in a sudoku, initalized as list [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        #where -1 means that particular index+1 value can come in that cell  
        for coord in self.space:
            probab[coord]=[-1 for k in range(self.n)]
        #for all coordinates which have non zero value in the given sudoku, change them to a list of 0 & 1
        #where 0 means that index+1 value cannot come and 1 means that index+1 value is occupied
        for coord in self.space:
            if self.puzzle[coord[0]][coord[1]]!=0:
                p=[0]*self.n
                p[self.puzzle[coord[0]][coord[1]]-1]=1
                probab[coord]=p
        #the below loop ensures that if a cell has a any value, then its row, col & region will have 0
        #at that index. 
        for coord in self.space:
            ak=[]
            if self.puzzle[coord[0]][coord[1]]!=0:
                for i in range(0,9):
                    ak.append((coord[0],i))
                    ak.append((i,coord[1]))
                c_r,c_c=self.get_center(coord)
                ak+=[(c_r,c_c),(c_r-1,c_c-1),(c_r-1,c_c),(c_r-1,c_c+1),(c_r,c_c-1),(c_r,c_c+1),(c_r+1,c_c-1),(c_r+1,c_c),(c_r+1,c_c+1)]
                for i in ak:
                    if i!=coord:
                        probab[i][self.puzzle[coord[0]][coord[1]]-1]=0
        return probab
    def print_probab(self):
        for i in self.probab:
            print(i,self.probab[i])
    def export_csv(self):
        df = pd.DataFrame(data=self.puzzle)
        df = (df.T)
        df.to_csv('dict1.xlsx')
    def read_puzzle(self,puzzle_name):
        fl=open(puzzle_name,'r')
        puzzle=[]
        s=fl.readlines()
        for i in s:
            puzzle.append([int(j) for j in i.split()])
        return puzzle    
    def print_puzzle(self):
        for i in self.puzzle:
            for j in i:
                print(j," ",end=" ")
            print()
    def init_t(self):
        self.t={}
        for i in self.probab:
            if -1 in self.probab[i]:
                ans=[]
                for j in range(len(self.probab[i])):
                    if self.probab[i][j]==-1:
                        ans.append(j+1)
                self.t[i]=ans               
        return self.t   
    def print_empty(self):
        self.t=self.init_t()
        self.t1={}

        f={}        
        for i in range(1,10):
            ans=0
            for j in self.t:
                if i in self.t[j]:
                    ans+=1/len(self.t[j])
            f[i]=ans
        an1=[]
        for i in f:
            print(i,f[i],abs(s.counter[i]-f[i]))
            an1.append((abs(s.counter[i]-f[i]),i,f[i]))
        #print(self.t)
       # print(min(an1))    
    def gett(self,n1):
        an1=[]
        for i in self.t:
            if n1 in self.t[i]:
                print(i,self.t[i],1/len(self.t[i]))
                an1.append((1/len(self.t[i]),i,self.t[i]))
        print(max(an1))
    def update(self,coord,val):
        r=self.get_row(self.puzzle,coord)
        c=self.get_row(self.puzzle,coord)
        reg=self.get_cell(self.puzzle,coord)
        if val in r or val in c or val in reg:
            return False
        self.puzzle[coord[0]][coord[1]]=val
        self.counter=self.count()
        self.probab=self.probablity_init()
        return True
        #print()
        #s.print_puzzle()
        #print()
        #s.print_empty()
        #return s.probablity()
    def probablity(self):
        
        self.probab=self.probablity_init()
        self.t=self.init_t()
        var={}
        revar={}
        d=0
        for i in range(1,10):
            for j in range(9):
                for k in range(9):
                    var[str(i)+'_'+str(j)+'_'+str(k)]=d
                    revar[d]=str(i)+'_'+str(j)+'_'+str(k)
                    d+=1
        an=[]
        for i in s.t:
            ab=[0]*729
            for val in s.t[i]:      
                ab[var[str(val)+'_'+str(i[0])+'_'+str(i[1])]]=1
            an.append(ab)
        bn=[1]*len(an)
        lp={}
        for i in range(1,10):
            lp[i]=[]
        for i in s.t:
            for j in range(1,10):
                if j in s.t[i]:
                    lp[j].append(i)
        for i in lp:
            ab=[0]*729
            for tp in lp[i]:
                ab[var[str(i)+'_'+str(tp[0])+'_'+str(tp[1])]]=1
            an.append(ab)
            bn.append(self.counter[i]) 
        an=numpy.array(an)
        bn=numpy.array(bn)
        x=numpy.linalg.lstsq(an,bn)[0]  
        ans=[]
       # for i in s.t:
        #    print(i,s.t[i])
        for i in range(len(x)):
            if(x[i]>0 and (int(revar[i][2]),int(revar[i][4])) in s.t):
                ans.append((x[i],revar[i]))
        ans=sorted(ans,reverse=True)
#       print(len(self.t))
#        for i in self.probab:
#            print(i,self.probab[i])
        #ans1=max(ans)
        return ans 
    #(int(ans1[1][2]),int(ans1[1][4])),int(ans1[1][0]) 
'''
s=sudoku('puzzle3.txt',9)
ts=time.time()
te=0
while True:
    if s.goal_state(s.puzzle)==True:
        te=time.time()
        break

    ans1=s.probablity()
    while s.update((int(ans1[0][1][2]),int(ans1[0][1][4])),int(ans1[0][1][0]))==False:
        ans1=ans1[1:]
    input()
#    print(c,v)
    s.print_puzzle()

'''
import os
t='/home/shivam/Projects/sudokus/'
os.chdir(t)
dr=os.listdir()
st={}
fn=0
for dir in dr:
    st[dir]=[]
delete_list=[]
for dir in sorted(dr):
    os.chdir(dir)    
    for files in os.listdir():
        print(fn,' ',files)
        s=sudoku(files,9)
        fn+=1
        ts=time.time()
        te=0
        #s.print_probab()
        while True:
            if s.goal_state(s.puzzle)==True:
                te=time.time()
                break
            if(time.time()-ts>10):
                print("File error,", files, " exception Timeout")
                delete_list.append(files)
                break
            ans1=s.probablity()
            check=True
            try:
                while s.update((int(ans1[0][1][2]),int(ans1[0][1][4])),int(ans1[0][1][0]))==False:
                    ans1=ans1[1:]
            except Exception as identifier:
                print("File error,", files, " exception ",identifier)
                delete_list.append(files)
                break
            #print('1')
        #    input()
        #    print()
            #s.print_puzzle()
        #    print(s.count())
        #print('Puzzle '+files+' solved in: ',te-ts)
        st[dir].append(te-ts)
    os.chdir(t)
import os
def delete(lst):
    for i in lst:
        os.remove(i)
