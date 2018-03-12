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
                if puzzle[i][j]=='0':
                    empty_cells.append((i,j))
        return empty_cells
    def read_puzzle(self,puzzle_name):
        fl=open(puzzle_name,'r')
        self.puzzle=[]
        s=fl.readlines()
        for i in s:
            self.puzzle.append(i.split())    
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
    def cell_check(self,puzzle,cell,value):
        row=puzzle[cell[0]]
        if value in row:
            return False
        col=[puzzle[i][cell[1]] for i in range(0,9)]
        if value in col:
            return False
        if(cell[0]<3):
            c_r=1
        elif cell[0]<6:
            c_r=4
        else:
            c_r=7
        if(cell[1]<3):
            c_c=1
        elif cell[0]<6:
            c_c=4
        else:
            c_c=7
        cell=[puzzle[c_r][c_c],puzzle[c_r-1][c_c-1],puzzle[c_r-1][c_c],puzzle[c_r-1][c_c+1],puzzle[c_r][c_c-1],puzzle[c_r][c_c+1],puzzle[c_r+1][c_c-1],puzzle[c_r+1][c_c],puzzle[c_r+1][c_c+1]]
        if value in cell:
            return False
        print(row,col,cell)
        return True
s=sudoku('puzzle3.txt')
