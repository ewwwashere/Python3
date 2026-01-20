def trim_and_repeat(text: str, offset: int = 0, repetitions: int = 1) -> str:
    """
    Обрезает строку слева на offset символов и повторяет repetitions раз.
    
    Args:
        text: входная строка
        offset: количество символов для удаления слева (по умолчанию 0)
        repetitions: количество повторений (по умолчанию 1)
    
    Returns:
        результирующая строка
    """
    # Обрезаем строку слева
    trimmed = text[offset:]
    
    # Повторяем строку нужное количество раз
    result = trimmed * repetitions
    
    return result

# Тесты
print(trim_and_repeat("HelloWorld", 5))           # "World"
print(trim_and_repeat("Python", 2, 3))           # "thonthonthon"
print(trim_and_repeat("12345", 0, 2))            # "1234512345"
print(trim_and_repeat("abc", 3))                 # ""
print(trim_and_repeat("test", 1, 1))             # "est"
print(trim_and_repeat("repeat", 2, 2))           # "peatpeat"
