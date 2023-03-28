import random
from time import sleep
import PySimpleGUI as sg

nomes = ['Emerson', 'Keli', 'Thomas', 'Nicholas', 'Christopher']
email = ['emerson@email.com', 'keli@email.com', 'thomas@email.com', 'nicholas@email.com', 'christopher@email.com']
telefone = [1143527995, 5199963652, 447909138487, 1143526669, 3499965889]
cidade = ['Sao Bernado do Campo', 'Niteroi', 'Caratinga', 'Porto Alegre', 'Brumado']
estado = ['SP', 'RJ', 'MG', 'RS', 'BA']

sg.theme('DarkAmber')

layout = [
    [sg.Text('Bem-Vindo(a) ao Gerador de Dados para Testes')],
    [sg.Text('Escolha uma ou mais opções abaixo a serem geradas aleatoriamente!')],
    [sg.Checkbox('Nome', key='nome'), sg.Checkbox('Email', key='email'),
     sg.Checkbox('Telefone', key='telefone'), sg.Checkbox('Cidade', key='cidade'),
     sg.Checkbox('Estado', key='estado')],
    [sg.Button('Gerar Dados'), sg.Button('FIM')],
    [sg.Output(size=(40,10))]
]

window = sg.Window('Gerador de Dados', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == 'FIM':
        print('Programa de Teste Finalizado pelo Usuario...')
        sg.Popup('Programa Finalizado com Sucesso!')
        break

    opcoes = []
    for key in ['nome', 'email', 'telefone', 'cidade', 'estado']:
        if values[key]:
            opcoes.append(key)

    if not opcoes:
        sg.Popup('Selecione pelo menos uma opção!')
        continue

    try:
        arquivo = open('gerar_dados.txt', 'a')
        gerarNome = random.choice(nomes)
        gerarEmail = random.choice(email)
        gerarTelefone = random.choice(telefone)
        gerarCidade = random.choice(cidade)
        gerarEstado = random.choice(estado)

        for opcao in opcoes:
            if opcao == 'nome':
                print(gerarNome)
                arquivo.write("Nome gerado: " + gerarNome + "\n")
            elif opcao == 'email':
                print(gerarEmail)
                arquivo.write("Email gerado: " + gerarEmail + "\n")
            elif opcao == 'telefone':
                print(gerarTelefone)
                arquivo.write("Telefone gerado: " + gerarTelefone + "\n")
            elif opcao == 'cidade':
                print(gerarCidade)
                arquivo.write("Cidade gerada: " + gerarCidade + "\n")
            elif opcao == 'estado':
                print(gerarEstado)
                arquivo.write("Estado gerado: " + gerarEstado + "\n")
        arquivo.write('Dados salvos com Sucesso!\n')
        arquivo.close()
    except:
        print('Ocorreu um erro inesperado!')
        sg.Popup('Ocorreu um erro inesperado!')
window.close()
