# Automação de Relatórios de Ortopedia - TI Saúde

**Descrição:**

Este projeto consiste em um script Python que automatiza a geração de relatórios para a especialidade de Ortopedia, utilizando dados de um banco de dados MySQL. O script conecta ao banco de dados, extrai informações de agendamentos realizados nos últimos 30 dias, calcula o valor médio das consultas e exporta os dados para um arquivo CSV.  Além disso, contém funções para criar visualizações gráficas dos dados.


**Tecnologias Utilizadas:**

* Python
* Pandas
* Matplotlib
* Seaborn
* MySQL Connector

**Requisitos:**

* Python 3.x instalado.
* Bibliotecas Python: `mysql-connector-python`, `pandas`, `matplotlib`, `seaborn`.  Essas bibliotecas podem ser instaladas usando `pip install mysql-connector-python pandas matplotlib seaborn`.
* Um banco de dados MySQL chamado "ti_saude" com uma tabela chamada "agendamentos" contendo pelo menos as colunas: `especialidade`, `status_agendamento`, `data_agendamento`, `valor_consulta`.  As credenciais de conexão estão codificadas no script (por razões de simplicidade no exemplo, mas **NÃO É RECOMENDADO** para produção.  Considere variáveis de ambiente ou um arquivo de configuração separado).
* As credenciais de acesso ao banco de dados (usuario, senha) devem ser alteradas para as suas credenciais.


**Como Executar:**

1. **Instale as bibliotecas:** Abra seu terminal ou prompt de comando e execute: `pip install mysql-connector-python pandas matplotlib seaborn`
2. **Configure as credenciais:**  Modifique as variáveis `host_db`, `usuario_db`, `senha_db` e `banco_de_dados` na função `conectar_mysql()` em `ti_saude.py` com suas credenciais corretas.
3. **Execute o script:** Execute o script `ti_saude.py` a partir do terminal usando o comando: `python ti_saude.py`

O script irá conectar ao banco de dados, executar a consulta para a especialidade de Ortopedia, gerar o arquivo CSV (`ortopedia_ultimos_30dias.csv`) e imprimir o valor médio das consultas.  A função `criar_visualizacoes` está incompleta no exemplo fornecido e precisará ser completada para gerar as visualizações.


**Estrutura do Projeto:**

* `ti_saude.py`: Script Python principal contendo as funções para conexão com o banco de dados, processamento dos dados e geração do relatório.
* `ti_saude.ipynb`: Notebook Jupyter com código similar ao de `ti_saude.py` (provavelmente usado para desenvolvimento e testes).


**Funções Principais (ti_saude.py):**

* `conectar_mysql()`: Conecta ao banco de dados MySQL. Retorna a conexão ou `None` em caso de erro.
* `automacao_ortopedia(conexao)`: Executa a automação específica para Ortopedia. Consulta os dados, calcula a média dos valores das consultas e salva em um arquivo CSV.
* `criar_visualizacoes(conexao)`:  (Incompleta no exemplo) Esta função irá criar e salvar as visualizações gráficas.


**Exemplo de saída (Console):**

```
Conexão com o banco de dados MySQL bem-sucedida!
Executando a consulta para Ortopedia...
15 agendamentos de Ortopedia encontrados.
Dados exportados com sucesso para o arquivo 'ortopedia_ultimos_30dias.csv'.
O valor médio das consultas de Ortopedia nos últimos 30 dias é: R$ 250.50
```


**Créditos ao Autor:** Kaiki Nattan dos Santos