import os
import sys
from pyspark.sql import SparkSession

def main(caminho_csv: str, caminho_saida: str):
    spark = SparkSession.builder \
        .appName("Conversor CSV para Parquet") \
        .getOrCreate()

    # Verifica se o arquivo CSV existe
    if not os.path.exists(caminho_csv):
        print(f"Erro: O arquivo {caminho_csv} não foi encontrado.")
        sys.exit(1)

    # Criação da pasta de saída, caso não exista
    if not os.path.exists(caminho_saida):
        os.makedirs(caminho_saida)
        print(f"A pasta de saída {caminho_saida} foi criada.")

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
    caminho_csv = "C:/Users/nicolas.7220/Desktop/teste/-APACHE-SPARK-COM-DELTA-LAKE-E-APACHE-ICEBERG/data/raw/teste.csv"
    caminho_saida = "C:/Users/nicolas.7220/Desktop/teste/-APACHE-SPARK-COM-DELTA-LAKE-E-APACHE-ICEBERG/data/processed/teste"

    main(caminho_csv, caminho_saida)
