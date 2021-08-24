def table(length, height):
    for i in range(height + 1):
        row = []
        for j in range(length + 1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(i * j)
        print('\t'.join([str(i) for i in row]))


table(10, 10)