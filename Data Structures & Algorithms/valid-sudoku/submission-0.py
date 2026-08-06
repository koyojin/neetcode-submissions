class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            a = defaultdict(int)

            for j in range(9):
                if board[i][j].isnumeric():
                    a[board[i][j]]+=1
                else:
                    pass
            print(a)
            if not all(e<=1 for e in a.values()):
                return False
        
        for k in range(9):
            b = defaultdict(int)

            for l in range(9):
                if board[l][k].isnumeric():
                    b[board[l][k]]+=1
                else:
                    pass
            print(b)

            if not all(f<=1 for f in b.values()):
                return False  
            
        for p in range(3):
            for k in range(3):
                c = defaultdict(int)

                for m in range(3):
                    for n in range(3):
                        if board[m+3*p][n+3*k].isnumeric():
                            c[board[m+3*p][n+3*k]]+=1
                        else:
                            pass       
                print(c)
                if not all(g<=1 for g in c.values()):
                    return False  
        return True
                