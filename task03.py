msg = input("Введите строку: ")
msg = msg.lstrip()

count = 0
i = 0
while i < len(msg):
    if msg[i] == "o":
        count += 1

    if msg[i] == " ":
        break

    i += 1

print("'o' = {0}".format(count))