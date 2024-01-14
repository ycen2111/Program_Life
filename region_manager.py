import config
#记录元素位置和大小，判断当前鼠标所在的是哪个区域

WIDTH = config.ROWS * (config.GRID_SIZE + config.GRID_GAP) + config.GRID_GAP
GRID_WIDTH = WIDTH
GRID_HEIGHT = config.COLS * (config.GRID_SIZE + config.GRID_GAP) + config.GRID_GAP
MENU_WIDTH = WIDTH
MENU_HEIGHT = int (GRID_HEIGHT * 0.07)
MOUSE_INFO_WIDTH = 120
MOUSE_INFO_HEIGHT = 40
BAR_INFO_WIDTH = 100
BAR_INFO_HEIGHT = 40
HEIGHT = GRID_HEIGHT + MENU_HEIGHT
#(start x, start y, stop x, stop y)
MENU_AREA = (0,0,WIDTH,MENU_HEIGHT)
GRID_AREA = (0,MENU_HEIGHT,WIDTH,HEIGHT)

def get_menu_start_point():
    return (0,0)

def get_menu_size():
    return (WIDTH,MENU_HEIGHT)

def get_grid_start_point():
    return (0,MENU_HEIGHT)

def get_grid_size():
    return (WIDTH,GRID_HEIGHT)

def in_grid_region(position):
    x = position[0]
    y = position[1]

    if (x > 0 and x < WIDTH and y > MENU_HEIGHT and y < HEIGHT):
        return True
    else:
        return False

def get_mouse_info_size():
    return (MOUSE_INFO_WIDTH,MOUSE_INFO_HEIGHT)

def get_bar_info_size():
    return (BAR_INFO_WIDTH,BAR_INFO_HEIGHT)