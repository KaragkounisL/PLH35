col1 = [0x2b, 0x7e, 0x15, 0x16]
col2 = [0x8a, 0x84, 0xeb, 0x01]
rcon = [0x01, 0x00, 0x00, 0x00]


def xor(list1, list2):
    result = []
    for i in range(len(list1)):
        result.append((list1[i] ^ list2[i]))
    return result


def xor_rcon_results():
    result = xor(xor(col1, col2), rcon)
    for i in result:
        print(hex(i))


# multiplication function in the Galois Field GF(2^8)
def galois_mult(a, b):
    p = 0
    hiBitSet = 0
    for i in range(8):
        if b & 1 == 1:
            p ^= a
        hiBitSet = a & 0x80
        a <<= 1
        if hiBitSet == 0x80:
            a ^= 0x1b
        b >>= 1
    return p


# Fixed matrix for the Galois Field
row_gf = [[0x02, 0x03, 0x01, 0x01], [0x01, 0x02, 0x03, 0x01],
          [0x01, 0x01, 0x02, 0x03], [0x03, 0x01, 0x01, 0x02]]

# Inserting the columns of the matrix for mixing
matrix_col = [[0xd4, 0xbf, 0x5d, 0x30], [0xe0, 0xb4, 0x52, 0xae],
              [0xb8, 0x41, 0x11, 0xf1], [0x1e, 0x27, 0x98, 0xe5]]


def galois(matrix_col, row_gf):
    final = []
    for col in matrix_col:
        row1 = []
        row1.clear()
        for row in row_gf:
            for i in range(len(row)):
                if i == 0:
                    xor_arr = galois_mult(row[i], col[i])
                else:
                    xor_arr ^= galois_mult(row[i], col[i])
            row1.append(xor_arr)
        final.append(row1)
    return final


def galois_results():
    final = galois(matrix_col, row_gf)
    for list in final:
        print("Column", final.index(list) + 1)
        for i in list:
            print(hex(i)[-2:], end=' ')
        print()


galois_results()
