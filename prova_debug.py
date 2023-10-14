def print_multiplication_table(m):
    for i in range(1,11):
        x = i*m
        print(i, 'x', m, '=', x)


for z in range(1, 4):
    print(f"The multiplication table of {z}:, \n")
    print_multiplication_table(z)
    print('')