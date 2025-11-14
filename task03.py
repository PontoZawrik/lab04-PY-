msg = input("Введите строку: ")
msg = msg.lstrip()

count = 0

for i in range(len(msg)):
    if msg[i] == "o":
        count += 1

    if msg[i] == " ":
        break

print("'o' = {0}".format(count))