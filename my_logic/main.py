#游戏主逻辑控制
import my_data.actived_cell_list as actived_cell_list
import my_data.cell_data as cell_data
import my_data.grid_neighbor_number as neighbor_number

RUNNING = False
dead_cell_list = []

def start_sim():
    global RUNNING
    RUNNING = True

def stop_sim():
    global RUNNING
    RUNNING = False

def run_sim():
    global RUNNING
    global dead_cell_list
    if RUNNING:
        #获取次回合临近的cell
        neighbor_cell_list = actived_cell_list.get_keys_list()
        #获取当前存活cell的字典keys列表
        curr_cell_list = cell_data.get_keys_list()
        #获取当前neighbors
        curr_neighbors = list(neighbor_number.get_neibor_num_list())
        #遍历临近的cell，寻找将复活的cell
        level_up_cell_list = []
        for coor in neighbor_cell_list:
            if (curr_neighbors[coor[0]][coor[1]] == 3):
                level_up_cell_list.append(coor)
        #遍历存活cell，寻找将死亡的cell
        level_down_cell_list = []
        for coor in curr_cell_list:
            if (curr_neighbors[coor[0]][coor[1]] == 3):
                level_up_cell_list.append(coor)
            elif (curr_neighbors[coor[0]][coor[1]] != 2):
                level_down_cell_list.append(coor)
            # if (curr_neighbors[coor[0]][coor[1]] != 2 and curr_neighbors[coor[0]][coor[1]] != 3):
            #     dead_cell_list.append(coor)
        #修改他们的状态
        for coor in level_up_cell_list:
            # if (cell_data.add_cell_level(coor[0], coor[1])):#增加到了最大值
            #     dead_cell_list.append(coor)
            cell_data.add_cell_level(coor[0], coor[1])
        for coor in level_down_cell_list:
            cell_data.sub_cell_level(coor[0], coor[1])
        # for coor in dead_cell_list:
        #     if (cell_data.sub_cell_level(coor[0], coor[1])):#减小到了最小值
        #         dead_cell_list.remove(coor)
    
    #RUNNING = False