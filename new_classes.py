class membro_universidade:
    def __init__(self, nome, email, matricula):
        self.nome = nome
        self.email = email
        self.__matricula = matricula

    def exibir_dados(self):
        print("\nDados do membro")
        print("Nome:", self.nome)
        print("Email:", self.email)
        print("Matricula:", self.__matricula)


class disciplina:
    def __init__(self, codigo, descricao, periodo, carga_horaria, nome):
        self.codigo = codigo
        self.descricao = descricao
        self.periodo = periodo
        self.carga_horaria = carga_horaria
        self.nome = nome

    def exibir_dados(self):
        print("\nDados da disciplina")
        print("Nome:", self.nome)
        print("Codigo:", self.codigo)
        print("Descricao:", self.descricao)
        print("Periodo:", self.periodo)
        print("Carga horaria:", self.carga_horaria)


class aluno(membro_universidade):
    def __init__(self, nome, email, matricula, coeficiente_rendimento):
        super().__init__(nome, email, matricula)
        self.coeficiente_rendimento = coeficiente_rendimento

    def exibir_dados(self):
        super().exibir_dados()
        print("Coeficiente de rendimento:", self.coeficiente_rendimento)


class professor(membro_universidade):
    def __init__(self, nome, email, matricula, departamento, titulacao, salario):
        super().__init__(nome, email, matricula)
        self.departamento = departamento
        self.titulacao = titulacao
        self.salario = salario

    def exibir_dados(self):
        super().exibir_dados()
        print("Departamento:", self.departamento)
        print("Titulacao:", self.titulacao)
        try:
            valor = float(self.salario)
            brl = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except (ValueError, TypeError):
            brl = str(self.salario)
        print("Salario: R$ " + brl)
        # Teste commit branch

membro_generico = membro_universidade("João Silva", "joao.silva@uni.br", "12345")

disciplina_poo = disciplina("SI001", "Programação Orientada a Objetos", "2024.1", "60h", "POO")


aluno_exemplo = aluno("Maria Souza", "maria.souza@aluno.br", "2024001", 8.5)

professor_exemplo = professor(
    "Dr. Carlos Lima",
    "carlos.lima@prof.br",
    "P9876",
    "Ciência da Computação",
    "Doutorado",
    8500.75
)

print("--- Testando as Instâncias ---")
membro_generico.exibir_dados()
disciplina_poo.exibir_dados()
aluno_exemplo.exibir_dados()
professor_exemplo.exibir_dados()
print("------------------------------")