import hashlib
import numpy as np


def Mkey(t):    #평문 -> 2진수 리스트
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



def Shift(keyList): # shift
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



    return np.reshape(keyList,(1,256))


def main():
    t = "test"

    print( Shift(Mkey(t)) )

if __name__=="__main__":
    main()