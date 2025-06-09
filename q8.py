def print_formatted(n):
    width = len(bin(n)[2:])
    for i in range(1, n + 1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexadecimal = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        print(f"{decimal} {octal} {hexadecimal} {binary}")

n = int(input())
print_formatted(n)