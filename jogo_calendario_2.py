from math import remainder

#LEGENDA - NÚMERO BINÁRIO#
#nbs = número binário sujo#
#nbl = número binário limpo#
#nbf = número binário final#
#nd = número decimal#

lista_binario = []
numero1 = 0
while numero1 < 32:
    nbs = bin(numero1)
    nbl = nbs.lstrip('0b')
    nbf = nbl.zfill(5)
    lista_binario.append(nbf)
    numero1 +=1


print('************************************')
print('**Bem vindo ao jogo do Calendário!**')
print('************************************')

nome_cadastro = input('Olá, tudo bom? Qual é o seu nome?')

print('Agora responda sobre o dia do do mês que você nasceu, ele esta na lista abaixo?')

lista1 = []
for x in lista_binario:
    if (x[4:5] == "1"):
        nd1 = int(x[:1]) * 16 + int(x[1:2]) * 8 + int(x[2:3]) * 4 + int(x[3:4]) * 2 + int(x[4:5]) * 1
        lista1.append(nd1)

print(lista1)

resposta0 = input('Sim(S) ou Não(N)').upper()

if resposta0 == 'S':
    r0 = 1
else:
    r0 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista2 = []
for x in lista_binario:
    if (x[3:4] == "1"):
        nd2 = int(x[:1]) * 16 + int(x[1:2]) * 8 + int(x[2:3]) * 4 + int(x[3:4]) * 2 + int(x[4:5]) * 1
        lista2.append(nd2)

print(lista2)

resposta1 = input('Sim(S) ou Não(N)').upper()

if resposta1 == 'S':
    r1 = 1
else:
    r1 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista3 = []
for x in lista_binario:
    if (x[2:3] == "1"):
        nd3 = int(x[:1]) * 16 + int(x[1:2]) * 8 + int(x[2:3]) * 4 + int(x[3:4]) * 2 + int(x[4:5]) * 1
        lista3.append(nd3)

print(lista3)

resposta2 = input('Sim(S) ou Não(N)').upper()

if resposta2 == 'S':
    r2 = 1
else:
    r2 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista4 = []
for x in lista_binario:
    if (x[1:2] == "1"):
        nd4 = int(x[:1]) * 16 + int(x[1:2]) * 8 + int(x[2:3]) * 4 + int(x[3:4]) * 2 + int(x[4:5]) * 1
        lista4.append(nd4)

print(lista4)

resposta3 = input('Sim(S) ou Não(N)').upper()

if resposta3 == 'S':
    r3 = 1
else:
    r3 = 0

print('E nessa lista, o dia que você nasceu aparece?')

lista5 = []
for x in lista_binario:
    if (x[:1] == "1"):
        nd5 = int(x[:1]) * 16 + int(x[1:2]) * 8 + int(x[2:3]) * 4 + int(x[3:4]) * 2 + int(x[4:5]) * 1
        lista5.append(nd5)

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