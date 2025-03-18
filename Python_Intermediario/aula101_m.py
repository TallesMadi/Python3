def reverse_word(word):
    word_reversed = ''
    for i in range(len(word), 0, -1):
        word_reversed += word[i - 1]
    return word_reversed.lower()

nome = 'Talles'

print('Este módulo se chama', __name__)
