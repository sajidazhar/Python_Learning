string = input("enter the string : ")
i = 0
temp = ""
while i < len(string):
    if string[i] not in temp:
        temp += string[i]
        print(f"{string[i]} : {string.count(string[i])}")
    i += 1
