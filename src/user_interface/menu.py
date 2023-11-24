from user_interface import menu_principal, conversao_moeda, exibe_cotacao, login, historico_conversao, historico_cotacao, acoes, ticker, noticias
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
                "┋          [6] Histórico de conversões                ┋\n"
                "┋                                                     ┋\n"
                "┋          [7] Notícias Financeiras                   ┋\n"
                "┋                                                     ┋\n"
                "┋                     [0] Voltar                      ┋\n"
                "┋                                                     ┋\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "┋                                                     ┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝\n")
        op = int(input("🡆 Escolha uma opção:"))

        if op == 1:
            os.system("cls")
            conversao_moeda.faz_conversao(usuario_id)

        elif op == 2:
            minha_chave = 'H11QRWDOIE670Q2T'
            os.system("cls")
            acoes.exibe_acoes(usuario_id, minha_chave)
        
        elif op == 3:
            minha_chave = 'H11QRWDOIE670Q2T'
            os.system("cls")
            ticker.buscar_ticker(usuario_id, minha_chave)

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
            minha_chave = 'H11QRWDOIE670Q2T'
            os.system("cls")
            noticias.exibir_noticias(usuario_id, minha_chave)
            
        elif op == 0:
            os.system("cls")
            menu_principal.tela_bem_vindo()
        
        else:
            print("\n【Opção Inválida ✗✗】\n")
            time.sleep(2)
            os.system("cls")

