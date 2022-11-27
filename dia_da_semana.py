# por: Lisandra Sapucaia Gumes
# em: 27/11/2022

# Programa para calcular qual dia da semana
# corresponde a determinada data.


def calcula(d, m, a):
    
    # definir valores pra caso o mes seja janeiro ou fevereiro
    if (m == 1):
        m = 13
        a = a - 1
    elif (m == 2):
        m = 14
        a = a - 1

    # calculo
    # d + 2m + [3(m+1)]/5 + a + a/4 - a/100 + a/400 + 2

    parcial = d + 2*m + (3*(m + 1))//5 + a + a//4 - a//100 + a//400 + 2
    # print(parcial)
    final = parcial % 7
    # print(final)

    # corrige o mes e ano para imprimir se for o caso
    if (m == 13):
        m = 1
        a = a + 1
    elif (m == 14):
        m = 2
        a = a + 1

    # determina o dia da semana por meio do resultado final
    if (final == 0): # sabado
        print(f"\nA data {d}/{m:0>2}/{a} é um sábado.")
        
    elif(final == 1): # domingo
        print(f"\nA data {d}/{m:0>2}/{a} é um domingo.")

    elif(final == 2): # segunda
        print(f"\nA data {d}/{m:0>2}/{a} é uma segunda-feira.")
    
    elif(final == 3): # terça
        print(f"\nA data {d}/{m:0>2}/{a} é uma terça-feira.")

    elif(final == 4): # quarta
        print(f"\nA data {d}/{m:0>2}/{a} é uma quarta-feira.")
    
    elif(final == 5): # quinta
        print(f"\nA data {d}/{m:0>2}/{a} é uma quinta-feira.")
    
    else: # sexta
        print(f"\nA data {d}/{m:0>2}/{a} é uma sexta-feira.")




dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

# checar se ano é bissexto; 0 < mês <= 31 e 0 < ano <= 12
if (((ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0)) and (dia > 0 and dia <= 31) and (mes > 0 and mes <= 12)):

    # checa se os meses tem a qtd correta de dias (fev tem 29)
    if ((mes == 2 and dia > 29) or (mes == 4 and dia > 30) or (mes == 6 and dia > 30) or (mes == 9 and dia > 30) or (mes == 11 and dia > 30)):
        print(f"\nA data {dia}/{mes:0>2}/{ano} não existe no calendário Gregoriano!")
        
    else:
        calcula(dia, mes, ano)

# checa se o ano NÃO é bissexto; 0 < mes < 31 e 0 < ano <= 12 
elif ( not((ano % 4 == 0 and ano % 100 != 0) or (ano % 4 == 0 and ano % 100 == 0 and ano % 400 == 0)) and (dia > 0 and dia <= 31) and (mes > 0 and mes <= 12)):
    # checa se os meses tem a qtd correta de dias (fev tem 28)
    if ((mes == 2 and dia > 28) or (mes == 4 and dia > 30) or (mes == 6 and dia > 30) or (mes == 9 and dia > 30) or (mes == 11 and dia > 30)):
        print(f"\nA data {dia}/{mes:0>2}/{ano} não existe no calendário Gregoriano!")
    else:
        calcula(dia, mes, ano)

# se o programa não entrar nos laços, a data esta errada
else:
    print(f"\nA data {dia}/{mes:0>2}/{ano} não existe no calendário Gregoriano!")
    

