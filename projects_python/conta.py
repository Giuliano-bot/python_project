class conta():

    def __init__(self, nome_banco, numero_conta, numero_agencia, nome_cliente ):

              

        self.bancos = nome_banco
        self.conta = numero_conta
        self.agencia = numero_agencia
        self.cliente = nome_cliente 
        self.saldo = 0

        self.clientes = ['Maria', 'João']
        self.banco = ['Bradesco','Itau','Safra']
        self.conta_cli= ['01','02', '03']
        self.agencia_cli = ['01', '02', '03']
        

    def validação(self):

        if nome_banco in self.banco:
            pass

        elif numero_conta in self.conta_cli:
            pass

        elif numero_agencia in self.agencia_cli:
            pass

        elif nome_cliente in self.clientes:
            pass

    def servicos(self):     
        self.serv = input('Você Gostaria de Sacar ou Depositar ?: ')
        self.serv1 = self.serv.lower()

        if self.serv1 == 'sacar':                                
            self.sacar = int(input('Qual valor ?: '))        
            while self.sacar > self.saldo:
                self.stop = float(input(f'Seu saldo atual é de {self.saldo},\n Digite o VALOR igual ou MENOR que o seu saldo! >>> '))

            else: 
                self.saldo_atual = self.saldo - self.sacar
                print(f'Você sacou {self.sacar}\nSeu saldo anterior: {self.saldo_atual}')                    
    
        if self.serv1 == 'depositar':
            
            self.deposito = float(input('Digite o valor do Depósito'))
            while self.deposito <= 0:
                self.stop1 = float(input(f'Seu saldo atual é de {self.saldo},\n Digite o VALOR igual ou MENOR que o seu saldo! >>> '))
            else:
                self.saldo_atual2 = self.deposito + self.saldo 
                print(f'Você depositou {self.deposito}\n Seu saldo Atual: {self.saldo_atual2}')

caramba = conta('Bradesco', 1, 2, 'Maria')
caramba.servicos()
                           

                


                







    
        
         




        

   

      