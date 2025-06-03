class livro:
    #definir aqui dentro o molde, que vao ser as caracteristicas e o comportamento
    def __init__(self, titulo, autor, numero_pagina):
    #metodo magico construtor init...temos o self pro metodo entender que 
    #ele precisa chamar ele mesmo
        self.titulo = titulo
        self.autor = autor
        self.numero_pagina = numero_pagina
        self.emprestado = False

    def emprestar(self):
        if not self.emprestado:
            self.emprestado = True
            return f'O livro {self.titulo} foi emprestado'
        return f'O livro {self.titulo} já esta emprestado'
    
    def devolver(self):
        if self.emprestado:
            self.emprestado = False
            return f'O livro {self.titulo} foi devolvido'
        return f'O livro {self.titulo} já esta disponivel'
    
class leitor:
    def __init__(self,nome):
        self.nome = nome #se atentar a identação
        self.livros_emprestados = [] #colchete esta criando uma lista, pq um leitor pode pegar mais de um livro
    
    def realizar_emprestimo(self,livro):
        if not livro.emprestado:
            self.livros_emprestados.append(livro)
            return livro.emprestar()
        return f'O livro {livro.titulo} não esta disponivel'
    
    def devolver_livro(self,livro,dias_atrasado):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            multa = max(0, (dias_atrasado-15) *2)
            #2 é o valor da multa por dia
            return livro.devolver() + f'multa: R$ {multa}'
        return f'O leitor {self.nome} não possui o livro {livro.titulo}'
        
class biblioteca:
    def __init__(self):
        self.livro=[]
        self.leitor=[]
    
    def adicionar_livro(self, livro):
        self.livro.append(livro)
        return f'O livro {livro} foi add a biblioteca'
    
    def remover_livro(self,livro):
        if livro in self.livro:
            self.livro.remove(livro)
            return f'O livro {livro} foi removido da biblioteca'
        return f'O livro {livro} nao esta na biblioteca'
    
    def emprestar_livro(self, livro, leitor):
        if livro in self.livro and not livro.emprestado:
            return leitor.realizar_emprestimo(livro)
        return f'O {livro.titulo} nao esta disponivel para emprestimo'
    
livro1 = livro ('Fundamentos POO', 'Ricardo', 500)
leitor1 = leitor ('Larissa')
biblioteca = biblioteca()

print(biblioteca.adicionar_livro(livro1))
print(biblioteca.emprestar_livro(livro1,leitor1))
print(leitor1.devolver_livro(livro1, dias_atrasado=20))
