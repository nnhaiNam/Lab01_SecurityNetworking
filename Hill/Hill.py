import numpy as np
from sympy import Matrix

# Chuyển đổi ký tự thành số nguyên
def char_to_num(c):
    return ord(c) - ord('A')

# Chuyển đổi số nguyên thành ký tự
def num_to_char(n):
    return chr(int(n) + ord('A'))

# Mã hóa văn bản với ma trận khóa
def hill_encrypt(plain_text, key):
    plain_text = plain_text.upper().replace(" ", "")
    if len(plain_text) % 2 != 0:
        plain_text += 'X'  # Padding nếu độ dài không chia hết cho 2

    cipher_text = ""
    for i in range(0, len(plain_text), 2):
        pair = [char_to_num(plain_text[i]), char_to_num(plain_text[i + 1])]
        result = np.dot(key, pair) % 26
        cipher_text += num_to_char(result[0]) + num_to_char(result[1])

    return cipher_text

# Giải mã văn bản với ma trận khóa
def hill_decrypt(cipher_text, key):
    cipher_text = cipher_text.upper().replace(" ", "")
    det = int(np.round(np.linalg.det(key))) % 26
    det_inv = pow(det, -1, 26)
    key_inv = Matrix(key).inv_mod(26)
    key_inv = np.array(key_inv).astype(int) % 26

    plain_text = ""
    for i in range(0, len(cipher_text), 2):
        pair = [char_to_num(cipher_text[i]), char_to_num(cipher_text[i + 1])]
        result = np.dot(key_inv, pair) % 26
        plain_text += num_to_char(result[0]) + num_to_char(result[1])

    return plain_text

# Nhập ma trận khóa từ bàn phím
key = []
print("Nhập ma trận khóa 2x2:")
for i in range(2):
    row = list(map(int, input(f"Hàng {i + 1}: ").split()))
    key.append(row)
key = np.array(key)

# Kiểm tra tính khả nghịch của ma trận khóa
det = int(np.round(np.linalg.det(key))) % 26
if np.gcd(det, 26) != 1:
    print("Ma trận khóa không khả nghịch. Vui lòng nhập ma trận khác.")
else:
    # Nhập văn bản từ bàn phím
    plain_text = input("Nhập văn bản để mã hóa: ")

    # Mã hóa văn bản
    cipher_text = hill_encrypt(plain_text, key)
    print(f"Ciphertext: {cipher_text}")

    # Giải mã văn bản
    decrypted_text = hill_decrypt(cipher_text, key)
    print(f"Decrypted text: {decrypted_text}")