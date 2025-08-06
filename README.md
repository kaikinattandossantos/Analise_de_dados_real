# Automação de Relatórios de Ortopedia - TI Saúde

**Descrição:**

Este projeto consiste em um script Python que se conecta a um banco de dados MySQL ("ti_saude"), extrai dados de agendamentos médicos da especialidade de Ortopedia, calcula estatísticas relevantes (valor médio das consultas nos últimos 30 dias) e gera um relatório em formato CSV.  Adicionalmente, há funções para criar visualizações gráficas que sumarizam dados de agendamentos.

**Tecnologias Utilizadas:**

* Python
* Pandas
* Matplotlib
* Seaborn
* MySQL Connector/Python


**Requisitos:**

* Python 3.x instalado.
* Bibliotecas Python: `mysql-connector-python`, `pandas`, `matplotlib`, `seaborn`.  Essas podem ser instaladas via pip: `pip install mysql-connector-python pandas matplotlib seaborn`
* Um servidor MySQL rodando com o banco de dados "ti_saude" e a tabela "agendamentos".  A tabela "agendamentos" deve conter pelo menos as colunas: `especialidade`, `status_agendamento`, `data_agendamento`, `valor_consulta`.
* Credenciais de acesso ao banco de dados MySQL (definidas no código).  **É crucial alterar as credenciais padrão ("root", "senha123") por valores seguros antes de executar o script.**

**Como Executar:**

1. **Instale as bibliotecas:** Execute o comando `pip install mysql-connector-python pandas matplotlib seaborn` no seu terminal.
2. **Configure as credenciais:** Modifique as variáveis `host_db`, `usuario_db`, `senha_db` e `banco_de_dados` na função `conectar_mysql()` dentro do arquivo `ti_saude.py` com suas credenciais corretas de acesso ao banco de dados.
3. **Execute o script:** Execute o arquivo `ti_saude.py` usando um interpretador Python.  A saída mostrará o status da conexão e os resultados da automação (incluindo a criação do arquivo CSV e, em caso de conclusão, mensagens com o valor médio e informações sobre a geração dos gráficos).


**Estrutura do Código:**

O projeto é composto por dois arquivos principais:

* **`ti_saude.py`:** Contém o código fonte em Python com as funções para conectar ao banco de dados, executar a automação de Ortopedia e gerar visualizações.
* **`ti_saude.ipynb`:**  Um notebook Jupyter que demonstra o uso das funções e serve como documentação adicional.


**Funções Principais:**

* **`conectar_mysql()`:** Estabelece a conexão com o banco de dados MySQL.
* **`automacao_ortopedia(conexao)`:**  Executa a consulta SQL, processa os dados de Ortopedia, calcula a média e salva os dados em um arquivo CSV.
* **`criar_visualizacoes(conexao)`:** Gera gráficos de receita, distribuição de status e tendências de agendamento.


**Arquivo Gerado:**

O script gera o arquivo `ortopedia_ultimos_30dias.csv` contendo os dados dos agendamentos de Ortopedia dos últimos 30 dias.


**Créditos ao Autor:**

Kaiki Nattan dos Santos

**Observações:**

* O código inclui tratamento de erros básico para lidar com falhas de conexão e problemas na execução de consultas SQL.
* Para usar as funções de visualização (`criar_visualizacoes`), complete o código faltante nesse método dentro de `ti_saude.py`.  É necessário definir as consultas SQL para obter os dados necessários e usar as bibliotecas `matplotlib` e `seaborn` para criar os gráficos e salvá-los em arquivos (ex: `.png`).