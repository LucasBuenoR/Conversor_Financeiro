from user_interface import menu_principal, conversao_moeda, exibe_cotacao, login, historico_conversao, historico_cotacao, acoes
import os
import time

def meu_menu(usuario_id):
    while True:
        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋            • • • • • • $MENU • • • • • •            ┋\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "┋                                                     ┋\n"
                "┋          [1] Conversões de moedas                   ┋\n"
                "┋                                                     ┋\n"
                "┋          [2] Pesquisar ações do mercado financeiro  ┋\n"
                "┋                                                     ┋\n"
                "┋          [3] Pesquisar ticker de ativos             ┋\n"
                "┋                                                     ┋\n"
                "┋          [4] Pesquisar cotações de moedas           ┋\n"
                "┋                                                     ┋\n"
                "┋          [5] Histórico de cotações                  ┋\n"
                "┋                                                     ┋\n"
                "┋          [6] Historico de conversões                ┋\n"
                "┋                                                     ┋\n"
                "┋          [7] Notícias Financeiras                   ┋\n"
                "┋                                                     ┋\n"
                "┋                     [0] Voltar                      ┋\n"
                "┋                                                     ┋\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "┋                                                     ┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n")
        op = int(input("🡆 Escolha uma Opção:"))

        if op == 1:
            os.system("cls")
            conversao_moeda.faz_conversao(usuario_id)

        elif op == 2:
            os.system("cls")
            acoes.inicia_acoes(usuario_id)
        
        elif op == 3:
            os.system("cls")
            # Pesquisar ticker de ativos

        elif op == 4:
            os.system("cls")
            exibe_cotacao.iniciar_cotacao(usuario_id)

        elif op == 6:
            os.system("cls")
            historico_conversao.exibe_historico_conversao(usuario_id)

        elif op == 5:
            os.system("cls")
            historico_cotacao.exibe_historico_cotacao(usuario_id)
        
        elif op == 7:
            os.system("cls")
            # Notícias Financeiras

        elif op == 0:
            os.system("cls")
            menu_principal.tela_bem_vindo()
        
        else:
            print("\n【Opção Inválida ✗✗】\n")
            time.sleep(2)
            os.system("cls")

