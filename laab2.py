from csv import reader
import xml.dom.minidom as minidom

#Блок1 Вывод строк с Названием больше 30 символов
cnt = 0
with open("books-en.csv", "r") as csvfile:
    table = reader(csvfile, delimiter=";")
    for row in table:
        if len(row[1]) > 30:
            cnt += 1
print(cnt)


#Блок2 Поиск книги по автору
while True:
    flag = 0
    search = input("Введите Автора")

        

    if search == "0":
        break
    with open("books-en.csv", "r") as csvfile:
        table = reader(csvfile, delimiter=";")
        for row in table:
            index = row[2].find(search)
            if (index != -1) and (1991 <= int(row[3]) < 1995):
                print(f"Name: {row[1]}, Year: {row[3]}")
                flag = 1

    if flag == 0:
        print("ничего не найдено, или нет книг нужного года")

#Блок3 Генератор билеографических ссылок


output = open('res.txt', "w")
csvF = open("books-en.csv", "r")
table = reader(csvF, delimiter=";")
lt_tb = list(table)

cnt = 1
print
for i in range(1, len(lt_tb), 9):
    row = lt_tb[i]
    zap = f"{row[2]}. {row[1]} - {row[3]}"
    output.write(f"{cnt}. {zap}\n")
    cnt +=1
    if cnt == 21:
        break
output.close()
csvF.close()

#Блок4 Из xml сделать нужный список

xmlF = open("currency.xml", "r")
data = xmlF.read()
dom = minidom.parseString(data)

el = dom.getElementsByTagName("Valute")
char = ""
flag = False
spisok = []
for node in el:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == "Nominal":
                if child.firstChild.nodeType == 3:
                    if child.firstChild.data == "10" or child.firstChild.data == "100":
                        flag = True
            if child.tagName == "CharCode":
                if child.firstChild.nodeType == 3:
                    char = child.firstChild.data
            if flag:
                spisok.append(char)
                flag = False

print(list(set(spisok)))

#Доп Задание
output = open('res.txt', "w")
csvF = open("books-en.csv", "r")
table = reader(csvF, delimiter=";")
lt_tb = list(table)
lt_tb.pop(0)
rate = {}
izdat = set() #все издательства без повторений

for row in lt_tb:
    
    rate[row[1]] = int(row[-2])
    
    izdat.add(row[-3])
rate = dict(sorted(rate.items(), key=lambda item: item[1]))
print(izdat)
print(list(rate.keys())[-20:]) #20 самых популярных книг