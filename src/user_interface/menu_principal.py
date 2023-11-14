import os
from user_interface import login, cadastro, esqueci_senha, sobre

def tela_bem_vindo():

    os.system("cls")

    print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
            "┋                 €   ¥  £   ₿   $                 ┋\n"
            "┋ • • • • • • • • B E M  V I N D O • • • • • • • • ┋\n"
            "┋                 €   ¥  £   ₿   $                 ┋\n"
            "┋╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┋\n"
            "┋                                                  ┋\n"
            "┋                   [1] ENTRAR                     ┋\n"
            "┋                                                  ┋\n"
            "┋                   [2] CADASTRAR                  ┋\n"
            "┋                                                  ┋\n"
            "┋                   [3] ATUALIZAR MINHA SENHA      ┋\n"
            "┋                                                  ┋\n"
            "┋                   [4] SOBRE                      ┋\n"
            "┋                                                  ┋\n"
            "┋                                                  ┋\n"
            "┋                   [0] SAIR                       ┋\n"
            "┋                                                  ┋\n"
            "┋                                                  ┋\n"
            "┋                                                  ┋\n"
            "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
    op = int(input("🡆"))

    if (op == 1):
        login.tela_de_login()
    elif (op == 2):
        cadastro.tela_cadastro()
    elif (op == 3):
        esqueci_senha.reset_senha()
    elif (op == 4):
        sobre.meu_sobre()
    else:
        escolha = input("\n🡆 Deseja sair do sistema ([S]im/[N]ão):").lower()
        if (escolha == 's'):
            os.system("cls")
            exit()
        else:
            tela_bem_vindo()
            os.system("cls")

