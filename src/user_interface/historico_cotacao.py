import os
import sqlite3
import json
import time
from user_interface import menu


def exibe_historico_cotacao(usuario_id):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    
    cursor.execute('''
        SELECT moeda_origem, moeda_destino, taxa_cambio, data_cotacao 
        FROM historico_cotacoes 
        WHERE usuario_id = ?
        ''', (usuario_id,))

    historico = cursor.fetchall()

    if historico:
        print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "┋           HISTÓRICO DE COTAÇÕES          ┋\n"
                "┋━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┋\n"
                "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
        for cotacao in historico:
            moeda_origem, moeda_destino, taxa_cambio, data_cotacao = cotacao
            print(f"De: {moeda_origem} Para: {moeda_destino} - Valor: {taxa_cambio} em {data_cotacao}")
        print("\nOpções"
              "\n[1] Exportar histórico de cotação\n"
              "[2] Limpar histórico de cotação\n"
              "[0] Voltar para o menu")
        escolha = int(input("🡆"))
        if escolha == 1:
            exportar_historico_cotacoes(usuario_id)
        elif escolha == 2:
            limpa_historico_cotacoes(usuario_id)
            print("\n【Histórico limpo!】\n")
            time.sleep(2)
            os.system("cls")
        else:
            print()
            time.sleep(2)
            os.system("cls")
            menu.meu_menu(usuario_id)
    else:
        print("\n【Nenhum registro de cotação encontrado para este usuário.】")
        escolha = input("\n🡆 Voltar para o menu ([S]im/[N]ão):").lower()
        if escolha == 's':
            time.sleep(2)
            os.system("cls")
            menu.meu_menu(usuario_id)
        else:
            time.sleep(2)
            os.system("cls")
            exibe_historico_cotacao(usuario_id)
    banco.close()


def limpa_historico_cotacoes(usuario_id):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    # Faz o delete do histórico de conversão do usuário
    cursor.execute('''
        DELETE 
        FROM historico_cotacoes 
        WHERE usuario_id = ?
        ''', (usuario_id,))
    banco.commit()
    banco.close()


def exportar_historico_cotacoes(usuario_id):
    banco = sqlite3.connect('mybase.db')
    cursor = banco.cursor()

    # Consulta para obter o histórico de conversão do usuário
    cursor.execute('''
        SELECT moeda_origem, moeda_destino, taxa_cambio, data_cotacao 
        FROM historico_cotacoes
        WHERE usuario_id = ?
        ''', (usuario_id,))

    historico = cursor.fetchall()

    if historico:
        # Converter o histórico de conversão em uma lista de dicionários
        historico_convertido = []
        for conversao in historico:
            moeda_origem, moeda_destino, taxa_cambio, data_cotacao = conversao
            historico_convertido.append({
                'moeda_origem': moeda_origem,
                'moeda_destino': moeda_destino,
                'taxa_cambio': taxa_cambio,
                'data_cotacao': data_cotacao
            })

        nome_arquivo = f'src/historico_cotacao_usuario_{usuario_id}.json'
        with open(nome_arquivo, 'w') as file:
            json.dump(historico_convertido, file, indent=4)

        print(f"\n【Histórico de cotações do usuário {usuario_id} exportado para '{nome_arquivo}'.】\n")
        time.sleep(2)
        os.system("cls")
        exibe_historico_cotacao(usuario_id)
    else:
        print("\n【Nenhum registro de cotação encontrado para este usuário.】\n")
        time.sleep(2)
        os.system("cls")
        exibe_historico_cotacao(usuario_id)


    banco.close()