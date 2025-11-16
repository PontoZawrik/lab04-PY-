msg = list(input("Введите строку: "))

countStar = 0
countPlus = 0

for i in msg:
    if i == "*":
        countStar += 1

    if i == "+":
        countPlus += 1

print("'*' = {0} \n'+' = {1}".format(countStar, countPlus))