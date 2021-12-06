'''
#2021 정보보안
#4조
#20163081 정금종
#20163048 남시현
'''
from sys import stdin
import sys
from mkeyShift import Mstate, Mkey, Shift, dShift
from box import fill_box, down_row_shift, up_row_shift, left_col_shift, right_col_shift
from shiftBoxTable import *
from hexadoku import CreateTable as _CreateTable
from table import p_table, str_to_bool, xor_table, xor_table2
from test import hexadoku, puzzle
from padding import zeroPadding as _pad
from padding import utfD as _d
import numpy as np
import binascii
import time, copy

'''
20163048 남시현
'''


# 평문 -> 256 16*16
def CreateState(_text):
    state = Mstate(_text)
    return state


# 평문 -> 키
def CreateKey(_text):
    key = Mkey(_text)
    return key


# 키 -> 박스
def CreateBox(_key):
    cBox = fill_box(_key)
    return cBox


# key -> box -> table
# empty table
def CreateTable(_box):
    global cTable
    eTable = _CreateTable(_box)

    # 헥사도쿠 알고리즘
    if hexadoku(eTable, 0, 0):
        # 완성된 테이블 가져오기 (10진수)
        cTable = puzzle(eTable)

    return cTable


# 생성된 스도쿠박스 시프트
def BoxShift(_box, _round):
    if _round % 2 == 0:
        _box = right_shift_table(_box)
    elif _round % 2 == 1:
        _box = down_shift_table(_box)
    return _box


def HexaShift(_sudoku, _round):
    if _round % 2 == 0:
        _sudoku = right_move_box(_sudoku)
    elif _round % 2 == 1:
        _sudoku = down_move_box(_sudoku)
    return _sudoku


'''
20163081 정금종
'''


def main():
    print('''
 ___  ___  _______      ___    ___ ________                ___      ___  _____      ________               
|\  \|\  \|\  ___ \    |\  \  /  /|\   __  \              |\  \    /  /|/ __  \    |\   __  \              
\ \  \\ \  \ \   __/|   \ \  \/  / | \  \|\  \             \ \  \  /  / /\/_|\  \   \ \  \|\  \             
 \ \   __  \ \  \_|/__  \ \    / / \ \   __  \             \ \  \/  / /\|/ \ \  \   \ \  \\\   \            
  \ \  \ \  \ \  \_|\ \  /     \/   \ \  \ \  \             \ \    / /      \ \  \ __\ \  \\\   \           
   \ \__\ \__\ \_______\/  /\   \    \ \__\ \__\             \ \__/ /        \ \__\\__\  \_______\          
    \|__|\|__|\|_______/__/ /\ __\    \|__|\|__|              \|__|/          \|__\|__|\|_______|          
                       |__|/ \|__|                                                                         
                                                                                                           
                                                                                                           
 _______   ________   ________  ________      ___    ___ ________  _________  ___  ________  ________      
|\  ___ \ |\   ___  \|\   ____\|\   __  \    |\  \  /  /|\   __  \|\___   ___\\\\  \|\   __  \|\   ___  \    
\ \   __/|\ \  \\\\ \  \ \  \___|\ \  \|\  \   \ \  \/  / | \  \|\  \|___ \  \_\ \  \ \  \|\  \ \  \\\\ \  \   
 \ \  \_|/_\ \  \\\\ \  \ \  \    \ \   _  _\   \ \    / / \ \   ____\   \ \  \ \ \  \ \  \\\\\  \ \  \\\\ \  \  
  \ \  \_|\ \ \  \\\\ \  \ \  \____\ \  \\\\  \|   \/  /  /   \ \  \___|    \ \  \ \ \  \ \  \\\\\  \ \  \\\\ \  \ 
   \ \_______\ \__\\\\ \__\ \_______\ \__\\\\ _\ __/  / /      \ \__\        \ \__\ \ \__\ \_______\ \__\\\\ \__\\
    \|_______|\|__| \|__|\|_______|\|__|\|__|\___/ /        \|__|         \|__|  \|__|\|_______|\|__| \|__|
                                            \|___|/                                                        
                                                                                                           
    Hexa Encryption v1.0                                                                                                                                                    
    ''')

    print("----- 평문을 입력하세요. -----")
    pText = input()
    print("----- 키를 입력하세요 -----")
    key = CreateKey(input())
    _key = copy.deepcopy(key)
    print("----- 암호화를 시작합니다. -----")
    start = time.time()
    # 암호화 할 때
    pEncode = _pad(pText)
    cTextList = []
    # 블록 리스트
    byteC = []
    # 256 단위의 블록 1개
    bitArr = []
    # 한 블록의 한 행
    bitRow = []
    # 32바이트 == 256비트씩 끊어 블록으로 만들기
    for i in range(int(len(pEncode) / 32)):
        byteC.append(pEncode[i * 32: i * 32 + 32])

    # 키로 박스 만들기
    box = CreateBox(key)

    # 박스로 테이블 만들기
    table = CreateTable(box)
    _table = copy.deepcopy(table)

    rowCnt = 0
    # 블록
    for u in range(len(byteC)):
        # 한 블록의 한 행
        for i in range(32):
            # 리스트에 넣기
            for k in range(7, -1, -1):
                tmp = byteC[u][i]
                if ((tmp >> k) & 1) == 1:
                    bitRow.append(True)
                else:
                    bitRow.append(False)
                # bitRow.append(((tmp >> k) & 1))
            rowCnt += 1
            if rowCnt == 2:
                bitArr.append(bitRow)
                bitRow = []
                rowCnt = 0

        # 여기다가 복호화/암호화 추가
        roundText = bitArr
        # 16라운드
        for j in range(16):
            # table 전치
            roundText = p_table(roundText, _table)
            # XOR
            roundText = xor_table(roundText, _key)
            _table = BoxShift(_table, j)
            _table = HexaShift(_table, j)
            # shift key
            _key = Shift(_key)

        cTextList.append(roundText)

        # bitArr 저장 필요
        bitArr = []
    end = time.time()

    cTextBit = ""
    cText = ""
    # 블록 수
    for p in range(len(byteC)):
        for pp in range(16):
            for ppp in range(16):
                if cTextList[p][pp][ppp]:
                    cTextBit += '1'
                else:
                    cTextBit += '0'

    for b in range(0, len(cTextBit), 8):
        cText += (str(hex(int(cTextBit[b:8 + b], 2))))

    cTexts = cText.split('0x')

    for kk in range(len(cTexts)):
        if len(str(cTexts[kk])) == 1:
            cTexts[kk] = '0' + cTexts[kk]

    print(''.join(cTexts))
    print('----- 암호문이 완성되었습니다. -----')
    print("소요시간 : " + str(end - start) + "초")


if __name__ == '__main__':
    main()
