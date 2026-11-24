room = [
    ["СТОЛ", "СТУЛ", "ШКАФ"],
    ["СТУЛ", "*", "КРЕСЛО"],
]

for row in room:
    print(row)

print()
print("Сделайте ход.При ходе вы перемещаете предмет, можно только на свободную ячейку\n"
      "Предупреждение!Всё начинается с нуля так и столбы так и строички,тоесть 1 столбик это 0.")
print("Напишите кординаты предмета который вы хотите перемести\n")

row = int(input("Впишите номер строки: "))
column = int(input("Впишите номер столбца: "))

mebel = room[row][column]
print(f"Вы взяли {mebel}")
room[row][column] = "*"

for row in room:
    print(row)

print("\nНапишите куда хотите перенести предмет тоесть кординаты:")
row = int(input("Впишите номер строки: "))
column = int(input("Впишите номер столбца: "))

room[row][column] = mebel
print(f"Вы положили {mebel}")

for row in room:
    print(row)

# def print_room():
# print()
# print(|̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅ ̅)
