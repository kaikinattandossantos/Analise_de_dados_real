Motivo por ter escolhido MySQL como SGBD oficial
    - Possuo experiência com esse SGBD
    - Os dados fornecidos apresentavam relacionamentos entre entidades, o que justifica o uso de um banco relacional para garantir integridade e consistência.
    - O MySQL é amplamente utilizado, possui ampla documentação e facilita consultas SQL complexas.



Bibliotecas Python Adicionais
Além das bibliotecas padrão do Python e do Pandas, foram utilizadas as seguintes:

    - mysql-connector-python: Para a conexão e interação com o banco de dados MySQL.
    - matplotlib: Para a criação e personalização dos gráficos.
    - seaborn: Para a criação de visualizações estatísticas mais elaboradas e com melhor estética sobre o Matplotlib.




Instruções de Execução
Para executar o script em Python, siga estes passos:

    1. Instalação das Bibliotecas: Abra seu terminal ou prompt de comando e instale as bibliotecas necessárias:

        pip install mysql-connector-python pandas matplotlib seaborn

    2. Configuração do Banco de Dados: Certifique-se de que você tem um servidor MySQL rodando localmente e que as credenciais e o nome do banco no script correspondem à sua configuração. O script está configurado para:

        Host: 
        Usuário: 
        Senha: 
        Banco de Dados: 

    Execução do Script: Salve o código como um arquivo .py (por exemplo, analise_saude.py) e execute-o pelo terminal:

        python analise_saude.py

    Ao ser executado, o script se conectará ao banco, processará os dados, imprimirá algumas informações no console e salvará três gráficos (.png) e um arquivo de dados (.csv) no mesmo diretório.

Para executar o script em SQL, siga esses passos:

    1. Selecione a parte que deseja executar e clique no simbolo de raio na parte superior esquerda do programa MySQL


Observações e premissas: 
    - Caso a importação de dados dentro do SQL por meio de "import data wizard" não seja bem sucedida, utilize o código:

        LOAD DATA LOCAL INFILE 'C:\\seu caminho para o arquivo CSV'
        INTO TABLE sua_tabela_que_receberá_os_dados
        CHARACTER SET utf8mb4
        FIELDS TERMINATED BY ','
        LINES TERMINATED BY '\n'
        IGNORE 1 ROWS;

        SET GLOBAL local_infile = 1;

    - Dentro do código SQL, a leitura de dados está formatada diferente no último relatório, é necessário primeiro executar o código para transformar 'NÃ£o Compareceu' em 'Não compareceu' (enviei dentro do script) e assim poder manipular a porcentagem de pessoas que não compareceram 