#记录下一个回合会有生命的无生命方格
import my_data.cell_data as cell_data
import my_data.grid_neighbor_number as neighbor

actived_cell_list = {}

#寻找lived_cell邻居，输出actived_cell_list keys列表，并清空字典
def get_keys_list():
    get_neighbor_cells()
    output = list(actived_cell_list.keys())
    actived_cell_list.clear()
    return output

#调用neighbor.get_neighbors_list列出所有和cell_data.lived_cell字典相邻的方格，保存在actived_cell_list字典里
def get_neighbor_cells():
    for cell in cell_data.lived_cell.keys():
        x = cell[0]
        y = cell[1]
        neighbor_list = neighbor.get_neighbors_list(x, y)
        for cell_id in neighbor_list:
            if cell_id not in actived_cell_list.keys() and cell_id not in cell_data.lived_cell.keys():
                actived_cell_list[cell_id] = True