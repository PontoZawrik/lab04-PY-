msg = list(input("Введите строку: "))

while True:
    n1, n2 = input().split()
    n1, n2 = int(n1) - 1, int(n2) - 1
    if 0 <= n1 < len(msg) and 0 <= n2 < len(msg):
        break

if n1 > n2:
    n1 += n2
    n2 = n1 - n2
    n1 = n1 - n2

del msg[n1:n2]
msg = "".join(msg)

print(msg)