import sqlite3
import msvcrt
import os
import time
from user_interface import menu, menu_principal, esqueci_senha


# esconde minha senha
def getpass_masked(prompt="Senha: "):
    print(prompt, end='', flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in [b'\r', b'\n']:
            print('')
            return password
        elif char == b'\b':  # Se for backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        else:
            password += char.decode('utf-8')
            print('*', end='', flush=True)
# Interface de login
def tela_de_login():
    os.system("cls")
    max_tentativas = 3
    tentativas = 0
    while tentativas < max_tentativas:
        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋        €   ₿   $        ┋\n"
                "┋• • • • L O G I N • • • •┋\n"
                "┋        $   ₿   €        ┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        username = input("🡆 Login:")
        senha = getpass_masked("🡆 Senha:")

        usuario = valida_login(username, senha)
        if usuario:
            print("\n【✓✓ Login bem-sucedido ✓✓】\n")
            time.sleep(2)
            os.system("cls")
            # pass
            return menu.meu_menu(usuario)
        else:
            tentativas += 1
            print("\n【Credenciais inválidas. Tente novamente. ✗✗】\n")
            time.sleep(2)
            os.system("cls")
    # Verifica se o número de tentativas malsucedidas atingiu o máximo
    if tentativas == max_tentativas:
        opcao = input("\n🡆 Número máximo de tentativas alcançado. Deseja atualizar sua senha? ([S]im/[N]ão):")
        if opcao.lower() == 's':
            time.sleep(2)
            os.system("cls")
            return esqueci_senha.reset_senha()
        else:
            # Reinicia as tentativas
            tentativas = 0
            time.sleep(2)
            os.system("cls")
            return menu_principal.tela_bem_vindo()
# Valida login
def valida_login(username, senha):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()
    cursor.execute(
        "SELECT id FROM usuarios WHERE username = ? AND senha = ?", (username, senha))
    usuario_id = cursor.fetchone()
    banco.close()
    if usuario_id:
        return usuario_id[0] # Retorna o ID do usuário se o login for bem-sucedido
        #print(usuario)
    else:
        return None
