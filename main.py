import database
from new_classes import aluno, disciplina, membro_universidade, professor


def menu_membros():
    while True:
        print("\n1 - Cadastrar membro\n2 - Ver um membro\n3 - Atualizar membro\n4 - Deletar membro\n5 - Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            try:
                database.criar_membro(
                    input("Nome: "),
                    input("Email: "),
                    input("Matricula: "),
                )
                print("Membro salvo.")
            except Exception as e:
                print("Erro ao salvar:", e)

        elif opcao == "2":
            dados = database.buscar_membro(input("Matricula: "))
            if dados:
                membro_universidade(*dados).exibir_dados()
            else:
                print("Nao encontrado.")

        elif opcao == "3":
            database.atualizar_membro(
                input("Novo nome: "),
                input("Novo email: "),
                input("Matricula: "),
            )
            print("Dados atualizados.")

        elif opcao == "4":
            database.deletar_membro(input("Matricula: "))
            print("Membro removido.")

        elif opcao == "5":
            break


def menu_alunos():
    while True:
        print("\n1 - Cadastrar aluno\n2 - Ver um aluno\n3 - Atualizar aluno\n4 - Deletar aluno\n5 - Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            try:
                database.criar_aluno(
                    input("Matricula: "),
                    float(input("Coeficiente de rendimento: ")),
                )
                print("Aluno salvo.")
            except Exception as e:
                print("Erro ao salvar:", e)

        elif opcao == "2":
            dados = database.buscar_aluno(input("Matricula: "))
            if dados:
                aluno(*dados).exibir_dados()
            else:
                print("Nao encontrado.")

        elif opcao == "3":
            try:
                database.atualizar_aluno(
                    input("Novo nome: "),
                    input("Novo email: "),
                    float(input("Novo coeficiente: ")),
                    input("Matricula: "),
                )
                print("Aluno atualizado.")
            except Exception as e:
                print("Erro ao atualizar:", e)

        elif opcao == "4":
            database.deletar_aluno(input("Matricula: "))
            print("Aluno removido (membro permanece).")

        elif opcao == "5":
            break


def menu_professores():
    while True:
        print("\n1 - Cadastrar professor\n2 - Ver um professor\n3 - Atualizar professor\n4 - Deletar professor\n5 - Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            try:
                database.criar_professor(
                    input("Matricula: "),
                    input("Departamento: "),
                    input("Titulacao: "),
                    float(input("Salario: ")),
                )
                print("Professor salvo.")
            except Exception as e:
                print("Erro ao salvar:", e)

        elif opcao == "2":
            dados = database.buscar_professor(input("Matricula: "))
            if dados:
                professor(*dados).exibir_dados()
            else:
                print("Nao encontrado.")

        elif opcao == "3":
            try:
                database.atualizar_professor(
                    input("Novo nome: "),
                    input("Novo email: "),
                    input("Novo departamento: "),
                    input("Nova titulacao: "),
                    float(input("Novo salario: ")),
                    input("Matricula: "),
                )
                print("Professor atualizado.")
            except Exception as e:
                print("Erro ao atualizar:", e)

        elif opcao == "4":
            database.deletar_professor(input("Matricula: "))
            print("Professor removido (membro permanece).")

        elif opcao == "5":
            break


def menu_disciplinas():
    while True:
        print("\n1 - Cadastrar disciplina\n2 - Ver uma disciplina\n3 - Atualizar disciplina\n4 - Deletar disciplina\n5 - Voltar")
        opcao = input("Opcao: ")

        if opcao == "1":
            try:
                database.criar_disciplina(
                    input("Codigo: "),
                    input("Descricao: "),
                    input("Periodo: "),
                    int(input("Carga horaria: ")),
                    input("Nome da disciplina: "),
                )
                print("Disciplina salva.")
            except Exception as e:
                print("Erro ao salvar:", e)

        elif opcao == "2":
            dados = database.buscar_disciplina(input("Codigo: "))
            if dados:
                disciplina(*dados).exibir_dados()
            else:
                print("Nao encontrada.")

        elif opcao == "3":
            try:
                database.atualizar_disciplina(
                    input("Codigo: "),
                    input("Nova descricao: "),
                    input("Novo periodo: "),
                    int(input("Nova carga horaria: ")),
                    input("Novo nome: "),
                )
                print("Disciplina atualizada.")
            except Exception as e:
                print("Erro ao atualizar:", e)

        elif opcao == "4":
            database.deletar_disciplina(input("Codigo: "))
            print("Disciplina removida.")

        elif opcao == "5":
            break


def menu():
    database.init_db()
    print("Bem-Vindo ao sistema de integrantes do IFPR!!")
    print("Escolha uma opcao e siga as instrucoes.")

    while True:
        print("\n1 - Membros\n2 - Alunos\n3 - Professores\n4 - Disciplinas\n5 - Sair")
        opcao = input("Opcao: ")

        if opcao == "1":
            menu_membros()
        elif opcao == "2":
            menu_alunos()
        elif opcao == "3":
            menu_professores()
        elif opcao == "4":
            menu_disciplinas()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opcao invalida, tente de novo.")


if __name__ == "__main__":
    menu()
