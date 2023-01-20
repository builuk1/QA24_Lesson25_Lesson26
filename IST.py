'''Если псевдо-код ниже был бы языком программирования,
сколько тестов требуется для достижения 100% покрытия операторов?
1. If x=3 then
2. Display_messageX;
3. If y=2 then
4. Display_messageY;
5. Else
6. Display_messageZ;
7. Else
8. Display_messageZ;'''

x = 20
y = 15
if x == 3:
    print("Display_messageX")
    if y == 2:
        print("Display_messageY")
else:
    print("Display_messageZ")


def ist(x, y):
    if x == 3:
        # Порядок важен, так как return прерывает выполнение функции
        if y == 2:
            return ("Display_messageY")

        return ("Display_messageX")
    else:
        return ("Display_messageZ")
