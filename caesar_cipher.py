def caesar_cipher(text, key):
    """
    Encrypt text using the Caesar cipher with the given key.
    
    Args:
        text (str): The text to be encrypted.
        key (int): The encryption key.
        
    Returns:
        str: The encrypted text.
    """
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# 获取用户输入的文本和密钥
text = input("Enter the text to encrypt: ")
key = int(input("Enter the encryption key (a number between 1 and 25): "))

# 调用 caesar_cipher 函数对文本进行加密
encrypted_text = caesar_cipher(text, key)

# 打印加密后的文本
print("Encrypted text:", encrypted_text)
