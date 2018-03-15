import pandas as pd
class sudoku:
    def __init__(self,puzzle_name,n):
        self.n=n
        
        self.space=[(i,j) for i in range(self.n) for j in range(self.n)]        
        self.puzzle=self.read_puzzle(puzzle_name)
        self.counter={}
        for i in range(self.n):
            self.counter[i+1]=9
        self.probab=self.probablity_init()
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
        for coord in self.space:
            probab[coord]=[-1 for k in range(self.n)]
        for coord in self.space:
            if self.puzzle[coord[0]][coord[1]]!=0:
                self.counter[self.puzzle[coord[0]][coord[1]]]-=1
                p=[0]*self.n
                p[self.puzzle[coord[0]][coord[1]]-1]=1
           #     print(coord,p)
                probab[coord]=p

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
        df = pd.DataFrame(data=self.probab)
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
    def print_empty(self):
        self.t={}
        for i in self.probab:
            if -1 in self.probab[i]:
                ans=[]
                for j in range(len(self.probab[i])):
                    if self.probab[i][j]==-1:
                        ans.append(j+1)
#                        ans.append('P'+str(j+1)+' ')
                self.t[i]=ans               
# ans.append(str(' =1'))
                #if 2 in ans:
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
        print(min(an1))    
    def gett(self,n1):
        an1=[]
        for i in self.t:
            if n1 in self.t[i]:
                print(i,self.t[i],1/len(self.t[i]))
                an1.append((1/len(self.t[i]),i,self.t[i]))
        print(max(an1))
    def update(self,coord,val):
        self.puzzle[coord[0]][coord[1]]=val
        self.counter={}
        for i in range(self.n):
            self.counter[i+1]=9
        self.probab=self.probablity_init()
        s.print_puzzle()
        s.print_empty()
                   
s=sudoku('puzzle3.txt',9)
s.print_puzzle()
s.print_empty()
#s.print_probab()