n1 = int (input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao = int(input('Qual sua opção? : '))
    if opcao == 1:
        n3 = n1 + n2
        print(f'A Soma de {n1} com {n2} é {n3}')
    elif opcao == 2:
        n3 = n1 * n2
        print(f'A multiplicação de {n1} com {n2} é {n3}')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opcao == 4:
        n1 = int (input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Ok!. Volte sempre')
        StopIteration
    else:
        print('Opção Inválida. Tente novamente')
    print('=-=' * 10)

        