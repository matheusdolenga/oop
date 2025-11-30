import sqlite3
from new_classes import membro_universidade
import database
import time


conn = sqlite3.connect('universidade.db')
cursor = conn.cursor()

def create():
    cursor.execute("INSERT INTO membro_univerisade (nome, email, matricula) VALUES (?, ?, ?)", (membro_universidade.nome,membro_universidade.email, membro_universidade.matricula))
    conn.commit()

def read():
    cursor.execute("SELECT * FROM membro_univerisade WHERE matricula = ?", (membro_universidade.matricula,))
    result = cursor.fetchone()

def update():
    cursor.execute("UPDATE membro_univerisade SET nome = ?, email = ? WHERE matricula = ?", (membro_universidade.nome, membro_universidade.email, membro_universidade.matricula))
    conn.commit()

def delete():
    cursor.execute("DELETE FROM membro_univerisade WHERE matricula = ?", (membro_universidade.matricula,))
    conn.commit()

def interface():
    print("Bem-vindo ao sistema de gerenciamento da universidade!")
    print("Selecione a operação desejada:\n 1. Cadastrar novo membro\n 2. Visualizar dados de um membro\n 3. Atualizar dados de um membro\n 4. Deletar um membro\n 5. Sair")

    match input("Digite o número da operação desejada: "):
        case '1':
                print("Cadastro de novo membro selecionado.")
                print('isira primeiro o nome, depois o email, depois a matrícula:')
                create()
        case '2':
                print("Visualização de dados selecionada.")
                print('isira a matrícula do membro:')
                read()
        case '3':
                print("Atualização de dados selecionada.")
                print('isira primeiro o nome, depois o email, depois a matrícula:')
                update()
        case '4':
                print("Deleção de membro selecionada.")
                print('isira a matrícula do membro:')
                delete()
        case '5':
                print("Encerrando o programa")
                time.sleep(2)
                exit()
        case _:
            print("Operação inválida. Por favor, tente novamente.")

def main():
    interface()

if __name__ == "__main__":
    main()