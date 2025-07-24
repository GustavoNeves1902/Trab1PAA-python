import pickle
from collections import defaultdict
from estrutura_huffman import NoHuffman, construir_arvore, gerar_codigos
from huffman_caractere import compactar_por_caractere, descompactar_por_caractere
from huffman_palavra import compactar_por_palavra, descompactar_por_palavra
import os
import time

def testar_arquivo(nome_arquivo):
    print(f"\nAnalisando arquivo: {nome_arquivo}")

    # Compactação por caractere
    inicio = time.perf_counter()
    compactar_por_caractere(nome_arquivo, "temp_caractere.huff")
    fim = time.perf_counter()
    tempo_comp_caractere = fim - inicio

    # Compactação por palavra
    inicio = time.perf_counter()
    compactar_por_palavra(nome_arquivo, "temp_palavra.huff")
    fim = time.perf_counter()
    tempo_comp_palavra = fim - inicio

    tamanho_original = os.path.getsize(nome_arquivo)
    tamanho_caractere = os.path.getsize("temp_caractere.huff")
    tamanho_palavra = os.path.getsize("temp_palavra.huff")

    taxa_caractere = (tamanho_caractere / tamanho_original) * 100
    taxa_palavra = (tamanho_palavra / tamanho_original) * 100

    print(f"Taxa de compressão (caractere): {taxa_caractere:.2f}%")
    print(f"Taxa de compressão (palavra): {taxa_palavra:.2f}%")

    print(f"Tempo compactação (caractere): {tempo_comp_caractere:.4f} segundos")
    print(f"Tempo compactação (palavra): {tempo_comp_palavra:.4f} segundos")

    # Remover arquivos temporários, se desejar
    os.remove("temp_caractere.huff")
    os.remove("temp_palavra.huff")