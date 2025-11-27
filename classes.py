class Membro_universidade:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_dados(self):
        print(f"\nNome: {self.nome}\nEmail: {self.email}")
    
class Estudante(Membro_universidade):
    def __init__(self, nome, email, curso, Coeficiente_rendimento):
        super().__init__(nome, email)
        self.curso = curso
        self.Coeficiente_rendimento = Coeficiente_rendimento
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Curso: {self.curso}")
        print(f"Coeficiente de Rendimento: {self.Coeficiente_rendimento:.2f}")
    
class Estagiario(Estudante):
    def __init__(self, nome, email, curso, Coeficiente_rendimento, empresa, duracao, valor_bolsa):
        super().__init__(nome, email, curso, Coeficiente_rendimento)
        self.empresa = empresa
        self.duracao = duracao
        self.valor_bolsa = valor_bolsa
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Empresa: {self.empresa}\nDuração: {self.duracao}")
        print(f"Valor da Bolsa: R$ {self.valor_bolsa:.2f}")

class Empregado(Membro_universidade):
    def __init__(self, nome, email, setor, salario, titulacao=None):
        super().__init__(nome, email)
        self.setor = setor
        self.salario = salario
        self.titulacao = titulacao

    def adicionar_bonus(self):
        salario_com_bonus = self.salario

        if self.titulacao == "Mestrado":
            salario_com_bonus += 2000
        elif self.titulacao == "Doutorado":
            salario_com_bonus += 5000

        return salario_com_bonus

class Professor(Empregado):
    def __init__(self, nome, email, setor, departamento, titulacao, salario):
        super().__init__(nome, email, setor, salario, titulacao)
        self.departamento = departamento
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Titulação: {self.titulacao}")
        print(f"Departamento: {self.departamento}")
        print(f"Salário: R$ {self.adicionar_bonus():.2f}")

class Pesquisador(Empregado):
    def __init__(self, nome, email, setor, area_pesquisa, salario, titulacao):
        super().__init__(nome, email, setor, salario, titulacao)
        self.area_pesquisa = area_pesquisa
    
    def exibir_dados(self):
        super().exibir_dados()
        print(f"Área de Pesquisa: {self.area_pesquisa}\nTitulação: {self.titulacao}")
        print(f"Salário: R$ {self.adicionar_bonus():.2f}")

# E = Estudante, P = Professor, R = Pesquisador, S = Estagiario

E1 = Estudante("João Vitor da Graça Américo", "joao.vitor@email.com", "Ciência da Computação", 0.46)
E2 = Estudante("Paulo César Souza Gomes", "paulo.cesar@email.com", "Engenharia de Software", 0.90)

S1 = Estagiario("Kauan da Rosa Paulino", "kauan.paulino@email.com", "Análise e Desenvolvimento de Sistemas", 1.0, "Google", "1 ano", 5500.00)
S2 = Estagiario("Bruno Matos Wada", "bruno.wada@email.com", "Engenharia de Computação", 0.99, "Microsoft", "6 meses", 4500.00)

P1 = Professor("Eduardo Fieppo", "eduardo.fieppo@email.com", "Educacional", "Informática", "Doutorado", 25000.00)
P2 = Professor("Izaque Esteves", "izaque.esteves@email.com", "Educacional", "Biologia", "Mestrado", 9999997999.99)

R1 = Pesquisador("João Paulo Orlando", "joao.orlando@email.com", "Pesquisa Acadêmica", "Computação Quântica", 30000.00, "Doutorado")
R2 = Pesquisador("Gabriel Cândido", "gabriel.candido@email.com", "Pesquisa Acadêmica", "Matemática Aplicada", 5000.00, "Graduado")