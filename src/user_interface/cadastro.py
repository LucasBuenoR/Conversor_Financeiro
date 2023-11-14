import sqlite3
import time
import os
import msvcrt
from user_interface import login

def adicionar_usuario(nome_completo, username, senha, email):
    with sqlite3.connect('mybase.db') as banco:
        cursor = banco.cursor()

    try:
        cursor.execute("INSERT INTO usuarios (nome_completo, username, senha, email) VALUES (?, ?, ?, ?)",
                       (nome_completo, username, senha, email))
        banco.commit()
        print("\n【Usuário cadastrado com sucesso! ✓✓】")
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed: usuarios.email" in str(e):
            print("\n【O e-mail já está em uso. Por favor, use outro e-mail. ✗✗】")
            banco.close()
            return False
        elif "UNIQUE constraint failed: usuarios.username" in str(e):
            print("\n【O username já está em uso. Por favor, escolha outro nome de usuário. ✗✗】")
            banco.close()
            return False
    return True

def tela_cadastro():
    os.system("cls")
    print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
            "┋        €       ₿       $        ┋\n"
            "┋• • • • FAÇA SEU CADASTRO • • • •┋\n"
            "┋        $       ₿       €        ┋\n"
            "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
    while True:
        nome_completo = input("🡆 Digite seu nome completo:")
        email = input("🡆 Digite seu e-mail.......:")
        username = input("🡆 Crie o seu username.....:")
        senha = getpass_masked("🡆 Digite sua senha........:")
        senha_1 = getpass_masked("🡆 Confirme sua senha......:")

        if senha == senha_1:
            if adicionar_usuario(nome_completo, username, senha, email):
                time.sleep(2)
                login.tela_de_login()
                os.system("cls")
                break
            else:
                print("【Por favor, preencha os dados novamente. ✗✗】\n")
        else:
            print("\n【A senha informada é diferente. Tente novamente. ✗✗】\n")
# esconde minha senha quando vou cadastrar
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
    