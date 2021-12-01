'''
#2021 정보보안
#4조
#20163048 남시현
'''
from sys            import stdin
import sys
from mkeyShift      import Mstate, Mkey, Shift, dShift
from box            import fill_box, down_row_shift, up_row_shift, left_col_shift, right_col_shift
from shiftBoxTable  import *
from hexadoku       import CreateTable as _CreateTable
from table          import p_table, str_to_bool, xor_table
from test           import hexadoku, puzzle
from padding        import zeroPadding as _pad
from padding        import utfD as _d
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
    state = xor_table(_state, _key)    #XOR
    _key = dShift(_key)             #shift key
    state = p_table(_state, _table)   #table 전치
    

    return state

#
def BoxShift(_box,_round):    #생성된 스도쿠박스 시프트
    #if _round % 2 == 0:
    _box = left_shift_table(_box)
    #elif _round % 2 == 1 :
    _box = up_shift_table(_box)
    #return 0


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
    print("----- 키를 입력하세요 -----")
    key = CreateKey(input())
    print("----- 복호화를 시작합니다. -----")
    start = time.time()
    #cEncode = _pad(cText)   #암호화 할 때
    cEncode = _d(cText)    #복호화 할 때
    print(cText)
    print(cEncode)

    pTextList = []

    byteC = []  #블록 리스트
    bitArr = [] #256 단위의 블록 1개
    bitRow = [] #한 블록의 한 행  
    for i in range( int(len(cEncode) / 32)): #32바이트 == 256비트씩 끊어 블록으로 만들기
        byteC.append(cEncode[ i * 32 : i * 32 + 32])
    

    #키로 박스 만들기
    box = CreateBox(key)

    #박스로 테이블 만들기
    table = CreateTable(box)

    #Key의 원소를 Bool 타입으로 변환
    keyB = str_to_bool(key) 
    

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
        #print("========= 블록 번호" + str(u) +" =========")
        #print(bitArr)
        ####
        #여기다가 복호화/암호화 추가
        for j in range(16): #16라운드
            #print(roundBox)
            roundText = Round(bitArr,key,box,table)
            BoxShift(table,j)
            print("라운드 : "  + str(j))
            for rt in range(len(roundText)):
                print(roundText[rt],end='')
            print("\n")
        pTextList.append(roundText)
        ####
        #bitArr 저장 필요
        bitArr = []
    end = time.time()
    
    pTextBitCount = 0 
    pTextBit = ""
    pText = ""
    for p in range(len(byteC)): #블록 수
        for pp in range(16):
            for ppp in range(16):
                if (pTextList[p][pp][ppp]):
                    pTextBit += '1'
                else:
                    pTextBit += '0'

    print('\n----- 평문이 완성되었습니다. -----')
    for b in range(0,len(pTextBit) , 8):
        pText += (str(hex(int(pTextBit[b:8 + b])))[2:4])
    print(pText)
    print(bytes.fromhex(pText).decode('utf-8'))
    print('==================================')
    print(end - start)
            

#if __name__=="__main__":
main()