# Delta Lake

## O que é o Delta Lake?

O **Delta Lake** é uma camada de armazenamento de open-source que roda sobre o **Apache Spark**. Ele oferece suporte a **ACID transactions** (Atomicidade, Consistência, Isolamento e Durabilidade), tornando o armazenamento de dados mais confiável e eficiente.

### Funcionalidades do Delta Lake:

- **ACID Transactions**: Garante que todas as operações de leitura e gravação sejam consistentes e seguras.
- **Schema Evolution**: Suporte para alterações no esquema de dados ao longo do tempo.
- **Time Travel**: Capacidade de acessar versões anteriores dos dados.
- **Stream and Batch Processing**: Integração com processos em lote e streaming.

## Como Usar Delta Lake

Para usar o Delta Lake em seu projeto Spark, você pode seguir as etapas básicas:

1. **Importar o Delta Lake**:
   ```python
   from delta import DeltaTable

2. **Criar uma Tabela Delta:**:
df.write.format("delta").save("/path/to/delta_table")

3. **Leitura de uma Tabela Delta:**:
df = spark.read.format("delta").load("/path/to/delta_table")

4. **Gerenciar Atualizações e Versionamento:**:
deltaTable = DeltaTable.forPath(spark, "/path/to/delta_table")
deltaTable.update(condition, set)