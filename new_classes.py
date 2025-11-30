class membro_universidade:
    def __init__(self, nome, email, matricula):
        self.nome = nome
        self.email = email
        self.matricula = matricula

    def exibir_dados(self):
        print(f"\nNome: {self.nome}\nEmail: {self.email}\nMatrícula: {self.matricula}")

class disciplina:
    def __init__(self, codigo, descricao, periodo, carga_horaria, nome):
        self.codigo = codigo
        self.descricao = descricao
        self.periodo = periodo
        self.carga_horaria = carga_horaria
        self.nome = nome

    def exibir_dados(self):
        print(f"\nNome da Disciplina: {self.nome}\nCódigo: {self.codigo}\nDescrição: {self.descricao}\nPeríodo: {self.periodo}\nCarga Horária: {self.carga_horaria} horas")

class aluno(membro_universidade):
    def __init__(self, nome, email, matricula, coeficiente_rendimento):
        super().__init__(nome, email, matricula)
        self.matricula = matricula
        self.coeficiente_rendimento = coeficiente_rendimento

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Matrícula: {self.matricula}")


class professor(membro_universidade):
    def __init__(self, nome, email, matricula, departamento, titulacao, salario):
        super().__init__(nome, email, matricula)
        self.departamento = departamento
        self.titulacao = titulacao
        self.salario = salario

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Departamento: {self.departamento}\nTitulação: {self.titulacao}\nSalário: {self.salario}")