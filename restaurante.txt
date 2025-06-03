class Restaurante:
    def __init__(self):
        self.cardapio = {} #dicionario = porque queremos que os clientes chamem o nome do prato
        self.comanda = {}
    
    def adicionar_prato(self):
        nome = input("nome do prato: ")
        preco = float(input("Preço: "))
        self.cardapio[nome] = preco
        print(f"{nome} foi adicionado ao sistema")

    def remover_prato(self):
       nome = input('Qual prato deseja remover do cardapio? ')
       if nome in self.cardapio:
            del self.cardapio[nome]
            print(f" O {nome} foi removido do cardapio")
       else:
            print("Esse prato nao esta no cardapio")
 
    def atualizar_preco(self):
        nome = input("Nome do prato que deseja atualizar: ")
        if nome in self.cardapio:
            novo_preco = float(input("Novo preço: "))
            self.cardapio[nome] = novo_preco
            print(f"O preço de {nome} foi atualizado para R${novo_preco:.2f}")
        else:
            print("Esse prato não está no cardápio.")

    def abrir_comanda(self):
        numero = int(input("insira numero da comanda: "))
        if numero in self.comanda:
            print("Comanda já existente")
            return
        self.comanda[numero]={"pratos":[], "total":0, "status":"aberta"}
        print(f"comanda {numero} aberta")
        
    def adicionar_pedido(self):
        numero= int(input("insira o numero da comanda: "))
        if numero not in self.comanda:
            print("comanda não encontrada")
            return
        print("Cardapio disponivel: ")
        for nome, preco in self.cardapio.items():
            print(f"{nome}, R${preco:.2f}")
        
        prato = input("nome do prato para adicionar: ")
        if prato in self.cardapio:
            self.comanda[numero]["pratos"].append(prato)    
            self.comanda[numero]["total"]+=self.cardapio[prato]
            self.comanda[numero]["status"]='sendo preparado'
            print(f"{prato} adicionado a comanda {numero}")
        else:
            print("Prato não esta no cardapio")

    def pagamento(self, numero):
        if numero not in self.comanda:
           print("comanda nao encontrada")
           return
        print("Qual a forma de pagamento desejada? ")
        print("1 - dinheiro ")
        print("2 - Cartao de Credito ")
        print("3 - Cartao de Debito ")
        print("4 - Pix")  
        opcao = input("Escolha uma opçao: ")

        forma_de_pagamento = {
           "1":"dinheiro",
           "2":"Cartao de Credito",
           "3":"Cartao de Debito",
           "4":"Pix"
        }
        if opcao in forma_de_pagamento:
           self.comanda[numero]['forma_de_pagamento'] = forma_de_pagamento[opcao]
           print(f"Forma de pagamento escolhida: {self.comanda[numero]['forma_de_pagamento']}")
        else:
           print("Opção invalida")

    def verificar_pedido(self):
        numero=int(input("numero da comanda: "))
        if numero not in self.comanda:
            print("comanda não encontrada")
            return 
        print(f"conta da comanda {numero} fechada")
        print(f"Status: {self.comanda[numero]}")
        print(f"total: R$ {self.comanda[numero]['total']}") 
    
    def receber_pagamento(self, numero_comanda):
        if numero_comanda not in self.comanda:
            print("Comanda nao encontrda")
            return
        
        self.pagamento(numero_comanda)
        print(f"Pagamento realizado via {self.comanda[numero_comanda]['forma_de_pagamento']}")

    def fechar_conta(self):
        numero=int(input("numero da comanda"))
        if numero not in self.comanda:
            print("comanda não encontrada")
            return 
        
        if self.comanda[numero]["status"] == 'aberta':
            print("o pedido esta em preparo")
            return
        
        print(f"conta da comanda {numero} fechada")
        print(f"total a pagar: R${self.comanda[numero]['total']}")
        del self.comanda[numero]


restaurante = Restaurante()

while True:
    print("1 adicionar ao cardapio" )
    print('2 remover do cardapio' )
    print("3 Atualizar item do cardapio ")
    print("4 abrir comanda")
    print("5 adicionar pedido")
    print("6 verificar pedido")
    print("7 Escolher forma de pagamento: ")
    print("8 realizar pagamento")
    print("9 fechar conta")
    print("10 sair")
    opcao=input("escolha uma opção: ")
    if opcao == "1":
      restaurante.adicionar_prato()
    elif opcao == "2":
     restaurante.remover_prato()
    elif opcao == "3":
     restaurante.atualizar_preco()
    elif opcao == "4":
     restaurante.abrir_comanda()
    elif opcao == "5":    
     restaurante.adicionar_pedido()
    elif opcao == "6":
     restaurante.verificar_pedido()
    elif opcao == "7":
     numero_comanda = int(input("Digite o numeor da sua comanda: "))
     restaurante.pagamento(numero_comanda)
    elif opcao == "8":
     restaurante.receber_pagamento()
    elif opcao == "9":
     restaurante.fechar_conta()
    elif opcao == "10":
     print("saindo")
     break
    else:
     print("opçao incorreta")