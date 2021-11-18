# 2021 정보보안
# 4조
# 20163080 전유승
import box
import numpy as np


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
