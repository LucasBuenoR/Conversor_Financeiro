from user_interface import menu_principal, conversao_moeda, exibe_cotacao, login, historico_conversao, historico_cotacao
import os

def meu_menu(usuario_id):
    while True:
        print("+=====================================+\n"
              "|----------------$MENU----------------|\n"
              "|=====================================|\n"
              "|                                     |\n"
              "|     [1] - Conversão de moedas       |\n"
              "|     [2] - Exibir ações              |\n"
              "|     [3] - Exibir cotação            |\n"
              "|     [4] - Histórico de conversões   |\n" #colocar historico de conversao dentro da opcao [1] - conversao de moedas
              "|     [5] - Histórico de cotações     |\n"
              "|     [6] - Previsão de gastos        |\n"
              "|     [7] - Notícias Financeiras      |\n"
              "|     [0] - Voltar para o início      |\n"
              "|                                     |\n"
              "|                                     |\n"
              "|                                     |\n"
              "+=====================================+\n")
        op = int(input("==> Escolha uma Opção: "))
    
        if (op == 1):
            os.system("cls")
            conversao_moeda.faz_conversao(usuario_id)
        elif (op == 3):
            os.system("cls")
            exibe_cotacao.iniciar_cotacao(usuario_id)
            #dados_moedas = exibe_cotacao.obter_cotacoes_1(usuario_id)
           #exibe_cotacao.exibir_todas_cotacoes_moedas_1(dados_moedas, usuario_id)
            #dados_moedas = exibe_cotacao.obter_cotacoes_2(usuario_id)
            #exibe_cotacao.exibir_todas_cotacoes_moedas_2(dados_moedas, usuario_id)
        elif (op == 4):
            os.system("cls")
            historico_conversao.exibe_historico_conversao(usuario_id)
        elif (op == 5):
            os.system("cls")
            historico_cotacao.exibe_historico_cotacao(usuario_id)
        elif (op == 0):
            os.system("cls")
            menu_principal.tela_bem_vindo()



