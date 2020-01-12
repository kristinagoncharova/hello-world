import os, random, time

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

size = 10
#inital state
#0 - space
#1 - rock
#2 - fish
#3 - shrimp
random.seed(42)
data = [[str(random.randint(0,3)) for _ in range(size)]for _ in range(size)]

def screen(size,data):
    print("".join(['#' for _ in range(2*size+1)]))
    for i in range(size):
        print("#"+"#".join(data[i])+"#")

    print("".join(['#' for _ in range(2*size+1)]))

def count_neigh(x,y, data):
    res = {0:0,1:0,2:0,3:0}
    for a in range(-1,2):
        for b in range(-1,2):
            if not (a==0 and b==0):
                if x+a >=0 and y+b >=0:
                    try:
                        res[int(data[x+a][y+b])]+=1
                    except IndexError:
                        pass
    return res




while True:
    screen(size,data)
    data1 = data

    for i in range(size):
        for j in range(size):
            neigh = count_neigh(i,j, data)
            if data[i][j]=='1':
                pass
            elif data[i][j]=='2': #fish
                if neigh[2] > 3 or neigh[2]<2:
                    data1[i][j]="0"
            elif data[i][j]=='3': #shrimp
                if neigh[3] > 3 or neigh[3]<2:
                    data1[i][j]="0" 
            elif data[i][j]=='0': #space
                if neigh[2] == 3:
                    data1[i][j]=='2'
                elif neigh[3] == 3:
                    data1[i][j]=='3'
    data = data1
    time.sleep(5)
    clear()
    
print(data[3][5])
print(count_neigh(3,5, data)[2])
