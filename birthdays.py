birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}



print('Enter a name: (blank to quit)')
name = input()

      
if name in birthdays:
      print(birthdays[name] + ' is the birthdays of ' + name)
else:
      print('I do not have birthdays information for ' + name)
      print('What is their birthdays: ')
      bday = input()
      birthdays[name] = bday
      print('Birthdays database updated.')
