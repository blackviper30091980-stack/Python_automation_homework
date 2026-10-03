 # task 01 == Виправте синтаксичні помилки
print("Hello","World")
print("World")

# task 02 == Виправте синтаксичні помилки
hello = "hello"
world = "world"
if True:
    print(f"{hello}, {world}!")


# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello,World!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
side_1 = 1
side_2 = 2
side_3 = 3
side_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = 1 + 2 + 3 + 4
print(perimeter)


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print(total_trees)

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temperature = +5
afternoon_temperature = morning_temperature - 10
evening_temperature = afternoon_temperature + 4
print(evening_temperature)
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
total_boys = 24
total_girls = total_boys//2
present_boys = total_boys - 1
present_girls = total_girls - 2
present_children = present_boys + present_girls
print(present_children)


# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
book1_price = 8
book2_price = book1_price + 2
book3_price = (book1_price + book2_price)//2
total_price = book1_price + book2_price + book3_price
print(total_price)