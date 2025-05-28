class TranspositionCipher:
    def __init__(self):
        pass
    def encrypt(self, text, key):
        encrypted_text = ''
        for  col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text
    def decrypt(self, text, key):
        decrypted_text = [''] * key
        row, col = 0, 0
        for char in text:
            decrypted_text[col] += char
            col += 1
            if col == key or row * key + col >= len(text):
                col = 0
                row += 1
        return ''.join(decrypted_text)