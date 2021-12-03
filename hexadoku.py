# 2021 정보보안
# 4조
# 20163081 정금종

##
# 최초 헥사도쿠 테이블 생성을 위한 박스를 전달받아 초기 값을 설정한다.
##

from box import fill_box
import numpy as np


# 박스 -> 빈 테이블


def CreateTable(_box):  # 호출 수정
    bx = _box.copy()

    hexadokuTable = [
        [bx[0], bx[1], bx[2], bx[3], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [bx[4], bx[5], bx[6], bx[7], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [bx[8], bx[9], bx[10], bx[11], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [bx[12], bx[13], bx[14], bx[15], -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

    return hexadokuTable
