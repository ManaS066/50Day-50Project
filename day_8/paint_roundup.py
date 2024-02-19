import math
def paint_wall(height ,width,cover):
    num_cans=(height*width)/cover
    round=math.ceil(num_cans)
    print(f"no of cans required to pain ta wall is:{round}")
paint_wall(10,20,4)