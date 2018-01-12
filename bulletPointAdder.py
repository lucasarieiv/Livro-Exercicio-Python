#! python3
# bulletPointAdder.py - Acrescenta marcadores da Wikipedia no início
# de cada linha do texto do clipboard

import pyperclip
text = pyperclip.paste()

# Separa as linha e acrescenta asteristicos.
lines = text.split('\n')
for i in range(len(lines)): # Percorre todos os índices da lista "Lines" em um loop
    lines[i] = '* ' + lines[i] #Acrescenta um asteristico em cada string da lista "lines"
text = '\n'.join(lines)
pyperclip.copy(text)
print(pyperclip.paste())
