# Задание "Слишком древний шифр":
# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки) с двумя каменными вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
#
# К вашему счастью рядом с менее успешными и уже неговорящими путешественниками находился папирус, где были написаны правила для решения этого "ребуса".
# (Как жаль, что они поняли это так поздно :( ).
#
# Во вторую вставку нужно было написать те пары чисел друг за другом, чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.





import time
from random import randint
a = 'Получение шифра...'
print(a)
time.sleep(3)
stone_1 = randint(3, 20)
print(stone_1)
time.sleep(1)
b = 'Получение ключа...'
print(b)
time.sleep(3)


def create_pairs():
    pairs = ''
    for i in range(1, stone_1):
        for j in range(i + 1, stone_1 + 1):
            if stone_1 % (i + j) == 0:
                pairs += str(i) + str(j)

    return pairs


pairs = create_pairs()
print(f"Ключ для числа {stone_1}: {pairs}")



