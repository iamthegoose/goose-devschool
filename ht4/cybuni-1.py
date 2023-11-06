class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encoded_text = ''
        key_index = 0
        for char in text:
            if char in self.alphabet:
                key_char = self.key[key_index % len(self.key)]
                char_index = self.alphabet.index(key_char)

                if char in self.alphabet:
                    ind = self.alphabet.index(char)
                    new_index = (ind + char_index) % len(self.alphabet)
                    encoded_char = self.alphabet[new_index]
                    encoded_text += encoded_char
                else:
                    encoded_text += char
                key_index += 1
            else:
                encoded_text += char
                key_index += 1

        return encoded_text

    def decode(self, text):
        decoded_text = ''
        key_index = 0

        for char in text:
            if char in self.alphabet:
                key_char = self.key[key_index % len(self.key)]
                char_index = self.alphabet.index(key_char)

                if char in self.alphabet:
                    ind = self.alphabet.index(char)
                    new_index = (ind - char_index) % len(self.alphabet)
                    decoded_char = self.alphabet[new_index]
                    decoded_text += decoded_char
                else:
                    decoded_text += char
                key_index += 1
            else:
                decoded_text += char
                key_index += 1

        return decoded_text