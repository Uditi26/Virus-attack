import random
turn=0
TTT=[['1','2','3','4','5','6'],['7','8','9','10','11','12'],['13','14','15','16','17','18'],['19','20','21','22','23','24'],['25','26','27','28','29','30'],['31','32','33','34','35','36']]
v_cell=0
n=17
count=0
def toss():
    play=['head','tail']
    t=random.choice(play)
    ch=input()
    if ch==t:
        print("Virus or Antivirus")
        w=input()
        w=w.lower()
        if w=='virus':
            virus1()
        else:
            antivirus()

def update(i):
    i=int(i)
    if i<=6 and i>=1:
        row=0
        column=i-1
    elif i>6 and i<=12:
        row=1
        column=i-7
    elif i>12 and i<=18:
        row=2
        column=i-13
    elif i>18 and i<=24:
        row=3
        column=i-19
    elif i>24 and i<=30:
        row=4
        column=i-25
    else:
        row=5
        column=i-31    
    return row,column


def virus1():
    print("Enter the cell you want to place virus at:")
    global v_cell;
    v_cell=int(input())
    row,column=update(v_cell)
    TTT[row][column]='V'
    TTT[row][column+1]='B'
    TTT[row][column-1]='B'
    TTT[row+1][column]='B'
    TTT[row-1][column]='B'
    TTT[row+1][column+1]='B'
    TTT[row-1][column+1]='B'
    TTT[row+1][column-1]='B'
    TTT[row-1][column-1]='B'
    printing()
    print("Enter "+ str(n) + " more cells for bugs")
    for i in range(0,17):
        ele = int(input())
        row,column=update(ele)
        TTT[row][column]='B'

def printing():
    x = '\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in TTT])
    print(x)

def antivirus():
    print("Enter your move")
    cells=input().split()
    global v_cell;
    global count;
    row,column=update(v_cell)
    l=len(cells)
    for i in range(l):
        j=int(cells[i])
        r,c=update(j)
        check=checking(j,row,column)
        if check==1:
            TTT[r][c]='0'
            count=count+1
        else:
            print("Wrong cell entered, enter one more cell")
            l=l+1
            cells[l]=int(input())
    printing()

def checking(j,row,column):
    r,c=update(j)
    if r==row+1 and c==column+1 or r==row and c==column+1 or r==row and c==column-1 or r==row+1 and c==column or r==row-1 and c==column or r==row-1 and c==column-1 or r==row-1 and c==column+1 or r==row+1 and c==column-1:  
        return 0
    else:
        return 1
    
def virus2():
    print("Enter the cell you want to place virus at:")
    global v_cell;
    row,column=update(v_cell)
    TTT[row][column]=0
    v_cell=int(input())
    global n
    row,column=update(v_cell)
    while True:
        if TTT[row][column]=='B':
            print("Can't be placed there, enter another cell value")
            v_cell=int(input())
            row,column=update(v_cell)
        else:
            break
    TTT[row][column]='V'
    if TTT[row][column+1]!='B':
        n=n-1
    TTT[row][column+1]='B'
    if TTT[row][column-1]!='B':
            n=n-1
    TTT[row][column-1]='B'
    if TTT[row+1][column]!='B':
            n=n-1
    TTT[row+1][column]='B'
    if TTT[row-1][column]!='B':
            n=n-1
    TTT[row-1][column]='B'
    if TTT[row+1][column+1]!='B':
            n=n-1
    TTT[row+1][column+1]='B'
    if TTT[row-1][column+1]!='B':
            n=n-1
    TTT[row-1][column+1]='B'
    if TTT[row+1][column-1]!='B':
            n=n-1
    TTT[row+1][column-1]='B'
    if TTT[row-1][column-1]!='B':
            n=n-1
    TTT[row-1][column-1]='B'
    printing()
    print("Enter "+ str(n) + " more cells for virus")
    for i in range(0,int(n)):
        ele = int(input())
        row,column=update(ele)
        TTT[row][column]='B'


def Main():
     virus1()
     printing()
     for i in range(0,5):
        antivirus()    
     virus2()
     printing()
     for i in range(0,3):
            antivirus()
     virus2()
     printing()
     for i in range(0,3):
            antivirus()
     global count
     print(count)
# virus1()
# printing()
# antivirus()

Main() 