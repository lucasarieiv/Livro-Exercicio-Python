def spam():
      eggs = 'spam local'
      print(eggs) #exibe 'spam local'


def bacon():
      eggs = 'Bacon local'
      print(eggs) #exibe 'Bacon local'
      spam()
      print(eggs) #exibe 'Bacon local'


eggs = 'global'
bacon()
print(eggs)
