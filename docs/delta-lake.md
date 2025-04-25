# Delta Lake com Apache Spark

Este notebook demonstra o uso do Delta Lake para comandos INSERT, UPDATE e DELETE.

## Comando INSERT

```python
from delta.tables import DeltaTable

df.write.format("delta").save("/tmp/delta/usuarios")
```

## Comando UPDATE

```python
delta_table = DeltaTable.forPath(spark, "/tmp/delta/usuarios")
delta_table.update("idade < 18", {"idade": "18"})
```

## Comando DELETE

```python
delta_table.delete("status = 'inativo'")
```
