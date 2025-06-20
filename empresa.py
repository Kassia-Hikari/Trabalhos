class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_pagamento(self):
        return self.salario 
    #retorna o salario do funcionario (Sem bonus ou horas extras)

class Gerente(Funcionario):
    def __init__(self, nome, salario, cargo, bonus):
        #chama o metodo init da classe pai (funcionario) usando o super()
        super().__init__(nome, salario, cargo)
        #add um atributo especifico para gerente: bonus
        self.bonus = bonus 
    
    def calcular_pagamento(self):
        #calcula o pagamento incluindo o bonus do gerente
        return self.salario + self.bonus
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, cargo, horas_extras=0, valor_hora_extra=0):
        #chama o metodo init da classe pai (funcioanario)
        super().__init__(nome, salario, cargo)
        #add atributos especificos para desenvolvedores: horas extras e valor hora extra
        self.hora_extras = horas_extras
        self.valor_hora_extra = valor_hora_extra

    def calcular_pagamento(self):
        #calcula o pagamento incluindo a hora extra
        return self.salario + (self.hora_extras * self.valor_hora_extra)

class SistemaEmpresa:
    def __init__(self):
        #inicializa uma lista de funcionarios
        self.funcionarios = []

    def add_func(self, funcionario):
        #add um funcionario a lista
        self.funcionarios.append(funcionario)

    def processar_pagamento(self):
        #processa os pagamentos de todos os funcionarios cadastrados
        for funcioanario  in self.funcionarios:
            print(f'Pagamento de {funcioanario.nome}: R${funcioanario.calcular_pagamento():.2f}')

#criando instancia de funcionarios
kassia = Gerente('Kassia', 8000, 'Gerente de Projetos', 2000)
hikari = Desenvolvedor('Hikari', 5000, 'Dev', horas_extras=10, valor_hora_extra=50)

#mostrar info dos funcionarios
print(kassia.__dict__)
print(hikari.__dict__)

#criando sistema e add funcioanarios
sistema = SistemaEmpresa()
sistema.add_func(kassia)
sistema.add_func(hikari)

#processando pagamentos
sistema.processar_pagamento()



