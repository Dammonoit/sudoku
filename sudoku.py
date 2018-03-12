class sudoku:
    def __init__(self,puzzle_name):
        self.puzzle_name=puzzle_name
        self.read_puzzle(self.puzzle_name)
        self.print_puzzle(self.puzzle)
        self.write_puzzle('nn.txt')

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