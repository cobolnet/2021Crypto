# 2021 정보보안
# 4조
# 20163080 전유승
import numpy as np


# 16*16 state와 16*16 key 테이블 xor
def xor_table(state, key):
    t_state = np.logical_xor(state, key)
    return t_state


# 16*16 state와 16*16 스도쿠 테이블
def p_table(state, sudoku):
    t_state = [[-1] * 16 for _ in range(16)]
    for i in range(4):
        for j in range(4):
            # state[0][0]~[3][3]
            if sudoku[i][j] == '0x0':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[0][0]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[0][1]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[0][2]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[0][3]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[1][0]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[1][1]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[1][2]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[1][3]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[2][0]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[2][1]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[2][2]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[2][3]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[3][0]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[3][1]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[3][2]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[3][3]
                        else:
                            print("index2 isn't valid!")
            # state[0][4]~[3][7]
            elif sudoku[i][j] == '0x1':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[0][4]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[0][5]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[0][6]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[0][7]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[1][4]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[1][5]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[1][6]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[1][7]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[2][4]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[2][5]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[2][6]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[2][7]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[3][4]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[3][5]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[3][6]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[3][7]
                        else:
                            print("index2 isn't valid!")
            # state[0][8]~[3][11]
            elif sudoku[i][j] == '0x2':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[0][8]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[0][9]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[0][10]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[0][11]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[1][8]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[1][9]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[1][10]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[1][11]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[2][8]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[2][9]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[2][10]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[2][11]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[3][8]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[3][9]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[3][10]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[3][11]
                        else:
                            print("index2 isn't valid!")
            # state[0][12]~[3][15]
            elif sudoku[i][j] == '0x3':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[0][12]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[0][13]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[0][14]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[0][15]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[1][12]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[1][13]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[1][14]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[1][15]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[2][12]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[2][13]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[2][14]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[2][15]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[3][12]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[3][13]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[3][14]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[3][15]
                        else:
                            print("index2 isn't valid!")
            # state[4][0]~[7][3]
            elif sudoku[i][j] == '0x4':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[4][0]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[4][1]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[4][2]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[4][3]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[5][0]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[5][1]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[5][2]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[5][3]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[6][0]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[6][1]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[6][2]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[6][3]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[7][0]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[7][1]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[7][2]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[7][3]
                        else:
                            print("index2 isn't valid!")
            # state[4][4]~[7][7]
            elif sudoku[i][j] == '0x5':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[4][4]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[4][5]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[4][6]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[4][7]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[5][4]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[5][5]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[5][6]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[5][7]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[6][4]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[6][5]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[6][6]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[6][7]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[7][4]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[7][5]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[7][6]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[7][7]
                        else:
                            print("index2 isn't valid!")
            # state[4][8]~[7][11]
            elif sudoku[i][j] == '0x6':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[4][8]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[4][9]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[4][10]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[4][11]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[5][8]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[5][9]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[5][10]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[5][11]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[6][8]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[6][9]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[6][10]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[6][11]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[7][8]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[7][9]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[7][10]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[7][11]
                        else:
                            print("index2 isn't valid!")
            # state[4][12]~[7][15]
            elif sudoku[i][j] == '0x7':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[4][12]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[4][13]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[4][14]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[4][15]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[5][12]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[5][13]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[5][14]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[5][15]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[6][12]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[6][13]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[6][14]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[6][15]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[7][12]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[7][13]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[7][14]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[7][15]
                        else:
                            print("index2 isn't valid!")
            # state[8][0]~[11][3]
            elif sudoku[i][j] == '0x8':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[8][0]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[8][1]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[8][2]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[8][3]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[9][0]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[9][1]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[9][2]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[9][3]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[10][0]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[10][1]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[10][2]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[10][3]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[11][0]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[11][1]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[11][2]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[11][3]
                        else:
                            print("index2 isn't valid!")
            # state[8][4]~[11][7]
            elif sudoku[i][j] == '0x9':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[8][4]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[8][5]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[8][6]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[8][7]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[9][4]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[9][5]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[9][6]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[9][7]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[10][4]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[10][5]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[10][6]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[10][7]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[11][4]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[11][5]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[11][6]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[11][7]
                        else:
                            print("index2 isn't valid!")
            # state[8][8]~[11][11]
            elif sudoku[i][j] == '0xa':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[8][8]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[8][9]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[8][10]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[8][11]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[9][8]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[9][9]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[9][10]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[9][11]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[10][8]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[10][9]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[10][10]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[10][11]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[11][8]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[11][9]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[11][10]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[11][11]
                        else:
                            print("index2 isn't valid!")
            # state[8][12]~[11][15]
            elif sudoku[i][j] == '0xb':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[8][12]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[8][13]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[8][14]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[8][15]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[9][12]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[9][13]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[9][14]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[9][15]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[10][12]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[10][13]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[10][14]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[10][15]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[11][12]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[11][13]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[11][14]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[11][15]
                        else:
                            print("index2 isn't valid!")
            # state[12][0]~[15][3]
            elif sudoku[i][j] == '0xc':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[12][0]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[12][1]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[12][2]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[12][3]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[13][0]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[13][1]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[13][2]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[13][3]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[14][0]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[14][1]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[14][2]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[14][3]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[15][0]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[15][1]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[15][2]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[15][3]
                        else:
                            print("index2 isn't valid!")
            # state[12][4]~[15][7]
            elif sudoku[i][j] == '0xd':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[12][4]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[12][5]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[12][6]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[12][7]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[13][4]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[13][5]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[13][6]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[13][7]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[14][4]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[14][5]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[14][6]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[14][7]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[15][4]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[15][5]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[15][6]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[15][7]
                        else:
                            print("index2 isn't valid!")
            # state[12][8]~[15][11]
            elif sudoku[i][j] == '0xe':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[12][8]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[12][9]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[12][10]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[12][11]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[13][8]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[13][9]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[13][10]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[13][11]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[14][8]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[14][9]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[14][10]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[14][11]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[15][8]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[15][9]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[15][10]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[15][11]
                        else:
                            print("index2 isn't valid!")
            # state[12][12]~[15][15]
            elif sudoku[i][j] == '0xf':
                for y in range(4):
                    for x in range(4):
                        r = (i * 4) + y
                        c = (j * 4) + x
                        if sudoku[r][c] == '0x0':
                            t_state[r][c] = state[12][12]
                        elif sudoku[r][c] == '0x1':
                            t_state[r][c] = state[12][13]
                        elif sudoku[r][c] == '0x2':
                            t_state[r][c] = state[12][14]
                        elif sudoku[r][c] == '0x3':
                            t_state[r][c] = state[12][15]
                        elif sudoku[r][c] == '0x4':
                            t_state[r][c] = state[13][12]
                        elif sudoku[r][c] == '0x5':
                            t_state[r][c] = state[13][13]
                        elif sudoku[r][c] == '0x6':
                            t_state[r][c] = state[13][14]
                        elif sudoku[r][c] == '0x7':
                            t_state[r][c] = state[13][15]
                        elif sudoku[r][c] == '0x8':
                            t_state[r][c] = state[14][12]
                        elif sudoku[r][c] == '0x9':
                            t_state[r][c] = state[14][13]
                        elif sudoku[r][c] == '0xa':
                            t_state[r][c] = state[14][14]
                        elif sudoku[r][c] == '0xb':
                            t_state[r][c] = state[14][15]
                        elif sudoku[r][c] == '0xc':
                            t_state[r][c] = state[15][12]
                        elif sudoku[r][c] == '0xd':
                            t_state[r][c] = state[15][13]
                        elif sudoku[r][c] == '0xe':
                            t_state[r][c] = state[15][14]
                        elif sudoku[r][c] == '0xf':
                            t_state[r][c] = state[15][15]
                        else:
                            print("index2 isn't valid!")
            else:
                print("index isn't valid!")

    # return 16*16 state
    return t_state

# def reverse_p_table(self, state, sudoku):
#     return t_state
