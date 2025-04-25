# Apache Iceberg com Apache Spark

Este notebook demonstra o uso do Apache Iceberg com comandos INSERT, UPDATE e DELETE.

## Comando INSERT

```python
df.write.format("iceberg").save("db.usuarios")
```

## Comando UPDATE

```python
spark.sql("UPDATE db.usuarios SET idade = idade + 1 WHERE idade < 18")
```

## Comando DELETE

```python
spark.sql("DELETE FROM db.usuarios WHERE status = 'inativo'")
```
