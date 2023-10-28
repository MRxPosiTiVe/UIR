import re


def matrix_generate(matrix_dimension):
    matrix = [[0 for _ in range(2 * matrix_dimension)] for _ in range(2 * matrix_dimension)]
    value = 1

    # Заполняем первую матрицу
    for j in range(matrix_dimension, 0, -1):
        
        # Заполнение верхней строки слева направо
        for i in range(matrix_dimension - j, j):
            matrix[matrix_dimension - j][i] = value
            value += 1

        # Заполнение правого столбца свержу вниз
        for i in range(matrix_dimension - j + 1, j):
            matrix[i][j - 1] = value
            value += 1

        # Заполнение левого столбца сверху вниз
        for i in range(matrix_dimension - j + 1, j):
            matrix[i][matrix_dimension - j] = value
            value += 1

        # Заполнение нижней строки слева направо
        for i in range(matrix_dimension - j + 2, j):
            matrix[j - 1][i - 1] = value
            value += 1

    value = 1

    # Заполняем вторую матрицу
    for j in range(matrix_dimension, 0, -1):

        # Заполнение верхней строки слева направо
        for i in range(2 * matrix_dimension - j, matrix_dimension + j):
            matrix[2 * matrix_dimension - j][i] = value
            value += 1

        # Заполнение правого столбца свержу вниз
        for i in range(2 * matrix_dimension - j + 1, matrix_dimension + j):
            matrix[i][matrix_dimension + j - 1] = value
            value += 1

        # Заполнение левого столбца сверху вниз
        for i in range(2 * matrix_dimension - j + 1, matrix_dimension + j):
            matrix[i][2 * matrix_dimension - j] = value
            value += 1

        # Заполнение нижней строки слева направо
        for i in range(2 * matrix_dimension - j + 2, matrix_dimension + j):
            matrix[matrix_dimension + j - 1][i - 1] = value
            value += 1

    for row in matrix:
        for cell in row:
            print(f"{cell:3}", end=" ")
        print()


n = input("Введите размерность матрицы NxN: ")

while not re.match(r'^[1-9]\d*$', n):
    n = input("Введите размерность матрицы NxN (где N это целочисленное значение (1, 2, 3 и тд)): ")

matrix_generate(int(n))
