#游戏主逻辑控制
import my_data.actived_cell_list as actived_cell_list
import my_data.cell_data as cell_data
import my_data.grid_neighbor_number as neighbor_number

RUNNING = False

def start_sim():
    global RUNNING
    RUNNING = True

def stop_sim():
    global RUNNING
    RUNNING = False

def run_sim():
    global RUNNING
    if RUNNING:
        #获取次回合临近的cell
        neighbor_cell_list = actived_cell_list.get_keys_list()
        #获取当前存活cell的字典keys列表
        curr_cell_list = cell_data.get_keys_list()
        #获取当前neighbors
        curr_neighbors = list(neighbor_number.get_neibor_num_list())
        #遍历存活cell，寻找将死亡的cell
        dead_cell_list = []
        for coor in curr_cell_list:
            if (curr_neighbors[coor[0]][coor[1]] != 2 and curr_neighbors[coor[0]][coor[1]] != 3):
                dead_cell_list.append(coor)
        #遍历临近的cell，寻找将复活的cell
        lived_cell_list = []
        for coor in neighbor_cell_list:
            if (curr_neighbors[coor[0]][coor[1]] == 3):
                lived_cell_list.append(coor)
        #修改他们的状态
        for coor in lived_cell_list:
            cell_data.add_cell_level(coor[0], coor[1])
        for coor in dead_cell_list:
            cell_data.sub_cell_level(coor[0], coor[1])
    
    #RUNNING = False