# <h1>Projeto Acadêmico De Tópicos Especiais Em Informática<h1>

## <h2>Requisitos<h2>
* Implementar uma aplicação que contenha pelo menos dez interfaces gráficas (UI).
o O tipo de UI pode ser definido pelos integrantes: Console, Formulário ou Web.
- [x] console.
- [ ] Formulário.
- [ ] Web.

* Armazenar dados de maneira persistente utilizando o SGBD da sua preferência.
  * O SGBD escolhido foi SQLite
*  Os dados precisam ser armazenados em pelo menos três tabelas.
   * Tabelas do nosso sistema: usuarios, historico_conversoes e historico_cotacoes.
*  Para cada tabela codificar na UI no mínimo três operações, dentre elas:
   Insert, Update, Delete e/ou Select.
    * Nossa aplicação realiza três operações SQL:
    * Insert - Insere novos usuários no sistema.
    * Update - Atualiza senhas dos usuários.
    * Delete - Deleta históricos de conversões e cotações de moedas.
      
* Elaborar, necessariamente, as seguintes UI:
- [x] Login: em que o usuário deverá fornecer um nome de usuário e uma senha. O
  acesso as funcionalidades do sistema ocorrem apenas para usuários previamente
  cadastrados.
- [x] Sobre: que apresente dados do projeto {tema escolhido e objetivo} e dos
    desenvolvedores: {nome completo e código de matrícula}.
- [x] Menu: em que o usuário poderá escolher a opção desejada da aplicação.

* Implementar uma funcionalidade que exporta todos os dados da aplicação no formato
  JSON. O arquivo deve ser compactado no formato zip.
  * Nas telas histórico de conversões e cotações o usuário consegue exportar os arquivos JSON e .zip.

* Implementar uma funcionalidade para importa dados.
  * Os dados devem ser disponibilizados em um endereço da web.
     * Usamos o flask para disponibilizar o arquivo JSON exportado pelo usuário.
  * Usar o módulo Requests ou URLlib.
     * Usamos o Requests.
  * Armazenar os dados importados em uma tabela.
     * Os dados importados são armazenados na tabelas historico_conversoes e historico_cotacoes.
  * Apresentar os dados importados em uma UI da aplicação.
     * os dados importados são apresentados em 7 telas da aplicação.

* Quantidade de telas exigidas 10
  * Atualmente a aplicação tem 12 telas. 
