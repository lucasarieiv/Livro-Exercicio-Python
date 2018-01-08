def spam():
      global eggs
      print(eggs)
      eggs = 'spam local'
      print(eggs)

eggs = 'global'
spam()
