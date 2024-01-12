# 记录这个方格附件邻居排列的编号

neibor_num_list = []
COLS = 0
ROWS = 0

def init(cols, rows):
    global neibor_num_list, COLS, ROWS
    COLS = cols
    ROWS = rows
    neibor_num_list = [[0 for _ in range(COLS)] for _ in range(ROWS)]

#增加周围邻居数量
def add_neighbor(x, y):
    global neibor_num_list
    will_be_alived = []
    nolonger_be_alived = []
    for (neib_x, neib_y) in get_neighbors_list(x, y):
        if (neibor_num_list[neib_x][neib_y] == 2):
            will_be_alived.append((neib_x, neib_y))
        elif (neibor_num_list[neib_x][neib_y] == 3):
            nolonger_be_alived.append((neib_x, neib_y))
        neibor_num_list[neib_x][neib_y] += 1
    return  will_be_alived, nolonger_be_alived

#减少周围邻居数量
def remove_neighbor(x, y):
    global neibor_num_list
    will_be_alived = []
    nolonger_be_alived = []
    for (neib_x, neib_y) in get_neighbors_list(x, y):
        if (neibor_num_list[neib_x][neib_y] == 4):
            will_be_alived.append((neib_x, neib_y))
        elif (neibor_num_list[neib_x][neib_y] == 3):
            nolonger_be_alived.append((neib_x, neib_y))
        neibor_num_list[neib_x][neib_y] -= 1
    return  will_be_alived, nolonger_be_alived

#获取方格周围邻居们的坐标列表
def get_neighbors_list(x, y):
    if (x == 0): #第一列
        if (y == 0): #第一行
            return [(x+1, y), (x, y+1), (x+1, y+1)]
        elif (y == ROWS-1): #最后一行
            return [(x+1, y), (x, y-1), (x+1, y-1)]
        else: #其他行
            return [(x+1, y), (x, y+1), (x, y-1), (x+1, y+1), (x+1, y-1)]
    elif (x == COLS-1): #最后一列
        if (y == 0): #第一行
            return [(x-1, y), (x, y+1), (x-1, y+1)]
        elif (y == ROWS-1): #最后一行
            return [(x-1, y), (x, y-1), (x-1, y-1)]
        else: #其他行
            return [(x-1, y), (x, y+1), (x, y-1), (x-1, y+1), (x-1, y-1)]
    else: #其他列
        if (y == 0): #第一行
            return [(x-1, y), (x, y+1), (x+1, y), (x-1, y+1), (x+1, y+1)]
        elif (y == ROWS-1): #最后一行
            return [(x-1, y), (x, y+1), (x+1, y), (x-1, y-1), (x+1, y-1)]
        return [(x-1, y), (x+1, y), (x, y+1), (x, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1), (x-1, y-1)]
    
#返回neibor_num_list
def get_neibor_num_list(): 
    global neibor_num_list
    return neibor_num_list