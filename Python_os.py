# import os
#
# os.path.join('usr', 'bin', 'spam')
# print(os.path.join('usr', 'bin', 'spam'))
# import os
#
# os.getcwd() SIGLA CWD 'CURRENT WORK DIRECTORY'PEGA DIRETÓRIO DE TRABALHO ATUAL
#
# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#     print(os.path.join('C:\\Users\\asweigart', filename))

# import os
#
# arquivos = os.listdir('C:\\Users\\Lucas\\Desktop\\Python')
#
# for arq in arquivos:
#     tam = os.path.getsize('C:\\Users\\Lucas\\Desktop\\Python\\'+arq)
#     print('Arquivo: ' + arq + '\t Tamanho Do Arquivo: ' + str(tam))


#Programa reconheçendo PenDrive

# import os

# penDriveConect = os.path.exists('E:\\')
# if penDriveConect == False:
#     print('Nenhum PenDrive Conectado')
# else:
#     print('PenDrive Conectado!')

import os

helloFile = open('C:\\Users\\Lucas\\Desktop\\Python\\hello.txt')
