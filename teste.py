import random


words = random.randint(1, 5)

word1 = 'Cachorro'
word2 = 'Cabra'
word3 = 'Cobra'
word4 = 'Leão'
word5 = 'Zebra'

if words == 1:
      print(' _ ' * len(word1))
      print(len(word1))
      print(word1)
elif words == 2:
      print(' _ ' * len(word2))
      print(len(word2))
      print(word2)
elif words == 3:
      print(' _ ' * len(word3))
      print(len(word3))
      print(word3)
elif words == 4:
      print(' _ ' * len(word4))
      print(len(word4))
      print(word4)
elif words == 5:
      print(' _ ' * len(word5))
      print(len(word5))
      print(word5)

