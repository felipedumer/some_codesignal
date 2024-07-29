def print_pyramid(N):
    for i in range(1, N + 1):
        # Calculate the number of spaces
        spaces = ' ' * (N - i)
        # Calculate the number of asterisks
        asterisks = '*' * (2 * i - 1)
        # Print the current level of the pyramid
        print(spaces + asterisks)

# Set N to 10
N = 10
print_pyramid(N)