import sqlite3
import os
import msvcrt
import time
from user_interface import menu_principal, login

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

def reset_senha():

    os.system("cls")

    banco = sqlite3.connect("mybase.db")
    cursor = banco.cursor()
    
    tentativas = 0
    max_tentativas = 3
    
    while tentativas < max_tentativas:
        
        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋        €       ₿       $        ┋\n"
                "┋• • • ATUALIZAR MINHA SENHA • • •┋\n"
                "┋        $       ₿       €        ┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        email = input("🡆 Digite seu email:")

        cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))
        usuario = cursor.fetchone()

        if usuario:
            nova_senha = getpass_masked("\n🡆 Digite a nova senha:")
            confirmar_nova_senha = getpass_masked("🡆 Confirme sua nova senha:")
    
            if nova_senha == confirmar_nova_senha:
                cursor.execute("UPDATE usuarios SET senha = ? WHERE email = ?", (nova_senha, email))
                banco.commit()
                print("\n【Senha Atualizada! ✓✓】\n")
                time.sleep(2)
                os.system("cls")
                banco.close()
                return login.tela_de_login()
            else:
                os.system("cls")
                print("\n【A senha informada é diferente. Tente novamente. ✗✗】\n")
                tentativas += 1
                time.sleep(2)
                os.system("cls")
        else:
            os.system("cls")
            print("\n【Usuário não encontrado. Tente novamente. ✗✗】\n")
            tentativas += 1
            time.sleep(2)
            os.system("cls")

    if tentativas == max_tentativas:
        escolha = input("\n🡆 Você excedeu o número de tentativas. Voltar para o menu inicial? ([S]im/[N]ão):").lower()
        if escolha == 's':
            banco.close()
            menu_principal.tela_bem_vindo()
        else:
            banco.close()
            reset_senha()