dict = {'0':'0000', '1':'0001', '2':'0010','3':'0011', '4':'0100', '5':'0101', '6':'0110','7':'0111' ,
        '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1110', 'E':'1111'}
def hexToBinStr(hexV):

    if hexV.isdigit():
        numV = int(hexV)
    else:
        numV = ord(hexV) - ord('A') + 10

    tmp_res = ''
    for j in range(3, -1, -1):
        if numV & 1<<j:
            tmp_res += '1'
        else:
            tmp_res += '0'

    return tmp_res

lst = '0DEC'
res = ''
for i in range(0, len(lst)):
    res += hexToBinStr(lst[i])

patt = ['001101', '010011', '111011', '110001', '100011', '110111', '001011', '111101',
        '011001', '101111']
pos = 0
while pos < len(res):
    if res[pos:pos+6] in patt:
        print(patt.index(res[pos:pos+6]))
        pos += 6
    else:
        pos += 1