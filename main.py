import sqlite3
import database
from new_classes import aluno, disciplina, membro_universidade, professor


def menu_membros():
    while True:
        print("\n1 - Cadastrar membro")
        print("2 - Ver um membro")
        print("3 - Atualizar membro")
        print("4 - Deletar membro")
        print("5 - Voltar")
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            matricula = input("Matricula: ").strip()
            if not nome or not email or not matricula:
                print("Preencha todos os campos.")
                continue
            try:
                database.criar_membro(nome, email, matricula)
                print("Membro salvo com sucesso.")
            except sqlite3.IntegrityError:
                print("Ja existe um membro com essa matricula.")

        elif opcao == "2":
            matricula = input("Matricula do membro: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            dados = database.buscar_membro(matricula)
            if not dados:
                print("Nenhum membro encontrado.")
            else:
                membro = membro_universidade(*dados)
                membro.exibir_dados()

        elif opcao == "3":
            matricula = input("Matricula do membro: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            atual = database.buscar_membro(matricula)
            if not atual:
                print("Nenhum membro encontrado.")
                continue
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            if not nome or not email:
                print("Nome e email nao podem ser vazios.")
                continue
            linhas = database.atualizar_membro(nome, email, matricula)
            if linhas:
                print("Dados atualizados.")
            else:
                print("Nada foi atualizado.")

        elif opcao == "4":
            matricula = input("Matricula do membro: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            linhas = database.deletar_membro(matricula)
            if linhas:
                print("Membro removido.")
            else:
                print("Nenhum membro encontrado.")

        elif opcao == "5":
            break
        else:
            print("Opcao invalida, tente de novo.")


def menu_alunos():
    while True:
        print("\n1 - Cadastrar aluno")
        print("2 - Ver um aluno")
        print("3 - Atualizar aluno")
        print("4 - Deletar aluno")
        print("5 - Voltar")
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            matricula = input("Matricula: ").strip()
            coef = input("Coeficiente de rendimento: ").strip()
            if not matricula or not coef:
                print("Preencha todos os campos.")
                continue
            try:
                coef_valor = float(coef)
            except ValueError:
                print("Coeficiente deve ser numerico.")
                continue
            try:
                if not database.buscar_membro(matricula):
                    print("Cadastre primeiro o membro com essa matricula.")
                    continue
                database.criar_aluno(matricula, coef_valor)
                print("Aluno salvo com sucesso (dados herdados do membro).")
            except sqlite3.IntegrityError:
                print("Ja existe um aluno com essa matricula ou membro nao existe.")

        elif opcao == "2":
            matricula = input("Matricula do aluno: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            dados = database.buscar_aluno(matricula)
            if not dados:
                print("Nenhum aluno encontrado.")
            else:
                aluno_obj = aluno(*dados)
                aluno_obj.exibir_dados()

        elif opcao == "3":
            matricula = input("Matricula do aluno: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            atual = database.buscar_aluno(matricula)
            if not atual:
                print("Nenhum aluno encontrado.")
                continue
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            coef = input("Novo coeficiente de rendimento: ").strip()
            if not nome or not email or not coef:
                print("Campos nao podem ser vazios.")
                continue
            try:
                coef_valor = float(coef)
            except ValueError:
                print("Coeficiente deve ser numerico.")
                continue
            linhas = database.atualizar_aluno(nome, email, coef_valor, matricula)
            if linhas:
                print("Dados do aluno atualizados.")
            else:
                print("Nada foi atualizado.")

        elif opcao == "4":
            matricula = input("Matricula do aluno: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            linhas = database.deletar_aluno(matricula)
            if linhas:
                print("Aluno removido (membro permanece cadastrado).")
            else:
                print("Nenhum aluno encontrado.")

        elif opcao == "5":
            break
        else:
            print("Opcao invalida, tente de novo.")


def menu_professores():
    while True:
        print("\n1 - Cadastrar professor")
        print("2 - Ver um professor")
        print("3 - Atualizar professor")
        print("4 - Deletar professor")
        print("5 - Voltar")
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            matricula = input("Matricula: ").strip()
            departamento = input("Departamento: ").strip()
            titulacao = input("Titulacao: ").strip()
            salario = input("Salario: ").strip()
            if (
                not matricula
                or not departamento
                or not titulacao
                or not salario
            ):
                print("Preencha todos os campos.")
                continue
            try:
                salario_valor = float(salario)
            except ValueError:
                print("Salario deve ser numerico.")
                continue
            try:
                if not database.buscar_membro(matricula):
                    print("Cadastre primeiro o membro com essa matricula.")
                    continue
                database.criar_professor(
                    matricula, departamento, titulacao, salario_valor
                )
                print("Professor salvo com sucesso (dados herdados do membro).")
            except sqlite3.IntegrityError:
                print("Ja existe um professor com essa matricula ou membro nao existe.")

        elif opcao == "2":
            matricula = input("Matricula do professor: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            dados = database.buscar_professor(matricula)
            if not dados:
                print("Nenhum professor encontrado.")
            else:
                prof = professor(*dados)
                prof.exibir_dados()

        elif opcao == "3":
            matricula = input("Matricula do professor: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            atual = database.buscar_professor(matricula)
            if not atual:
                print("Nenhum professor encontrado.")
                continue
            nome = input("Novo nome: ").strip()
            email = input("Novo email: ").strip()
            departamento = input("Novo departamento: ").strip()
            titulacao = input("Nova titulacao: ").strip()
            salario = input("Novo salario: ").strip()
            if (
                not nome
                or not email
                or not departamento
                or not titulacao
                or not salario
            ):
                print("Campos nao podem ser vazios.")
                continue
            try:
                salario_valor = float(salario)
            except ValueError:
                print("Salario deve ser numerico.")
                continue
            linhas = database.atualizar_professor(
                nome, email, departamento, titulacao, salario_valor, matricula
            )
            if linhas:
                print("Dados do professor atualizados.")
            else:
                print("Nada foi atualizado.")

        elif opcao == "4":
            matricula = input("Matricula do professor: ").strip()
            if not matricula:
                print("Matricula nao pode ser vazia.")
                continue
            linhas = database.deletar_professor(matricula)
            if linhas:
                print("Professor removido (membro permanece cadastrado).")
            else:
                print("Nenhum professor encontrado.")

        elif opcao == "5":
            break
        else:
            print("Opcao invalida, tente de novo.")


def menu_disciplinas():
    while True:
        print("\n1 - Cadastrar disciplina")
        print("2 - Ver uma disciplina")
        print("3 - Atualizar disciplina")
        print("4 - Deletar disciplina")
        print("5 - Voltar")
        opcao = input("Opcao: ").strip()

        if opcao == "1":
            codigo = input("Codigo: ").strip()
            descricao = input("Descricao: ").strip()
            periodo = input("Periodo: ").strip()
            carga = input("Carga horaria: ").strip()
            nome = input("Nome da disciplina: ").strip()
            if not codigo or not descricao or not periodo or not carga or not nome:
                print("Preencha todos os campos.")
                continue
            try:
                carga_valor = int(carga)
            except ValueError:
                print("Carga horaria deve ser numerica.")
                continue
            try:
                database.criar_disciplina(
                    codigo, descricao, periodo, carga_valor, nome
                )
                print("Disciplina salva com sucesso.")
            except sqlite3.IntegrityError:
                print("Ja existe uma disciplina com esse codigo.")

        elif opcao == "2":
            codigo = input("Codigo da disciplina: ").strip()
            if not codigo:
                print("Codigo nao pode ser vazio.")
                continue
            dados = database.buscar_disciplina(codigo)
            if not dados:
                print("Nenhuma disciplina encontrada.")
            else:
                disc = disciplina(*dados)
                disc.exibir_dados()

        elif opcao == "3":
            codigo = input("Codigo da disciplina: ").strip()
            if not codigo:
                print("Codigo nao pode ser vazio.")
                continue
            atual = database.buscar_disciplina(codigo)
            if not atual:
                print("Nenhuma disciplina encontrada.")
                continue
            descricao = input("Nova descricao: ").strip()
            periodo = input("Novo periodo: ").strip()
            carga = input("Nova carga horaria: ").strip()
            nome = input("Novo nome: ").strip()
            if not descricao or not periodo or not carga or not nome:
                print("Campos nao podem ser vazios.")
                continue
            try:
                carga_valor = int(carga)
            except ValueError:
                print("Carga horaria deve ser numerica.")
                continue
            linhas = database.atualizar_disciplina(
                codigo, descricao, periodo, carga_valor, nome
            )
            if linhas:
                print("Disciplina atualizada.")
            else:
                print("Nada foi atualizado.")

        elif opcao == "4":
            codigo = input("Codigo da disciplina: ").strip()
            if not codigo:
                print("Codigo nao pode ser vazio.")
                continue
            linhas = database.deletar_disciplina(codigo)
            if linhas:
                print("Disciplina removida.")
            else:
                print("Nenhuma disciplina encontrada.")

        elif opcao == "5":
            break
        else:
            print("Opcao invalida, tente de novo.")


def menu():
    database.init_db()
    print("Bem-Vindo ao sistema de integrantes do IFPR!!")
    print("Escolha uma opcao e siga as instrucoes.")

    while True:
        print("\n1 - Membros")
        print("2 - Alunos")
        print("3 - Professores")
        print("4 - Disciplinas")
        print("5 - Sair")
        opcao = input("Opcao: ").strip()

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