def print_asterisk_pattern(n):
    asterisks = 0
    reverse_pattern = n
    for i in range(n):
        asterisks += 1
        print("*" * asterisks)
        if i == n:
            break
    for j in range(n):
        reverse_pattern -= 1
        print("*" * reverse_pattern)


print_asterisk_pattern(4)
