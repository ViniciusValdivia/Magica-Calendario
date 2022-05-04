from math import remainder

print('************************************')
print('**Bem vindo ao jogo do Calendário!**')
print('************************************')

nome_cadastro = input('Olá, tudo bom? Qual é o seu nome?')

print('Agora responda sobre o dia do do mês que você nasceu, ele esta na lista abaixo?')

lista1 = []
numero1 = 1
while numero1 < 32:
    resto1 = remainder(numero1,2)
    if resto1 != 0:
        lista1.append(numero1)
    numero1 +=1
print(lista1)

resposta0 = input('Sim(S) ou Não(N)').upper()

if resposta0 == 'S':
    r0 = 1
else:
    r0 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista2 = []
numero2 = 1
while numero2 < 32:
    resto2 = remainder(numero2,4)
    if resto2 != 0 and resto2 != 1:
        lista2.append(numero2)
    numero2 +=1
print(lista2)

resposta1 = input('Sim(S) ou Não(N)').upper()

if resposta1 == 'S':
    r1 = 1
else:
    r1 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista3 = []
numero3 = 1
while numero3 < 32:
    resto3 = remainder(numero3,8)
    if resto3 != 0 and resto3 != 1 and resto3 != 2 and resto3 != 3:
        lista3.append(numero3)
    numero3 +=1
print(lista3)

resposta2 = input('Sim(S) ou Não(N)').upper()

if resposta2 == 'S':
    r2 = 1
else:
    r2 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista4 = []
numero4 = 1
while numero4 < 32:
    resto4 = remainder(numero4,16)
    if resto4 != 0 and resto4 != 1 and resto4 != 2 and resto4 != 3 and resto4 != 4 and resto4 != 5 and resto4 != 6 and resto4 != 7:
        lista4.append(numero4)
    numero4 +=1
print(lista4)

resposta3 = input('Sim(S) ou Não(N)').upper()

if resposta3 == 'S':
    r3 = 1
else:
    r3 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista5 = []
numero5 = 1
while numero5 < 32:
    resto5 = remainder(numero5,32)
    if resto5 != 0 and resto5 != 1 and resto5 != 2 and resto5 != 3 and resto5 != 4 and resto5 != 5 and resto5 != 6 and resto5 != 7 and resto5 != 8 and resto5 != 9 and resto5 != 10 and resto5 != 11 and resto5 != 12 and resto5 != 13 and resto5 != 14 and resto5 != 15:
        lista5.append(numero5)
    numero5 +=1
print(lista5)

resposta4 = input('Sim(S) ou Não(N)').upper()

if resposta4 == 'S':
    r4 = 1
else:
    r4 = 0

dia = r0 * 1 + r1 * 2 + r2 * 4 + r3 * 8 + r4 * 16

print('E mesmo se você não acredite em signos, você pode dizer qual é o seu signo?')

signo = int(input("(1)Áries, (2)Touro, (3)Gêmeos, (4)Câncer, (5)Leão, (6)Virgem, "
              "(7)Libra, (8)Escorpião, (9)Sagitário,(10)Capricórnio, (11)Aquário, (12)Peixes"))

if(signo == 1):
    if dia <= 19:
        mes = 'Abril'
    else:
        mes = 'Março'
elif(signo == 2):
    if dia <= 20:
        mes = 'Maio'
    else:
        mes = 'Abril'
elif(signo == 3):
    if dia <= 21:
        mes = 'Junho'
    else:
        mes = 'Maio'
elif(signo == 4):
    if dia <= 22:
        mes = 'Julho'
    else:
        mes = 'Junho'
elif(signo == 5):
    if dia <= 22:
        mes = 'Agosto'
    else:
        mes = 'Julho'
elif(signo == 6):
    if dia <= 22:
        mes = 'Setembro'
    else:
        mes = 'Agosto'
elif(signo == 7):
    if dia <= 22:
        mes = 'Outubro'
    else:
        mes = 'Setembro'
elif(signo == 8):
    if dia <= 21:
        mes = 'Novembro'
    else:
        mes = 'Outubro'
elif(signo == 9):
    if dia <= 21:
        mes = 'Dezembro'
    else:
        mes = 'Novembro'
elif(signo == 10):
    if dia <= 19:
        mes = 'Janeiro'
    else:
        mes = 'Dezembro'
elif(signo == 11):
    if dia <= 18:
        mes = 'Fevereiro'
    else:
        mes = 'Janeiro'
elif(signo == 12):
    if dia <= 20:
        mes = 'Março'
    else:
        mes = 'Fevereiro'
else:
    mes = 'Não nasceu'



print('Então , {} você faz aniversário {} de {}'.format(nome_cadastro, dia, mes))