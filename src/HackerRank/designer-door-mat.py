def print_welcome_mat(n, m):
    for i in range(1, n, 2):
        print((".|." * i).center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n - 2, 0, -2):
        print((".|." * i).center(m, "-"))


if __name__ == "__main__":
    n, m = map(int, input().split())
    print_welcome_mat(n, m)
