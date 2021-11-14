# 2021 정보보안
# 4조
# 20163080 전유승
# fill box with initial key list
def fill_box(key):
    t_list = [-1 for _ in range(16)]
    zero_to_f = [0 for _ in range(16)]
    dec_to_hex = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8,
                  9: 9, 10: 0xa, 11: 0xb, 12: 0xc, 13: 0xd, 14: 0xe, 15: 0xf}

    index = 0
    for i in range(16):
        temp_var = key[i][:]
        temp_str = ''.join(temp_var)
        temp_str2 = '0b' + temp_str
        temp_int = int(temp_str2, 2)

        temp_int %= 16

        if zero_to_f[temp_int] == 1:
            index += 1
            continue

        t_list[index] = dec_to_hex[temp_int]
        zero_to_f[temp_int] = 1
        index += 1

    # To fill list wasn't get hex
    for i in range(16):
        if t_list[i] == -1:
            for j in range(16):
                if zero_to_f[j] == 0:
                    zero_to_f[j] = 1
                    t_list[i] = dec_to_hex[j]
                    break

    # Convert 1D to 2D list
    # for i in range(4):
    #     for j in range(4):
    #         box[i][j] = t_list[(i * 4) + j]

    return t_list


def right_col_shift(box):
    c_temp = [box[0][3], box[1][3], box[2][3], box[3][3]]

    for x in range(2, -1, -1):
        for y in range(4):
            box[y][x + 1] = box[y][x]

    for i in range(4):
        box[i][0] = c_temp[i]

    return box


def down_row_shift(box):
    r_temp = [box[3][0], box[3][1], box[3][2], box[3][3]]

    for y in range(2, -1, -1):
        for x in range(4):
            box[y + 1][x] = box[y][x]

    for i in range(4):
        box[0][i] = r_temp[i]

    return box


def left_col_shift(box):
    c_temp = [box[0][0], box[1][0], box[2][0], box[3][0]]

    for x in range(1, 4):
        for y in range(4):
            box[y][x - 1] = box[y][x]

    for i in range(4):
        box[i][3] = c_temp[i]

    return box


def up_row_shift(box):
    r_temp = [box[0][0], box[0][1], box[0][2], box[0][3]]

    for y in range(1, 4):
        for x in range(4):
            box[y - 1][x] = box[y][x]

    for i in range(4):
        box[3][i] = r_temp[i]

    return box
