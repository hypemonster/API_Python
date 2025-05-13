Ph3 = input("Coloque um dos simbolo de operação + - * / = : ")


if Ph3 == "+":
    Ph = int(input("Coloque o primeiro valor: "))
    Ph2 = int(input("Coloque o segundo valor: "))
    print(Ph + Ph2)

elif Ph3 == "-":
    Ph = int(input("Coloque o primeiro valor: "))
    Ph2 = int(input("Coloque o segundo valor: "))
    print(Ph - Ph2)

elif Ph3 == "*":
    Ph = int(input("Coloque o primeiro valor: "))
    Ph2 = int(input("Coloque o segundo valor: "))
    print(Ph * Ph2)

elif Ph3 == "/":
    Ph = int(input("Coloque o primeiro valor: "))
    Ph2 = int(input("Coloque o segundo valor: "))
    print(Ph / Ph2)

else:
    Ph3 == "="
    Ph = int(input("Coloque o primeiro valor: "))
    Ph2 = int(input("Coloque o segundo valor: "))
    if Ph > Ph2:
        print(f'{Ph} é maior que {Ph2}')
    else:
        print(f'{Ph} é menor que {Ph2}')




