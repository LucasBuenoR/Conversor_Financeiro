from user_interface import menu_principal
import os
def meu_sobre():

    os.system("cls")
    print("\n╔━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╗\n"
            "┋                           €   ¥  £   ₿   $                           ┋\n"
            "┋           • • • • • • • • • •  SOBRE   • • • • • • • • • •           ┋\n"
            "┋                           €   ¥  £   ₿   $                           ┋\n"
            "┋╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼╼┋\n"
            "┋                                                                      ┋\n"
            "┋                   • • • CONVERSOR FINANCEIRO • • •                   ┋\n"
            "┋                                                                      ┋\n"
            "┋                     • • •  ₿  OBJETIVO  ₿  • • •                     ┋\n"
            "┋  O Conversor Financeiro é uma ferramenta que fornece informações em  ┋\n"
            "┋  tempo real sobre conversões de moedas, cotações, ações e notícias   ┋\n"
            "┋  financeiras. O principal objetivo é oferecer aos usuários uma       ┋\n"
            "┋  maneira simples e eficiente de acompanhar e analisar dados          ┋\n"
            "┋  financeiros.                                                        ┋\n"
            "┋                                                                      ┋\n"
            "┋                     • • • DESENVOLVIDO POR • • •                     ┋\n"
            "┋                      Edson Teo Araujo - 2840482213034                ┋\n"
            "┋                      Lucas Bueno Rojas Barbosa - 2840482023039       ┋\n"
            "┋                                                                      ┋\n"
            "┋           • Direitos Autorais © 2023 Top.Esp.Informática •           ┋\n"
            "╚━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╝")
    escolha = input("\n🡆 Deseja voltar para o menu inicial ([S]im/[N]ão):").lower()
    if (escolha == 's'):
            os.system("cls")
            menu_principal.tela_bem_vindo()
    else:
        meu_sobre()
        os.system("cls")