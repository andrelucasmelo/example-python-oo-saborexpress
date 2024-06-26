import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo': False},
                {'nome': 'Pizza Suprema', 'categoria': 'Pizza', 'ativo': True},
                {'nome': 'Cantina', 'categoria': 'Italiano', 'ativo': False}]


def exibir_nome_do_programa():
    '''Essa função exibe o titulo do Programa em forma estilizada'''
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")


def exibir_opcoes():
    '''Essa função exibe o menu de opções principal do programa'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    '''
    Função utilizada para avisar o usuario do termino po programa com sua posterior finalização
    '''
    exibir_subtitulo('Finalizando o app')
    exit()


def voltar_ao_menu_principal():
    '''
    Essa função retorna ao menu principal

    Outputs:
    - Retorna ao Menu Principal


    '''
    input('\nDigite uma tecla pra voltar a opção principal.')
    main()


def opcao_invalida():
    '''Essa função informa ao usuario que a opção escolhida é invalida
    Outputs:
    - Retorna ao menu principal
    '''
    print('opção invalida\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''
    Função utilizada para imprimir um subtitulo da função escolhida pelo usuario

    Inputs:
    - texto: (str) O texto do subtitulo
    '''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print('\n')


def cadastrar_novo_restaurante():
    '''
    Essa função é responsavel por cadastrar um novo restaurante

    Input:
    - nome_do_restaurante: Recebe o nome do novo restaurante a ser inserido
    - categoria: Recebe a categoria do novo restaurante a ser inserido

    Output:
    - Adiciona um novo restaurante a lista de restaurantes

    '''

    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante()}')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()


def listar_restaurantes():
    '''Exibe uma lista dos restaurantes cadastrados com as informações de Nome, Categoria e Status'''

    exibir_subtitulo('Listando os restaurantes')


    print(f'{"Nome do Restaurante".ljust(22)} | {"Categoria".ljust(20)} | {"Status"}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'

        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()


def alternar_estado_restaurante():
    '''
    Alterna o estado de cadastro de um restaurante buscado entre ativo e inativo.

     Output:
    -Exibe mensagem indicando sucesso da operação e retorna ao menu principal
   '''
    exibir_subtitulo('Alternando estado do restaurante')

    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado. ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante["nome"]} foi ativado com ' \
                       f'sucesso' if restaurante['ativo'] else f'O restaurante {restaurante["nome"]} ' \
                                                               f'foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():
    '''
    Função para seleção de opção no menu principal

    Outputs:
    - Executa a opção escolhida pelo usuario
    '''


    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        else:
            finalizar_app()
    except:
        opcao_invalida()


def main():
    '''
        Função principal do programa
    '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()
