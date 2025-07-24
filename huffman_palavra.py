# Arquivo: huffman_palavra.py
import pickle
import re
from collections import defaultdict
from estrutura_huffman import NoHuffman, construir_arvore, gerar_codigos

def compactar_por_palavra(nome_entrada, nome_saida):
    with open(nome_entrada, "r", encoding="utf-8") as f:
        texto = f.read()

    palavras = re.findall(r"\w+|\W+", texto)
    frequencias = defaultdict(int)
    for p in palavras:
        frequencias[p] += 1

    raiz = construir_arvore(frequencias)
    codigos = gerar_codigos(raiz)

    bits = "".join(codigos[p] for p in palavras)
    bytes_compactados = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8].ljust(8, '0')
        bytes_compactados.append(int(byte, 2))

    with open(nome_saida, "wb") as f:
        pickle.dump((raiz, len(bits), bytes_compactados), f)

    print("Arquivo compactado por palavra com sucesso.")

def descompactar_por_palavra(nome_entrada, nome_saida):
    with open(nome_entrada, "rb") as f:
        raiz, total_bits, bytes_compactados = pickle.load(f)

    bits = "".join(f"{byte:08b}" for byte in bytes_compactados)[:total_bits]
    resultado = []
    atual = raiz
    for bit in bits:
        atual = atual.esquerda if bit == '0' else atual.direita
        if atual.esquerda is None and atual.direita is None:
            resultado.append(atual.simbolo)
            atual = raiz

    with open(nome_saida, "w", encoding="utf-8") as f:
        f.write("".join(resultado))

    print("Arquivo descompactado por palavra com sucesso.")
