# Arquivo: estrutura_huffman.py
import heapq

class NoHuffman:
    def __init__(self, simbolo, freq):
        self.simbolo = simbolo
        self.freq = freq
        self.esquerda = None
        self.direita = None

    def __lt__(self, outro):
        return self.freq < outro.freq

def construir_arvore(frequencias):
    fila = [NoHuffman(s, f) for s, f in frequencias.items()]
    heapq.heapify(fila)
    while len(fila) > 1:
        esq = heapq.heappop(fila)
        dir = heapq.heappop(fila)
        pai = NoHuffman("", esq.freq + dir.freq)
        pai.esquerda = esq
        pai.direita = dir
        heapq.heappush(fila, pai)
    return fila[0] if fila else None

def gerar_codigos(raiz, prefixo="", tabela=None):
    if tabela is None:
        tabela = {}
    if raiz:
        if raiz.esquerda is None and raiz.direita is None:
            tabela[raiz.simbolo] = prefixo
        gerar_codigos(raiz.esquerda, prefixo + "0", tabela)
        gerar_codigos(raiz.direita, prefixo + "1", tabela)
    return tabela
