# 🏛️ Dashboard de Deputados - Processo Seletivo Vobys

Este projeto foi desenvolvido como parte de um desafio técnico para uma vaga de estágio. A aplicação realiza a extração de dados da API da Câmara dos Deputados, armazena as informações em um banco de dados relacional e as disponibiliza através de uma interface Web e um Dashboard analítico.

---

## 🚀 Demonstração

### Interface Web (Flask)
A aplicação consome os dados e gera uma tabela dinâmica para visualização rápida.
![Flask Web App](print-flask.png)

### Dashboard Analítico (Power BI)
Um diferencial do projeto é a camada de inteligência de dados, que permite filtrar e analisar a distribuição dos deputados por partido e estado.
- Em produção!

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.14
* **API:** [Dados Abertos da Câmara dos Deputados](https://dadosabertos.camara.leg.br/swagger/api.html
))
* **Banco de Dados:** SQLite3 (Persistência local)
* **Framework Web:** Flask (Exibição dos dados)
* **Manipulação de Dados:** Pandas (Exportação para CSV)
* **Visualização:** Power BI Desktop

---

## 📋 Funcionalidades

1.  **Consumo de API:** Busca dados atualizados sobre os deputados.
2.  **Persistência:** Salva automaticamente no banco `camara_dados.db`.
3.  **Tratamento de Dados:** Utiliza SQL para criar tabelas, limpar registros antigos e inserir novos dados sem duplicidade.
4.  **Visualização Web:** Servidor local que exibe os dados em HTML/CSS.
5.  **BI Integration:** Exporta os dados tratados para integração com Power BI.

---

## 🔧 Como Executar o Projeto

### 1. Preparar o ambiente
Clone o repositório e crie um ambiente virtual:
```bash
git clone [https://github.com/mariaclaramariano/projeto-estagio-vobys.git](https://github.com/mariaclaramariano/projeto-estagio-vobys.git)
cd projeto-estagio-vobys
python -m venv venv
.\venv\Scripts\activate  # Windows
