
check_error = 1


def check_valid_input(square_side_length):
    if square_side_length.isnumeric() and not (int(square_side_length) % 2 == 0 or int(square_side_length) <= 0):
        return 0
    else:
        return 1


def magic_total_constant(square_side_length):
    return square_side_length * (square_side_length**2 + 1) / 2


def print_magic_square(square_side_length, magic_square_arr):
    for row in magic_square_arr:
        for element in row:

            print("| ", str(element), end=(2 * (len(str(square_side_length ** 2))) - len(str(element))) * " ")
        print(' |', '\n')


def build_magic_square(square_side_length, magic_square_arr):
    current_col = square_side_length - 1
    current_row = square_side_length // 2
    current_number = 1

    while current_number <= square_side_length ** 2:
        magic_square_arr[current_row][current_col] = current_number
        current_number = current_number + 1
        new_row = (current_row - 1) % square_side_length
        new_col = (current_col + 1) % square_side_length

        if magic_square_arr[new_row][new_col]:
            current_col = current_col - 1
        else:
            current_col = new_col
            current_row = new_row


def verify_magic_square(square_side_length, magic_square_arr):

    diagonal_sum = 0
    reverse_diagonal_sum = 0

    for diagonal_position in range(square_side_length):
        col_sum = 0
        row_sum = 0

        for row_and_col_iterator in range(square_side_length):
            row_sum = row_sum + magic_square_arr[diagonal_position][row_and_col_iterator]
            col_sum = col_sum + magic_square_arr[row_and_col_iterator][diagonal_position]
            if (row_and_col_iterator + diagonal_position) == (square_side_length - 1):
                reverse_diagonal_sum = reverse_diagonal_sum + magic_square_arr[diagonal_position][row_and_col_iterator]

        if row_sum != magic_square_constant or col_sum != magic_square_constant:
            print("The magic square is not valid.")
            return 0

        diagonal_sum = diagonal_sum + magic_square_arr[diagonal_position][diagonal_position]

    if diagonal_sum != magic_square_constant or reverse_diagonal_sum != magic_square_constant:
        print("The magic square is not valid.")
        return 0
    else:
        return 1


while check_error:

    input_number = input("Please enter the number (No chars)(odd and positive only):\n")
    check_error = check_valid_input(input_number)
    if not check_error:
        input_number = int(input_number)


magic_square = [[0 for row in range(input_number)] for col in range(input_number)]

magic_square_constant = magic_total_constant(input_number)

build_magic_square(input_number, magic_square)

print_magic_square(input_number, magic_square)

valid_magic_square = verify_magic_square(input_number, magic_square)

if valid_magic_square:
    print("correct")
