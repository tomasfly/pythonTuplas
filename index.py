# -*- coding: utf-8 -*-
###### 1 
palos = 'pica', 'corazon', 'rombo', 'trebol'
cartas = 0,1,2,3,4,5,6,7,8,9,10,11,12,13
tmatrix = palos,cartas

diezDePica = tmatrix[0][0],tmatrix[1][10]
diezDeCorazon = tmatrix[0][1],tmatrix[1][10]
diezDeRombo = tmatrix[0][2],tmatrix[1][10]
diezDeTrebol = tmatrix[0][3],tmatrix[1][10]

# class implementation
class Cartas:
    def __init__(self, carta):
        self.carta = carta
As = Cartas('As')

class Palos:
    def __init__(self, palo):
        self.palo = palo
Pica = Palos('Pica')

###### 2
jugada = (diezDePica,diezDeCorazon,diezDeRombo,diezDeTrebol)
class Poker:
    def __init__(self, cartas):
        self.cartas = cartas
    def isPoker(self):
        cartasLen = len(self.cartas)
        numeros = []
        for var in self.cartas:
            res = var[1]
            numeros.append(var[1])
        print(numeros)
        return len(set(numeros)) <= 1        
Poker = Poker(jugada)
print(Poker.isPoker())