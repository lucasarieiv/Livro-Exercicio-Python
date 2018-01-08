print('Whats is your name ?')
name = input()
print('Wrote your Age. ')
age = input()

if name == 'Alice':
      print('Hi Alice.')
elif int(age) < 12:
      print('You are not Alice, Kiddo.')
else:
      print('You are neither Alice nor a little kid.')
