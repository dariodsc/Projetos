# Calculadora em Python |Dário Costa| ** Atualizada em 04/01/22 ** 

# função calculadora para que possa se repetir
# função again para criar um laço de repetição

def calculadora():
    print("Calculadora Python\n")
    print('Utilize uma das 4 operações matemáticas\n\n(Adição, Subtração, Divisão ou Multiplicação)\n')
    valor_1 = int(input("Primeiro número: "))
    valor_2 = int(input("Segundo número: "))
    calculo = input('''\nEscolha um operador:\n 
(1). Adição\n(2). Subtração\n(3). Multiplicação\n(4). Divisão\n\nInforme o operador: ''')

    # adição
    if calculo == "1":
        print(f"\nResultado: {valor_1} + {valor_2} = {valor_1 + valor_2}")
    
    # subtração
    elif calculo == "2":
        print(f"\nResultado: {valor_1} - {valor_2} = {valor_1 - valor_2}")

    # multiplicação
    elif calculo == "3":
        print(f"\nResultado: {valor_1} X {valor_2} = {valor_1 * valor_2}")
    
    # divisão
    elif calculo == "4":
        print(f"\nResultado: {valor_1} / {valor_2} = {valor_1 // valor_2}")
    else:
        print("Escolha um operador válido")

    again()
    # fim da função calculadora

def again():
    calcular_denovo = input("Quer calcular novamente: [S] Sim ou [N] Não: \n")
    if calcular_denovo.upper().strip()[0] == "S":
        calculadora()
    elif calcular_denovo.upper().strip()[0] == "N":
        print("Encerrando...")
    else:
        print('Valor invalido!')
        again()
    # fim da função again

calculadora()
# chama a função calculadora para nova execução
