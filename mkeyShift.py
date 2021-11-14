'''
#2021 정보보안
#4조
#20163048 남시현
'''

import hashlib
import numpy as np


def Mstate(t): #평문 (8비트 * 32자) -> 2진수 리스트
    tList = list(t)
    tList16 = []
    tList10 = []
    tList2 = []
    rtList = []

    for i in tList:
        tList16.append(str(hex(ord(i))))

    for i in tList16:
        tList10.append(int(i, 16))

    for i in tList10:
        tList2.append(str((bin(i)[2:].zfill(8))))

    for i in tList2:
        rtList.append(list(i))

    rtList = np.reshape(rtList, (16, 16))

    return rtList   #16*16 state return







def Mkey(t):    #평문 -> sha256(4비트 * 64자) -> 2진수 리스트
    t = t.encode('utf-8')
    key = hashlib.sha256(t).hexdigest()
    keyList16 = list(key)
    keyList10 = []
    keyList2 = []
    keyList = []

    for i in keyList16:
        keyList10.append(int(i, 16))

    for i in keyList10:
        keyList2.append(str((bin(i)[2:].zfill(4))))

    for i in keyList2:
        keyList.append(list(i))

    keyList = np.reshape(keyList, (16, 16))

    return keyList



def Shift(keyList): # encription shift

    keyList = np.reshape(keyList, (16, 16))
    tmplist = keyList.copy()

    for idx_i in range(16):
        for idx_j in range(16):
            if idx_i == 0 and idx_j ==0:
                keyList[idx_i][idx_j] = tmplist[15][15]

            else:
                if idx_i == 0:
                    keyList[idx_i][idx_j] = tmplist[15][idx_j - 1]
                elif idx_j == 0:
                    keyList[idx_i][idx_j] = tmplist[idx_i - 1][15]
                else:
                    keyList[idx_i][idx_j] = tmplist[idx_i - 1][idx_j - 1]


    return keyList    #np.reshape(keyList,(1,256))



def dShift(keyList): #decription Shift
    tmplist = keyList.copy()

    print(tmplist)

    for idx_i in range(16):
        for idx_j in range(16):
            if idx_i == 15 and idx_j ==15:
                keyList[idx_i][idx_j] = tmplist[0][0]

            else:
                if idx_i == 15:
                    keyList[idx_i][idx_j] = tmplist[0][idx_j + 1]
                elif idx_j == 15:
                    keyList[idx_i][idx_j] = tmplist[idx_i + 1][0]
                else:
                    keyList[idx_i][idx_j] = tmplist[idx_i + 1][idx_j + 1]

    print(keyList)

    return np.reshape(keyList,(1,256))





def main(): #test
    t = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    Mstate(t)
    #dShift(Mkey(t))

if __name__=="__main__":
    main()