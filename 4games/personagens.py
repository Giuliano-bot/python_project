from random import randint

class personagem():

    def __init__(self, nome):
        self.nome = nome
        self.hp = 100
        self.xp = 0
        self.mp = 100
        self.atack = 
        self.esquiva = randint(1, 100)
        

    def subir_nivel(self):
        if self.xp > (99*self.nivel)
            self.nivel += 1
            print('level up')

    def ataque(self):
        while True:
            select = input( 'Selecione o monstro: \n1-minotauro\n2-mago')        
    

class mago(Personagem):
    def __init__(self):
        super().__init__(self)
        self.inteligencia = True
        self.mag_ataq = ' Magia das Trevas '
        self.poder_especial = 3 

    def recuperacao_mana(self):
        if self.poder_especial > 0:
            self.mp = 100
            print('mana recuperada')
            self.poder_especial -= 1



class guerreiro(personagem):

    def __init__(self):
        super()__init__(self)
        self.forca = True
        self.msg_atq = ' estocada violenta '
        self.poder_especial = 3

    def furia(self):
        if self.poder_especial > 0:
            if self.hp < 100:
                self.hp += self.hp + (self.hp * 0.10)


             else:
                 



     

