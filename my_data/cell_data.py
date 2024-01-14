import config
import grid_info.grid_color as color
import my_data.grid_neighbor_number as neighbor
#用字典记录所有游戏数据

#存活方格cell列表
lived_cell = {}

#查询方格是否存活
def is_cell_alive(x, y):
    global lived_cell
    return (x, y) in lived_cell

#查询有多少方格存活
def count_alive_cell():
    global lived_cell
    return len(lived_cell)

#增加方格状态
#如果增加后到达最大值则返回True
def add_cell_level(x, y):
    global lived_cell
    (R, G, B) = color.color[x][y]
    if (R + config.ADD_COLOR_UNIT >= 255):
        #neighbor.remove_neighbor(x, y)
        color.change_color(x, y, (255, G, B))
        return True
    else:
        if (R == 0): #记录这个新生坐标
            lived_cell[x, y] = True
            neighbor.add_neighbor(x, y)
        color.change_color(x, y, (R + config.ADD_COLOR_UNIT, G, B))
        return False

#减少方格状态
#如果减小到最小值则返回True
def sub_cell_level(x, y):
    global lived_cell
    (R, G, B) = color.color[x][y]
    if (R <= config.SUB_COLOR_UNIT): #删除死亡坐标
        del lived_cell[x, y]
        neighbor.remove_neighbor(x, y)
        color.change_color(x, y, (0, G, B))
        return True
    else:
        color.change_color(x, y, (R - config.SUB_COLOR_UNIT, G, B))
        return False

#返回String格式信息
def get_string_info(x, y):
    global lived_cell
    info = []
    info.append("X: " + str(x) + "  Y: " + str(y))
    info.append("RGB: " + str(color.color[x][y]))
    info.append("neighbor: " + str(neighbor.neibor_num_list[x][y]))
    return info

#返回lived_cell keys
def get_keys_list():
    return list(lived_cell.keys())