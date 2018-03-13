class sudoku:
    def __init__(self,puzzle_name):
        self.puzzle_name=puzzle_name
        self.read_puzzle(self.puzzle_name)
        self.empty_cells=self.zero_cells(self.puzzle)
        print(self.empty_cells)
    def zero_cells(self,puzzle):
        empty_cells=[]
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j]==0:
                    empty_cells.append((i,j))
        return empty_cells
    def read_puzzle(self,puzzle_name):
        fl=open(puzzle_name,'r')
        self.puzzle=[]
        s=fl.readlines()
        for i in s:
            self.puzzle.append([int(j) for j in i.split()])    
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
    def get_cell(self,puzzle,cell):
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
            self.print_puzzle(self.puzzle)
            return True
        else:
            c_cell=empty_cells[0]
            for i in range(1,10):
                print(c_cell,i)
                if self.cell_check(self.puzzle,c_cell,i):
                    self.puzzle[c_cell[0]][c_cell[1]]=i

                    if self.simpleBT(empty_cells[1:]):
                        return True
                self.puzzle[c_cell[0]][c_cell[1]]=0
        return False


s=sudoku('puzzle3.txt')
print(s.simpleBT(s.empty_cells))