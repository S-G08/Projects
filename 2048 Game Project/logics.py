import random

def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat

def add_new_2(mat):
    r=random.randint(0,3)
    c=random.randint(0,3)
    while mat[r][c]!=0:
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2

def get_curr_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j]==2048:
                return "WON"
    
    # If any empty postion is present in matrix
    for i in range(4):
        for j in range(4):
            if mat[i][j]==0:
                return "Game Not Over"
    
    # If there are same consecutive numbers that can be combined
    for i in range(3):
        for j in range(3):
            if (mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]):
                return "Game Not Over"
            
    # checking for same numbers in last row
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return "Game Not Over"
    
    # checking for same numbers in last column
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return "Game Not Over"
        
    return "LOST"
    