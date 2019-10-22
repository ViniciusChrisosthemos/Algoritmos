def findNext(i,j,grid):
    firstIt = i*len(grid) + j
    
    for n in range(firstIt, len(grid)*len(grid[0])):
        row = int(n/len(grid))
        column = n % len(grid[0])
        if not grid[row][column]:
            return row, column

    return -1, -1

def getCandidates(i,j,grid):
    candidates = [True]*9

    for e in range(len(grid)):
        if grid[e][j]:
            candidates[grid[e][j]-1] = False
    
    for e in range(len(grid[0])):
        if grid[i][e]:
            candidates[grid[i][e]-1] = False
    
    fi = (int(i/3))*3
    fj = (int(j/3))*3

    for a in range(3):
        for b in range(3):
            if grid[fi+a][fj+b]:
                candidates[grid[fi+a][fj+b]-1] = False
    
    return [(idx+1) for idx,x in enumerate(candidates) if x]

def printGrid(grid):
    for a in grid:
        for b in a:
            print(b, end=' ')
        print('\n')

def sudoku(i,j,grid):
    i, j = findNext(i,j,grid)
    candidates = getCandidates(i, j, grid)
    
    if not len(candidates):
        print('Sem candidatos')
        return False

    printGrid(grid)
    print('*'*20)
    for candidate in candidates:
        print(candidate)
        grid[i][j] = candidate
        ni, nj = findNext(i, j, grid)
        if ni == -1:
            return True
        if sudoku(ni,nj,grid):
            return True
        else:
            grid[i][j] = 0
    return False


grid = [[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]

sudoku(0,0,grid)
printGrid(grid)
