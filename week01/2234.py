import copy
def search(start,direction,area):

    if len(direction) == 0:
        return area
    else:
        for w in direction:
            if w=='N':
                move = (start[0]-1,start[1])
                # print('move:',move)
                if move[0] >= 0:
                    next_dir = copy.deepcopy(wall_info[table[move[0]][move[1]]])
                    if 'S' in next_dir and move in index:
                        area.append(move)
                        index.remove(move)
                        next_dir.remove('S')
                        search(move,next_dir,area)
            elif w=='E':
                move = (start[0],start[1]+1)
                # print('move:',move)
                if move[1] < m:
                    next_dir = copy.deepcopy(wall_info[table[move[0]][move[1]]])
                    if 'W' in next_dir and move in index:
                        area.append(move)
                        index.remove(move)
                        next_dir.remove('W')
                        search(move,next_dir,area)
            elif w=='S':
                move = (start[0]+1,start[1])
                # print('move:',move)
                if move[0] < n:
                    next_dir = copy.deepcopy(wall_info[table[move[0]][move[1]]])
                    if 'N' in next_dir and move in index:
                        area.append(move)
                        index.remove(move)
                        next_dir.remove('N')
                        search(move,next_dir,area)
            elif w=='W':
                move = (start[0],start[1]-1)
                # print('move:',move)
                if move[1] >= 0:
                    next_dir = copy.deepcopy(wall_info[table[move[0]][move[1]]])
                    if 'E' in next_dir and move in index:
                        area.append(move) 
                        index.remove(move)
                        next_dir.remove('E')
                        search(move,next_dir,area)
def distance(point1,point2):
    if (abs(point1[0]-point2[0])==1 and point1[1]==point2[1]) or (abs(point1[1]-point2[1])==1 and point1[0]==point2[0]):
        return 1
    return -1

m,n = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
wall_info = {0:['N','E','S','W'], 1:['N','E','S'], 2:['E','S','W'],  4:['N','S','W'], 8:['N','E','W'], 
             3:['E','S'], 5:['N','S'], 6:['S','W'], 9:['N','E'], 10:['E','W'], 12:['N','W'],
             7:['S'], 11:['E'], 13:['N'], 14:['W'], 15:[]}

index = [(x,y) for x in range(n) for y in range(m)]
result = []
size = []
bigger = []
while len(index) != 0:
    for i in index:
        # print("start:",i)
        index.remove(i)
        area = [i]
        area.append(search(i,wall_info[table[i[0]][i[1]]],area))
        area = area[0:len(area)-1]
        size.append(len(area))
        result.append(area)

for i in range(len(result)):
    for j in range(i+1,len(result)):
        for x in result[i]:
            for y in result[j]:
                if distance(x,y) == 1:
                    bigger.append(size[i]+size[j])
print(len(result))
print(max(size))
print(max(bigger)) 

            
