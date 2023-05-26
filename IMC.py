import os

print('Calculo IMC')

def calculo_imc():
    os.system('cls')
    while True: # Variavel altura - Valida os dados que entram
        try:
            altura_str = input('Informe sua altura: ')
            if '.' in altura_str:  # Verifica se a altura já possui ponto decimal
                altura = float(altura_str)
            else:
                altura = float(altura_str) / 100  # Converte altura em centímetros para metros
            break
        except ValueError:
            print('Valor inválido. Tente novamente.')
              
    while True:
        try:
            peso = float(input('Informe sua peso: '))
            break
        except ValueError:
            print('Valor inválido. Digite um valor válido.')

    while True: # Variavel do sexo - Validando as informações necessárias
        sexo = input('Informe seu sexo: M - Masculino / F - Feminino: ')
        if sexo.upper().strip() in ['M', 'F']:
            break
        else:
            print('Valor inválido!')

    if sexo.upper().strip() == 'M': # Continuidade da validação anterior
        sexo_certo = 'MASCULINO'
    else:
        sexo_certo = 'FEMININO'
    imc = peso / altura**2

    if imc < 18.5:  # IF da Regra IMC
        os.system('cls')
        print('Pessoa do sexo: {}'.format(sexo_certo))
        print('O IMC é: {:.2f}, está na faixa de MAGREZA'.format(imc))
    elif imc >= 18.5 and imc <= 24.9:
        os.system('cls')
        print('Pessoa do sexo: {}'.format(sexo_certo))
        print('O IMC é: {:.2f}, está dentro da faixa NORMAL'.format(imc))
    elif imc >= 25 and imc <= 29.9:
        os.system('cls')
        print('Pessoa do sexo: {}'.format(sexo_certo))
        print('O IMC é: {:.2f}, está na faixa do SOBREPESO'.format(imc))
    elif imc >= 30 and imc <= 39.9:
        os.system('cls')
        print('Pessoa do sexo: {}'.format(sexo_certo))
        print('O IMC é: {:.2f}, está na faixa do OBESIDADE'.format(imc))
    else:
        os.system('cls')
        print('Pessoa do sexo: {}'.format(sexo_certo))
        print('O IMC é: {:.2f}, está na faixa do OBESIDADE GRAVE'.format(imc))
        
    again()
        
def again():
    import os   # import para a usar o cls / Limpar a tela
    calcular_denovo = input("\nQuer calcular novamente: [S] Sim ou [N] Não: \n")
    if calcular_denovo.upper().strip()[0] == "S":
        os.system('cls')    # Usado no import
        calculo_imc()
    elif calcular_denovo.upper().strip()[0] == "N":
        os.system('cls')
        print("\nEncerrando...")
    else:
        print('Valor invalido!')
        again()        

calculo_imc()
