📊 Análise de Dados Sociais com Python

Projeto desenvolvido para demonstrar um pipeline básico de dados usando Python e a biblioteca pandas, aplicando os principais conceitos de ETL (Extração, Transformação e Carga) em um conjunto de dados.

Tecnologias utilizadas

Python

Pandas

CSV (dados)

 O que este projeto faz

Este projeto realiza um pipeline de dados completo com as seguintes etapas:

Leitura de arquivo CSV

Limpeza de dados nulos

Criação de uma nova coluna calculada

Cálculo de média de valores

Exportação dos dados tratados

Como usar

Envie um arquivo chamado dados.csv para a pasta principal do projeto

Execute no terminal o comando:

python analise.py
 O que esse projeto demonstra

✔ Manipulação de dados com Python e pandas
✔ Aplicação de conceitos de ETL
✔ Organização e estrutura de código
✔ Pipeline de dados simples
✔ Prática voltada para Engenharia de Dados

 Sobre a autora

Desenvolvido por Saionara Rufino Barros Frossard
Estudante de Inteligência Artificial com foco em Engenharia de Dados e Analytics.
LinkedIn: https://www.linkedin.com/in/saionara-rufino-barros-frossard-53a1302a0/


##Estrutura do Projeto

analise-dados-sociais-python/
│
├── analise.py
├── dados.csv
├── dados_tratados.csv
├── requirements.txt
└── README.md


##Arquitetura do Pipeline

O projeto segue o padrão ETL:

- **Extract** → Leitura do arquivo CSV  
- **Transform** → Limpeza e criação de nova coluna  
- **Load** → Exportação dos dados tratados  


 ##Exemplo de execução

Iniciando pipeline de dados...
Média calculada: 1250.0
Pipeline finalizado com sucesso!
