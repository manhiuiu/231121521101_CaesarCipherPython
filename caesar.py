def caesar_encrypt(text, k):
    result = ""
    k %= 26  # chuẩn hóa k về 0..25
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result


if __name__ == "__main__":
    plaintext = "PhanNhatMinhAnh"
    k = 17
    ciphertext = caesar_encrypt(plaintext, k)
    print(f"Plaintext : {plaintext}")
    print(f"Ciphertext: {ciphertext}")
