# 🚀 Apache Spark com Delta Lake e Apache Iceberg

Projeto desenvolvido como parte da disciplina de Engenharia de Dados com o objetivo de demonstrar a criação de um ambiente PySpark integrado com Delta Lake e Apache Iceberg, utilizando o gerenciador de pacotes Poetry.

---

## 📄 Descrição

Este repositório contém:
- Configuração de ambiente usando **Poetry**
- Notebooks com exemplos práticos de manipulação de dados com **Delta Lake** e **Apache Iceberg**
- Documentação gerada com **MKDocs**
- Modelo ER, comandos DDL e exemplos de uso real

---

## ⚠️ Aviso

Este projeto tem fins educacionais e pode exigir ajustes dependendo do seu sistema operacional e versão do Python. Recomendado uso em máquinas com sistema baseado em Unix (Linux/Mac) ou com Windows configurado com Python corretamente e PATH ajustado.

---

## ✅ Pré-requisitos

- **Python 3.10+**
- **Poetry** instalado ([guia oficial](https://python-poetry.org/docs/#installation))
- **Java JDK 8 ou superior**
- **Jupyter Lab**

Dependências principais:

```toml
pyspark = "^3.5.0"
delta-spark = "^3.1.0"
jupyterlab = "^4.0.0"
pyarrow = "^15.0.0"
mkdocs = "^1.5.0"
mkdocs-material = "^9.4.0"
```

---

## 🛠️ Instalação

### 1. Clone o projeto

```bash
git clone https://github.com/marcosgoudinho/-APACHE-SPARK-COM-DELTA-LAKE-E-APACHE-ICEBERG.git
cd spark-delta-iceberg
```

### 2. Instale as dependências

```bash
poetry install
```

### 3. Ative o ambiente virtual

```bash
poetry shell
```

### 4. Rode o Jupyter Lab

```bash
jupyter lab
```

> **Importante:** Caso o kernel Jupyter não esteja disponível, execute:
>
> ```bash
> python -m ipykernel install --user --name=spark-lake-project
> ```

---

## 🧪 How to: Como usar o projeto

### ⚡ SparkSession com Delta e Iceberg

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("SparkLake") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension,org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.iceberg.spark.SparkSessionCatalog") \
    .config("spark.sql.catalog.spark_catalog.type", "hive") \
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog") \
    .config("spark.sql.catalog.local.type", "hadoop") \
    .config("spark.sql.catalog.local.warehouse", "./warehouse") \
    .getOrCreate()
```

### 🧊 Iceberg: Exemplo de uso

```python
spark.sql("CREATE TABLE local.db.iceberg_table (id BIGINT) USING ICEBERG")
spark.sql("INSERT INTO local.db.iceberg_table VALUES (1), (2), (3)")
```

### 🔺 Delta Lake: Exemplo de uso

```python
data = spark.range(0, 5)
data.write.format("delta").mode("overwrite").save("warehouse/delta-table")
```

---

## 🧪 Testes

> Este projeto não possui testes automatizados. Recomendado executar os notebooks e validar outputs esperados no próprio ambiente Jupyter.

---

## 📚 Documentação

Acesse a documentação completa (gerada com MKDocs):

🔗 [Documentação do Projeto (localhost)](http://127.0.0.1:8000)

Para rodar localmente:

```bash
mkdocs serve
```

---
