import os
import sys
from pyspark.sql import SparkSession

def main(caminho_csv: str, caminho_saida: str):
    spark = SparkSession.builder \
        .appName("Conversor CSV para Parquet") \
        .getOrCreate()

    # Leitura do CSV
    print(f"Lendo arquivo CSV de: {caminho_csv}")
    df = spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(caminho_csv)

    # Escrita em formato Parquet
    print(f"Salvando arquivo Parquet em: {caminho_saida}")
    df.write.mode("overwrite").parquet(caminho_saida)

    print("Conversão concluída com sucesso!")
    spark.stop()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python converte_csv_para_parquet.py <caminho_csv> <caminho_saida_parquet>")
        sys.exit(1)

    caminho_csv = sys.argv[1]
    caminho_saida = sys.argv[2]

    if not os.path.exists(caminho_csv):
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")
        sys.exit(1)

    main(caminho_csv, caminho_saida)
