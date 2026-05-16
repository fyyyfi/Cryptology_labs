def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, text_length):
    i = 0
    j = 0
    keystream = []
    
    for _ in range(text_length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        
        t = (S[i] + S[j]) % 256
        keystream.append(S[t])
        
    return keystream

def rc4_encrypt(key_string, text_string):
    key_bytes = [ord(c) for c in key_string]
    text_bytes = [ord(c) for c in text_string]

    S = ksa(key_bytes)
    
    keystream = prga(S, len(text_bytes))
    

    cipher_bytes = []
    for n in range(len(text_bytes)):
        # Оператор ^ в Python - це побітовий XOR
        cipher_bytes.append(text_bytes[n] ^ keystream[n])
        
    keystream_hex = ''.join(f'{b:02X}' for b in keystream)
    cipher_hex = ''.join(f'{b:02X}' for b in cipher_bytes)
    
    return keystream_hex, cipher_hex

# --- Інтерактивна частина програми ---
if __name__ == "__main__":
    print("Програма для шифрування алгоритмом RC4")
    
    # Отримуємо значення від користувача
    key = input("Введіть ключ шифрування: ").strip()
    plaintext = input("Введіть текст для шифрування: ").strip()
    
    if not key or not plaintext:
        print("Помилка: Ключ та текст не можуть бути порожніми.")
    else:
        # Обчислення
        ks_hex, c_hex = rc4_encrypt(key, plaintext)
        
        print("\n-Результати")
        print(f"Відкритий текст: {plaintext}")
        print(f"Ключ:            {key}")
        print(f"Потік ключів:    {ks_hex}")
        print(f"Шифротекст:      {c_hex}")
        
        # RC4 - симетричний алгоритм. Якщо текст зашифрувати тим самим ключем ще раз, 
        # ми отримаємо вихідний текст.