import random
from time import sleep

nomes = ['Emerson', 'Keli', 'Thomas', 'Nicholas', 'Christopher']
email = ['emerson@email.com', 'keli@email.com', 'thomas@email.com', 'nicholas@email.com', 'christopher@email.com']
telefone = [1143527995, 5199963652, 447909138487, 1143526669, 3499965889]
cidade = ['Sao Bernado do Campo', 'Niteroi', 'Caratinga', 'Porto Alegre', 'Brumado']
estado = ['SP', 'RJ', 'MG', 'RS', 'BA']

print('\n\nBem-vindo ao Gerador de Dados para Testes - Para finalizar digite \033[0;30;41mFIM.\033[m\n')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n')

while True:
    try:
        arquivo = open('gerar_dados.txt', 'a')
        gerarNome = random.choice(nomes)
        gerarEmail = random.choice(email)
        gerarTelefone = random.choice(telefone)
        gerarCidade = random.choice(cidade)
        gerarEstado = random.choice(estado)
        print('Escolha uma ou mais opções abaixo a serem geradas aleatoriamente!')
        escolha = input('[1] - Nome\n[2] - Email\n[3] - Telefone\n[4] - Cidade\n[5] - Estado\n[FIM] - para finalizar o programa\nDigite uma ou mais opções separadas por vírgula: ')
        if escolha == 'FIM':
            sleep(2)
            print('Programa de Teste Finalizado pelo Usuario...')
            break

        opcoes = escolha.split(',')
        for opcao in opcoes:
            if opcao == '1':
                print(gerarNome)
                arquivo.write("Nome gerado: " + gerarNome + "\n")
            elif opcao == '2':
                print(gerarEmail)
                arquivo.write("Email gerado: " + gerarEmail + "\n")
            elif opcao == '3':
                print(gerarTelefone)
                arquivo.write("Telefone gerado: " + gerarTelefone + "\n")
            elif opcao == '4':
                print(gerarCidade)
                arquivo.write("Cidade gerada: " + gerarCidade + "\n")
            elif opcao == '5':
                print(gerarEstado)
                arquivo.write("Estado gerado: " + gerarEstado + "\n")
            elif opcao == '':
                 print('Digite apenas uma opcao valida.')
                 break
            else:
                print('Voce escolheu uma opção inválida!!!')
        arquivo.write('Dados salvos com Sucesso!')
        arquivo.close()
    except:
        print('Ocorreu um erro inesperado!')
        