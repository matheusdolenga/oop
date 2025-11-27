import sqlite3
import classes
import database
import time

def create():
    pass

def read():
    pass

def update():
    pass

def delete():
    pass

def interface():
    print("Bem-vindo ao sistema de gerenciamento da universidade!")
    print("Selecione a operação desejada:\n 1. Cadastrar novo membro\n 2. Visualizar dados de um membro\n 3. Atualizar dados de um membro\n 4. Deletar um membro\n 5. Sair")

    match input("Digite o número da operação desejada: "):
        case '1':
                print("Cadastro de novo membro selecionado.")
        case '2':
                print("Visualização de dados selecionada.")
        case '3':
                print("Atualização de dados selecionada.")
        case '4':
                print("Deleção de membro selecionada.")
        case '5':
                print("Encerrando o programa")
                time.sleep(2)
                exit()
        case _:
            print("Operação inválida. Por favor, tente novamente.")


def main():
    # inicia = sqlite3.connect('universidade.db')
    # cursor = inicia.cursor()

    interface()

if __name__ == "__main__":
    main()