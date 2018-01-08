def spam():
      global eggs
      eggs = 'Spam' #essa é a variável global


def bacon():
      eggs = 'Bacon' #essa é uma variável local


def ham():
      print(eggs) #essa é a variável global

eggs = 42
spam()
bacon()
print(eggs)
