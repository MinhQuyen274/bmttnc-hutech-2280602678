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
        num_of_columns = key
        num_of_rows = len(text) // key
        if len(text) % key != 0:
            num_of_rows += 1

        num_of_shaded_boxes = (num_of_columns * num_of_rows) - len(text)

        plaintext = [''] * num_of_rows
        col = 0
        row = 0

        for char in text:
            plaintext[row] += char
            row += 1

            if (row == num_of_rows) or (row == num_of_rows - 1 and col >= num_of_columns - num_of_shaded_boxes):
                row = 0
                col += 1

        return ''.join(plaintext)
