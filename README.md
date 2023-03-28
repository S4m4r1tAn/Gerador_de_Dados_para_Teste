# Gerador_de_Dados_para_Teste

Esse codigo é um gerador de dados de teste em Python com interface em PySimpleGUI.

Ele gera dados aleatórios de uma lista pre-estabelecida com nomes, e-mails, telefones, cidades e estados, e permite que o usuário escolha quais informações deseja gerar.

O programa começa definindo as listas de dados que serão usadas na geração aleatória. Em seguida, entra em um loop infinito que irá rodar até que o usuário digite "FIM" para finalizar.

Dentro do loop, o programa abre um arquivo "dados_gerados.txt" em modo de adição, para que as informações geradas sejam adicionadas ao final do arquivo.

Em seguida, o programa gera aleatoriamente uma informação de cada lista definida anteriormente.

O usuário então pode escolher quais informações deseja gerar, clicando nas informacoes que deseja gerar.

Depois que o usuário escolhe as informações a serem geradas, o programa exibe as informações na interface e as escreve no arquivo de saída.

O loop continua a rodar, permitindo que o usuário gere mais informações de teste quantas vezes desejar, bastando clicar em Limpar Tela para gerar novos dados ou digitando "FIM" para finalizar o programa.
