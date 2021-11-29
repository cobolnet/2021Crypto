'''
#2021 정보보안
#4조
#20163048 남시현
'''
from sys            import stdin
import sys
from mkeyShift      import Mstate, Mkey, Shift, dShift
from box            import fill_box, down_row_shift, up_row_shift, left_col_shift, right_col_shift
from hexadoku       import CreateTable as _CreateTable
from table          import p_table, xor_table
from test           import hexadoku, puzzle
from padding        import zeroPadding as _pad
import numpy as np
import binascii
import time
#import mkeyShift,hexadoku,box,table,test


def CreateState(_text): #평문 -> 256 16*16
    state = Mstate(_text)
    return state

def CreateKey(_text):    #평문 -> 키
    key = Mkey(_text)
    return key

def CreateBox(_key): #키 -> 박스
    cBox = fill_box(_key)
    return cBox

def CreateTable(_box) : #key -> box -> table
    eTable = _CreateTable( _box )      #empty table

    if (hexadoku(eTable, 0, 0)):  # 헥사도쿠 알고리즘
        cTable = puzzle(eTable)  # 완성된 테이블 가져오기 (10진수)

    return cTable



''''''''''''''''''''''''''''''



def Round(_state, _key,_box,_table) :  #key_s - 테이블전치 - xor - box_s

    _key = Shift(_key)             #shift key
    state = p_table(_state, _table)   #table 전치
    state = xor_table(_state, _key)    #XOR

    return state

def BoxShift(_box,_round):    #8까지 우하 16까지 좌상

    if round < 9:
        if _round % 2 == 0 :
            _box = down_row_shift(_box)
        else:
            _box = right_col_shift(_box)

    else :
        if _round % 2 == 0:
            _box = left_col_shift(_box)
        else:
            _box = up_row_shift(_box)

    return 0


''''''''''''''''''''''''''''''''''''''


def main():
    print('''
     _    _                                              
    | |  | |                                             
    | |__| | _____  ____ _                               
    |  __  |/ _ \ \/ / _` |                              
    | |  | |  __/>  < (_| |                              
    |_|__|_|\___/_/\_\__,_|            _   _             
    |  __ \                           | | (_)            
    | |  | | ___  ___ _ __ _   _ _ __ | |_ _  ___  _ __  
    | |  | |/ _ \/ __| '__| | | | '_ \| __| |/ _ \| '_ \ 
    | |__| |  __/ (__| |  | |_| | |_) | |_| | (_) | | | |
    |_____/ \___|\___|_|   \__, | .__/ \__|_|\___/|_| |_|
                            __/ | |                      
                           |___/|_|                          
    ''')

    print("----- 암호문을 입력하세요. -----")
    cText = input()
    #print(cText)
    print("----- 키를 입력하세요 -----")
    key = input()
    print("----- 복호화를 시작합니다. -----")
    start = time.time()
    cEncode = _pad(cText)


    byteC = []  #블록 리스트

    bitArr = []
    bitRow = []   
    for i in range( int(len(cEncode) / 32)): #32바이트 == 256비트씩 끊어 블록으로 만들기
        byteC.append(cEncode[ i * 32 : i * 32 + 32])


    #binscii = binascii.hexlify(cEncode.encode('utf-8'))
    rowCnt = 0
    for u in range(len(byteC)): #블록
        #print(byteC[u])
        for i in range(32): #한 블록의 한 행
            for k in range(7,-1,-1): #리스트에 넣기
                tmp = byteC[u][i]

                bitRow.append(((tmp >> k) & 1))
            rowCnt += 1
            if(rowCnt == 2):
                bitArr.append(bitRow)
                bitRow = []
                rowCnt = 0
        print("========= 블록 번호" + str(u) +" =========")
        print(bitArr)
        bitArr = []
    end = time.time()

    print(end - start)
            

#if __name__=="__main__":
main()