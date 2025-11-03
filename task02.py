msg = input("Введите строку: ")

countStar = 0
countPlus = 0

for i in range(len(msg)):
    if msg[i] == "*":
        countStar += 1

    if msg[i] == "+":
        countPlus += 1

print("'*' = {0} \n'+' = {1}".format(countStar, countPlus))