def get_user_input():
    try:
        n = int(input("Enter the value of n: "))
        if n <= 0:
            raise ValueError
        return n
    except ValueError:
        print("Invalid input! Please enter a positive integer.")
        return None


def print_pyramid(n):
    for i in range(1, n + 1):

        # Print leading spaces
        for space in range(n - i):
            print(" ", end="")

        # Print increasing numbers
        for num in range(1, i + 1):
            print(num, end="")

        # Print decreasing numbers
        for num in range(i - 1, 0, -1):
            print(num, end="")

        print()  # Move to next line


def main():
    n = get_user_input()
    if n is not None:
        print_pyramid(n)


if __name__ == "__main__":
    main()