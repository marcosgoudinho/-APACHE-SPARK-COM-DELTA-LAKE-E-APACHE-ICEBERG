# Apache Iceberg

## O que é o Apache Iceberg?

O **Apache Iceberg** é um formato de tabela para dados estruturados de grandes volumes, ideal para usar com ferramentas como **Apache Spark**, **Hive** e outras. Ele oferece recursos avançados como gerenciamento de versões, evoluções de esquema e operações em paralelo.

### Funcionalidades do Apache Iceberg:

- **Gerenciamento de Tabelas em Grande Escala**: Permite o gerenciamento de grandes volumes de dados distribuídos em várias partições.
- **Suporte a Várias Versões**: O Iceberg permite o controle de versões de dados e operações como `time travel`.
- **Evolução de Esquema**: Permite modificar o esquema de dados sem precisar refazer a tabela.
- **Leitura e Escrita Eficientes**: Suporta operações eficientes de leitura e escrita sobre grandes datasets.

## Como Usar Apache Iceberg

Para usar o Iceberg com **Apache Spark**, você pode integrar a dependência do Iceberg:

1. **Adicionar dependência Iceberg no Spark**:
   ```bash
   --packages org.apache.iceberg:iceberg-spark3-runtime:0.13.0

2. **Criar uma Tabela Iceberg:**:
    spark.sql("CREATE TABLE iceberg_table USING iceberg")

3. **Ler uma Tabela Iceberg:**:
    df = spark.read.format("iceberg").load("path/to/iceberg_table")

4. **Escrever Dados para Iceberg:**:
   df.write.format("iceberg").save("path/to/iceberg_table")
