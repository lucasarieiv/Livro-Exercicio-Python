# passwordFile = open('SecretPasswordFile.txt')
# PassWord = passwordFile.read()
# print('Enter Your Password')
# typedPassword = input()
#
# if typedPassword == PassWord:
#     print('Access Granted')
#     if typedPassword == '12345':
#         print('Sua Senha é Uma Merda')
# else:
#     print('Access Danied')
i = 0
while i == 0:
    for i in range(1, 10):
        print('>' * i)
    for i in range(10, -1, -1):
        print('>' * i)
