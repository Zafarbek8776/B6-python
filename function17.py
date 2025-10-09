def table(n):
    def show_row(i):
        print(f"{n} x {i} = {n * i}")

    for i in range(1, 11):
        show_row(i)

table(7)
