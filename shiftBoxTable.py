# 2021 정보보안
# 4조
# 20163080 전유승
import box
import numpy as np


# 테이블 내 박스를 병렬로 쉬프트함
def right_shift_table(sudoku):
    np_sudoku = np.array(sudoku)

    for i in range(4):
        for j in range(4):
            np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4] = \
                box.right_col_shift(np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4])

    return np_sudoku.tolist()


def down_shift_table(sudoku):
    np_sudoku = np.array(sudoku)

    for i in range(4):
        for j in range(4):
            np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4] = \
                box.down_row_shift(np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4])

    return np_sudoku.tolist()


def left_shift_table(sudoku):
    np_sudoku = np.array(sudoku)

    for i in range(4):
        for j in range(4):
            np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4] = \
                box.left_col_shift(np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4])

    return np_sudoku.tolist()


def up_shift_table(sudoku):
    np_sudoku = np.array(sudoku)

    for i in range(4):
        for j in range(4):
            np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4] = \
                box.up_row_shift(np_sudoku[i * 4:(i * 4) + 4,  j * 4:(j * 4) + 4])

    return np_sudoku.tolist()


# 테이블 내 박스의 위치를 상하좌우로 쉬프트함
def right_move_box(sudoku):
    np_sudoku = np.array(sudoku)
    temp = np.full([16, 16], 0)

    temp[:, 4:16] = np_sudoku[:, 0:12]
    temp[:, 0:4] = np_sudoku[:, 12:16]

    return temp.tolist()


def down_move_box(sudoku):
    np_sudoku = np.array(sudoku)
    temp = np.full([16, 16], 0)

    temp[4:16, :] = np_sudoku[0:12, :]
    temp[0:4, :] = np_sudoku[12:16, :]

    return temp.tolist()


def left_move_box(sudoku):
    np_sudoku = np.array(sudoku)
    temp = np.full([16, 16], 0)

    temp[:, 0:12] = np_sudoku[:, 4:16]
    temp[:, 12:16] = np_sudoku[:, 0:4]

    return temp.tolist()


def up_move_box(sudoku):
    np_sudoku = np.array(sudoku)
    temp = np.full([16, 16], 0)

    temp[0:12, :] = np_sudoku[4:16, :]
    temp[12:16, :] = np_sudoku[0:4, :]

    return temp.tolist()
