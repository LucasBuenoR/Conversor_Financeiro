import os
import sqlite3
import json
import time
from user_interface import menu
import zipfile


def exibe_historico_conversao(usuario_id):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    # Consulta para obter o histórico de conversão do usuário
    cursor.execute('''
        SELECT moeda_origem, moeda_destino, valor_origem, valor_convertido, data_conversao 
        FROM historico_conversoes 
        WHERE usuario_id = ?
        ''', (usuario_id,))

    historico = cursor.fetchall()

    if historico:
        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "┋          HISTÓRICO DE CONVERSÕES         ┋\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        for conversao in historico:
            moeda_origem, moeda_destino, valor_origem, valor_convertido, data_conversao = conversao
            print(f"De: {moeda_origem} Para: {
                  moeda_destino} - Valor: {valor_origem} Convertido: {valor_convertido} em {data_conversao}")
        print("\nOpções"
              "\n[1] Exportar histórico de conversões\n"
              "[2] Limpar histórico de conversões\n"
              "[0] Voltar para o menu")
        escolha = int(input("🡆"))
        if escolha == 1:
            exportar_historico_conversoes(usuario_id)
        elif escolha == 2:
            limpa_historico_conversoes(usuario_id)
            print("\n【Histórico limpo!】\n")
            time.sleep(2)
            os.system("cls")
        else:
            print()
            time.sleep(2)
            os.system("cls")
            menu.meu_menu(usuario_id)
    else:
        print("\n【Nenhum registro de conversão encontrado para este usuário.】")
        escolha = input("\n🡆 Voltar para o menu ([S]im/[N]ão):").lower()
        if escolha == 's':
            time.sleep(2)
            os.system("cls")
            menu.meu_menu(usuario_id)
        else:
            time.sleep(2)
            os.system("cls")
            exibe_historico_conversao(usuario_id)
    banco.close()


def limpa_historico_conversoes(usuario_id):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    # Faz o delete do histórico de conversão do usuário
    cursor.execute('''
        DELETE 
        FROM historico_conversoes 
        WHERE usuario_id = ?
        ''', (usuario_id,))
    banco.commit()
    banco.close()


def exportar_historico_conversoes(usuario_id):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    # Consulta para obter o histórico de conversão do usuário
    cursor.execute('''
        SELECT moeda_origem, moeda_destino, valor_origem, valor_convertido, data_conversao 
        FROM historico_conversoes 
        WHERE usuario_id = ?
        ''', (usuario_id,))

    historico = cursor.fetchall()

    nome_arquivo_json = f'src/historico_usuario.json'

    if historico:
        # Converter o histórico de conversão em uma lista de dicionários
        historico_convertido = []
        for conversao in historico:
            moeda_origem, moeda_destino, valor_origem, valor_convertido, data_conversao = conversao
            historico_convertido.append({
                'moeda_origem': moeda_origem,
                'moeda_destino': moeda_destino,
                'valor_origem': valor_origem,
                'valor_convertido': valor_convertido,
                'data_conversao': data_conversao
            })

        # Exportar o histórico de conversões para um arquivo JSON
        with open(nome_arquivo_json, 'w') as arquivo_json:
            json.dump(historico_convertido, arquivo_json, indent=4)
        
        # Cria o arquivo ZIP e adiciona o arquivo JSON ao ZIP
        nome_arquivo_zip = f'src/historico_usuario.zip'
        with zipfile.ZipFile(nome_arquivo_zip, 'w') as zip_file:
            zip_file.write(nome_arquivo_json, arcname='historico_usuario.json')
        
        print(f"\n【Histórico de conversões do usuário {usuario_id} exportado para '{nome_arquivo_json}' e compactado em '{nome_arquivo_zip}'.】\n")
        time.sleep(3)
        os.system("cls")
        exibe_historico_conversao(usuario_id)

    else:
        print("\n【Nenhum registro de conversão encontrado para este usuário.】\n")
        time.sleep(2)
        os.system("cls")
        exibe_historico_conversao(usuario_id)
    banco.close()

    return nome_arquivo_json, nome_arquivo_zip
