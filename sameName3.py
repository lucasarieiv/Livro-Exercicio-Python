Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170118] on linux
Type "copyright", "credits" or "license()" for more information.
>>> spam - =
SyntaxError: invalid syntax
>>> def spam():
	eggs = 3111

	
>>> spam()
>>> print(eggs)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(eggs)
NameError: name 'eggs' is not defined
>>> 
========== RESTART: /home/bumblebee/Projetos_Python/Livro/teste.py ==========
99
>>> 
========== RESTART: /home/bumblebee/Projetos_Python/Livro/teste.py ==========
0
99
>>> 
========== RESTART: /home/bumblebee/Projetos_Python/Livro/teste.py ==========
42
42
>>> 
========= RESTART: /home/bumblebee/Projetos_Python/Livro/sameName.py =========
Bacon local
spam local
Bacon local
>>> print(eggs)
global
>>> 
======== RESTART: /home/bumblebee/Projetos_Python/Livro/sameName2.py ========
spam
>>> 
