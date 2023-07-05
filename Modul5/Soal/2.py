def gabungkanArray(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while j < len(B):
        C.append(B[j])
        j += 1
    return C

A = [1, 4, 7, 9, 12]
B = [2, 3, 5, 8, 10, 11]
C = gabungkanArray(A, B)
print(C)