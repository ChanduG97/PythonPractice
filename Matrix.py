def create_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i},{j}]: ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(num) for num in row))

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = create_matrix(rows, cols)
    print("Matrix:")
    print_matrix(matrix)

if __name__ == "__main__":
    main()