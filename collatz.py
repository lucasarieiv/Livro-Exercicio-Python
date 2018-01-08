def collatz(number):
      if number % 2 == 0:
            v1 = number // 2
            print(v1)
            return v1
      elif number % 2 == 1:
            v2 = 3 * number + 1
            print(v2)
            return v2

print('Enter number. ')
num = input()

try:
      collatz(int(num))
except ValueError:
      print('Enter an Integer Value ')

