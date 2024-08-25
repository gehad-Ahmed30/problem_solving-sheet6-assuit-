def multply(A,B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):  #row
        for j in range(len(B[0])):  #colum
            for k in range(len(B)):
                result[i][j]+=A[i][k] * B[k][j]
    for r in result:
        print (' '.join(map(str, r)))
    return result

def read_matrix(rows):
    matrix = []
    for _ in range(rows):
        matrix.append(list(map(int, input().split())))
    return matrix

x, y = map(int, input().split())
A = read_matrix(x)

a, b = map(int, input().split())
B = read_matrix(a)

multply(A,B)