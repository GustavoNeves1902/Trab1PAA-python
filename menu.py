from huffman_caractere import compactar_por_caractere, descompactar_por_caractere
from huffman_palavra import compactar_por_palavra, descompactar_por_palavra
from huffman_teste import testar_arquivo
import os

def menu():
    while True:
        print("\n===== Menu Huffman =====")
        print("1 - Compactar por caractere")
        print("2 - Descompactar por caractere")
        print("3 - Compactar por palavra")
        print("4 - Descompactar por palavra")
        print("5 - Testar e gerar relatório de compressão (compactar por caractere e palavra)")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        if opcao == "5":
            nome_arquivo = input("Nome do arquivo para testar: ")
            if os.path.isfile(nome_arquivo):
                testar_arquivo(nome_arquivo)
            else:
                print("Arquivo não encontrado.")
            continue

        elif opcao not in ["1", "2", "3", "4", "5"]:
            print("Opcao invalida!")
            continue

        

        entrada = input("Nome do arquivo de entrada: ")
        saida = input("Nome do arquivo de saída: ")

        if opcao == "1":
            compactar_por_caractere(entrada, saida)
        elif opcao == "2":
            descompactar_por_caractere(entrada, saida)
        elif opcao == "3":
            compactar_por_palavra(entrada, saida)
        elif opcao == "4":
            descompactar_por_palavra(entrada, saida)
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
