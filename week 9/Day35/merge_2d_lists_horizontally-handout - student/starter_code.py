def merge2DList(matrix1, matrix2):
    final_matrix = []

    for r1, r2 in zip(matrix1, matrix2):
        merged_row = r1 + r2
        final_matrix.append(merged_row)

    return final_matrix


l1 = eval(input())
l2 = eval(input())

print(merge2DList(l1, l2))
