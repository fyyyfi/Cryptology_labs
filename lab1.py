def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    return tmp

def calculate_crc(data, polynomial):
    """Основна функція обчислення CRC."""
    r = len(polynomial) - 1
    appended_data = data + '0' * r
    remainder = mod2div(appended_data, polynomial)
    return remainder


if __name__ == "__main__":
    print("=== Програма для обчислення CRC ===")
    
    # Отримуємо значення від користувача
    M = input("Введіть повідомлення (в двійковому форматі, наприклад 110101): ").strip()
    G = input("Введіть поліном-генератор (в двійковому форматі, наприклад 1011): ").strip()
    
    # Перевірка, чи введено саме двійкові числа
    if not (set(M).issubset({'0', '1'}) and set(G).issubset({'0', '1'})):
        print("\nПомилка: Повідомлення та поліном-генератор повинні містити ЛИШЕ символи '0' та '1'.")
    elif len(G) <= 1:
        print("\nПомилка: Довжина полінома-генератора має бути більше 1 біта.")
    else:
        # Обчислення та виведення результатів
        print("\n--- Результати ---")
        print(f"Вхідне повідомлення: {M}")
        print(f"Поліном-генератор:   {G}")
        
        crc = calculate_crc(M, G)
        print(f"Обчислена контрольна сума (CRC): {crc}")
        
        transmitted_message = M + crc
        print(f"Закодоване повідомлення для передачі: {transmitted_message}")