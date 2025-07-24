import mysql.connector
from mysql.connector import Error
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def conectar_mysql():
    """
    Estabelece conexão com o banco de dados MySQL.

    Retorna:
        - Objeto de conexão se bem-sucedido.
        - None, caso ocorra algum erro.
    """
    try:
        host_db = "localhost"
        usuario_db = "root"
        senha_db = "senha123"
        banco_de_dados = "ti_saude"

        conexao = mysql.connector.connect(
            host=host_db,
            user=usuario_db,
            password=senha_db,
            database=banco_de_dados
        )

        if conexao.is_connected():
            print("Conexão com o banco de dados MySQL bem-sucedida!")
            return conexao

    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

def automacao_ortopedia(conexao):
    """
    Executa a automação para a especialidade de Ortopedia:
    - Consulta os agendamentos realizados nos últimos 30 dias.
    - Calcula o valor médio das consultas.
    - Exporta os dados para um arquivo CSV.
    """
    if not conexao:
        print("Não foi possível realizar a automação por falta de conexão.")
        return
    try:
        # Consulta SQL para Ortopedia nos últimos 30 dias 
        query_ortopedia = """
        SELECT * FROM agendamentos
        WHERE especialidade = 'Ortopedia' AND status_agendamento = 'Realizado'
          AND data_agendamento >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
        """
        print("\nExecutando a consulta para Ortopedia...")
        df_ortopedia = pd.read_sql_query(query_ortopedia, conexao)

        # Verifica se há resultados
        if df_ortopedia.empty:
            print("Nenhum agendamento de Ortopedia encontrado nos últimos 30 dias.")
            return

        print(f"{len(df_ortopedia)} agendamentos de Ortopedia encontrados.")

        # Converte o valor da consulta para tipo numérico (caso esteja como string)
        df_ortopedia['valor_consulta'] = pd.to_numeric(df_ortopedia['valor_consulta'])

        # Calcula valor médio
        valor_medio = df_ortopedia['valor_consulta'].mean()

        # Exportação dos dados de Ortopedia para CSV 
        nome_arquivo_csv = 'ortopedia_ultimos_30dias.csv'
        df_ortopedia.to_csv(nome_arquivo_csv, index=False, sep=';', decimal=',')

        print(f"Dados exportados com sucesso para o arquivo '{nome_arquivo_csv}'.")
        print(f"\nO valor médio das consultas de Ortopedia nos últimos 30 dias é: R$ {valor_medio:.2f}")

    except Error as e:
        print(f"Erro ao executar a consulta SQL: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

def criar_visualizacoes(conexao):
    """
    Cria e salva visualizações gráficas com base nos dados da tabela 'agendamentos':
    - Receita total por especialidade.
    - Distribuição de status dos agendamentos.
    - Tendência mensal de agendamentos realizados.
    """
    if not conexao:
        print("Não foi possível criar visualizações por falta de conexão.")
        return

    print("\nIniciando a criação de visualizações...")
    try:
        # Carrega todos os dados da tabela 
        query_total = "SELECT * FROM agendamentos;"
        df_total = pd.read_sql_query(query_total, conexao, parse_dates=['data_agendamento'])

        # Define estilo estético para os gráficos
        sns.set_style("whitegrid")

        # Gráfico 1: Receita por Especialidade 
        print("Gerando Gráfico 1: Receita por Especialidade...")
        # Filtra apenas agendamentos realizados ou confirmados
        df_receita = df_total[df_total['status_agendamento'].isin(['Realizado', 'Confirmado'])].copy()
        df_receita['valor_consulta'] = pd.to_numeric(df_receita['valor_consulta'])

        # Agrupa e soma a receita por especialidade
        receita_por_especialidade = df_receita.groupby('especialidade')['valor_consulta'].sum().sort_values(ascending=False)

        # Cria gráfico de barras
        plt.figure(figsize=(12, 7))
        ax1 = sns.barplot(x=receita_por_especialidade.index, y=receita_por_especialidade.values, palette="viridis")
        ax1.set_title('Receita Total por Especialidade (Realizados + Confirmados)', fontsize=16)
        ax1.set_xlabel('Especialidade', fontsize=12)
        ax1.set_ylabel('Receita Total (R$)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig('receita_por_especialidade.png')
        print("Gráfico 'receita_por_especialidade.png' salvo com sucesso.")
        plt.show()
        plt.close()

        # Gráfico 2: Distribuição de Status dos Agendamentos 
        print("\nGerando Gráfico 2: Distribuição de Status dos Agendamentos...")
        plt.figure(figsize=(10, 6))
        ax2 = sns.countplot(x='status_agendamento', data=df_total, palette="plasma",
                            order=df_total['status_agendamento'].value_counts().index)
        ax2.set_title('Distribuição de Status dos Agendamentos', fontsize=16)
        ax2.set_xlabel('Status do Agendamento', fontsize=12)
        ax2.set_ylabel('Quantidade', fontsize=12)
        plt.tight_layout()
        plt.savefig('distribuicao_status_agendamentos.png')
        print("Gráfico 'distribuicao_status_agendamentos.png' salvo com sucesso.")
        plt.show()
        plt.close()

        # --- Gráfico 3: Tendência de Agendamentos Realizados por Mês ---
        print("\nGerando Gráfico 3: Tendência de Agendamentos Realizados por Mês...")
        # Filtra apenas agendamentos realizados
        df_realizados = df_total[df_total['status_agendamento'] == 'Realizado'].copy()

        # Extrai o período (mês e ano) para análise de tendência
        df_realizados['mes_ano'] = df_realizados['data_agendamento'].dt.to_period('M')
        agendamentos_por_mes = df_realizados.groupby('mes_ano').size()
        agendamentos_por_mes.index = agendamentos_por_mes.index.to_timestamp()

        # Cria gráfico de linha
        plt.figure(figsize=(12, 6))
        ax3 = sns.lineplot(x=agendamentos_por_mes.index, y=agendamentos_por_mes.values,
                           marker='o', color='royalblue')
        ax3.set_title('Tendência de Agendamentos Realizados por Mês', fontsize=16)
        ax3.set_xlabel('Mês', fontsize=12)
        ax3.set_ylabel('Número de Agendamentos Realizados', fontsize=12)
        plt.tight_layout()
        plt.savefig('tendencia_agendamentos_mensal.png')
        print("Gráfico 'tendencia_agendamentos_mensal.png' salvo com sucesso.")
        plt.show()
        plt.close()

    except Exception as e:
        print(f"Ocorreu um erro ao gerar as visualizações: {e}")

# Ponto de entrada principal
if __name__ == '__main__':
    # Tenta estabelecer a conexão com o banco de dados
    conn = conectar_mysql()

    # Se a conexão for bem-sucedida, executa as funções principais
    if conn and conn.is_connected():
        try:
            # Executa a automação específica para Ortopedia
            automacao_ortopedia(conn)

            # Gera os gráficos e visualizações gerais
            criar_visualizacoes(conn)

        finally:
            # Fecha a conexão com o banco ao final da execução
            conn.close()
            print("\nConexão com o MySQL foi fechada.")
    else:
        print("\nA execução foi interrompida devido à falha na conexão com o banco de dados.")
