def caesar_cipher(text, shift, encode=True):
    result = []
    shift = shift % 26
    if not encode:
        shift = -shift
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

# Example usage
encoded = caesar_cipher("Hello World!", 3)
decoded = caesar_cipher(encoded, 3, encode=False)
