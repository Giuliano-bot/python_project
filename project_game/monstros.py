from personagens import personagem
from random import randint

class monstro(Personagem):

    def __init__(self):
        personagem.__init__(self)
        forca = randint(1, 100)


class minotauro(monstro):

    def __init__(self):
        monstro.__init__(self)
        msg_atq = 'Chifrada Sangrenta'

class orc(monstro):





