# <h1>Projeto Acadêmico De Tópicos Especiais Em Informática:computer::snake:<h1>
## <h2>:memo:Requisitos<h2>
* **Implementar uma aplicação que contenha pelo menos dez interfaces gráficas (UI).
  O tipo de UI pode ser definido pelos integrantes: Console, Formulário ou Web.**
  - :white_check_mark:UI escolhido: Console

* **Armazenar dados de maneira persistente utilizando o SGBD da sua preferência.**
  - :white_check_mark:O SGBD escolhido foi SQLite:floppy_disk:
*  **Os dados precisam ser armazenados em pelo menos três tabelas.**
   - :white_check_mark:Tabelas do nossa aplicação: usuarios, historico_conversoes e historico_cotacoes.
*  **Para cada tabela codificar na UI no mínimo três operações, dentre elas:
   Insert, Update, Delete e/ou Select.**
    * Nossa aplicação realiza três operações SQL:floppy_disk::
    - :white_check_mark:Insert - Insere novos usuários no sistema.
    - :white_check_mark:Update - Atualiza senhas dos usuários.
    - :white_check_mark:Delete - Deleta históricos de conversões e cotações de moedas.
* **Elaborar, necessariamente, as seguintes UI:**
  - :white_check_mark:Login: em que o usuário deverá fornecer um nome de usuário e uma senha. O
    acesso as funcionalidades do sistema ocorrem apenas para usuários previamente
    cadastrados.
  - :white_check_mark:Sobre: que apresente dados do projeto {tema escolhido e objetivo} e dos
    desenvolvedores: {nome completo e código de matrícula}.
  - :white_check_mark:Menu: em que o usuário poderá escolher a opção desejada da aplicação.

* **Implementar uma funcionalidade que exporta todos os dados da aplicação no formato
  JSON:page_with_curl:. O arquivo deve ser compactado no formato .zip:file_folder:.**
  - :white_check_mark:Nas telas histórico de conversões e cotações o usuário consegue exportar os arquivos JSON:page_with_curl: e .zip:file_folder:.

* **Implementar uma funcionalidade para importa dados.**
* **Os dados devem ser disponibilizados em um endereço da web.**
     - :white_check_mark:Usamos o flask para disponibilizar o arquivo JSON:page_with_curl: exportado pelo usuário.
* **Usar o módulo Requests ou URLlib.**
     - :white_check_mark:Usamos o Requests.
* **Armazenar os dados importados em uma tabela.**
     - :white_check_mark:Os dados importados são armazenados na tabelas historico_conversoes e historico_cotacoes.
* **Apresentar os dados importados em uma UI da aplicação.**
     - :white_check_mark:Os dados importados são apresentados em 7 telas da aplicação.

* **Quantidade de telas exigidas 10:flower_playing_cards:**
  - :white_check_mark:Atualmente a aplicação tem 12 telas:flower_playing_cards:. 
