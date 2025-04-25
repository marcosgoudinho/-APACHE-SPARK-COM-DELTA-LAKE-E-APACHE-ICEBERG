# 🚀 Apache Spark com Delta Lake e Apache Iceberg

Projeto desenvolvido como parte da disciplina de Engenharia de Dados com o objetivo de demonstrar a criação de um ambiente PySpark integrado com Delta Lake e Apache Iceberg, utilizando o gerenciador de pacotes Poetry.

---

## 📄 Descrição

Este repositório contém:
- Configuração de ambiente usando *Poetry*
- Notebooks com exemplos práticos de manipulação de dados com *Delta Lake* e *Apache Iceberg*
- Documentação gerada com *MKDocs*
- Modelo ER, comandos DDL e exemplos de uso real

---

## ⚠️ Aviso

Este projeto tem fins educacionais e pode exigir ajustes dependendo do seu sistema operacional e versão do Python. Recomendado uso em máquinas com sistema baseado em Unix (Linux/Mac) ou com Windows configurado com Python corretamente e PATH ajustado.

---

## ✅ Pré-requisitos

- *Python 3.10+*
- *Poetry* instalado ([guia oficial](https://python-poetry.org/docs/#installation))
- *Java JDK 8 ou superior*
- *Jupyter Lab*

Dependências principais:

```toml
pyspark = "^3.5.0"
delta-spark = "^3.1.0"
jupyterlab = "^4.0.0"
pyarrow = "^15.0.0"
mkdocs = "^1.5.0"