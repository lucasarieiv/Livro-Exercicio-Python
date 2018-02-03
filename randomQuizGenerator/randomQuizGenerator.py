#! python3
# randomQuizGenerato.py - Cria provas com perguntas e respostas em
# ordem aleatória, juntamente com os gabaritos contendo as respostas.


import random

# Os dados para as provas. As chaves são os estados e os valores sãos as capitais.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia':
'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield',
'Idiana': 'Idianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky':
'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Anapolis'}

#Gera 20 arquivos contendo provas.
for quizNum in range(len(capitals)):
    #Cria arquivos com as provas e os gabaritos das repostas.
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt' % (quizNum + 1), 'w')

    #Escrevendo o cabeçalho da prova.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quizFile.write('\n\n')

    # Embaralha a ordem dos estados.
    states = list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(20):
        # Obtém repostas corretas e incorretas.
        correctAnwser = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnwser)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnwser]
        random.shuffle(answerOptions)

        quizFile.write('%s. What is the capital of %s\n' % (questionNum + 1,
            states[questionNum]))
        for i in range(4):
            quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        #Grava o gabarito com as respostas em um arquivo
        answerKeyFile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[
            answerOptions.index(correctAnwser)]))
    quizFile.close()
    answerKeyFile.close()
