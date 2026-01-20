# lab3,1

sum_distance(from, to)
• Сумма чисел от from до to включительно
• Автоперестановка если from > to
• Работает с отрицательными числами

Примеры:
sum_distance(3, 7)    → 25 (3+4+5+6+7)
sum_distance(10, 5)   → 45
sum_distance(-2, 1)   → -2


# lab 3,2

trim_and_repeat(text, offset=0, reps=1)
• Обрезает строку слева + повторяет
• offset=0, reps=1 по умолчанию

Примеры:
trim_and_repeat("Hello", 3)      → "lo"
trim_and_repeat("abc", 1, 3)     → "bcBCbc"
trim_and_repeat("test", 2)       → "st"
