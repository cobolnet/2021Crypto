#2021 정보보안
#4조
#20163081 정금종

def pkcs7(block):
    k = block.encode('utf-8')
    bsize = len(k)

    if (bsize <= 64):
        paddingSize = 64 - bsize
        t = bytes.fromhex(str(hex(paddingSize)[2:4]))

        k += (t * paddingSize)
    return str(k.decode('utf-8'))

#tt = pkcs7("테스트")

#print(tt)
#print(tt.encode('utf-8'))