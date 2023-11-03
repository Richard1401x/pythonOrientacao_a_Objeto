class Pessoa:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.falando = False
        self.dormindo = False

    def comer(self):
        if self.comendo == True:
            print(f'{self.nome} ja esta comendo.')
        elif self.dormindo == True:
            print(f'{self.nome} não pode comer, pois está dormindo.')
        elif self.falando == True:
            print(f'{self.nome} é educado, então não pode falar comendo.')
        else:
            print(f'{self.nome} começou a comer.')
            self.comendo = True

    def parar_comer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer.')
            self.comendo = False
        else:
            print(f'{self.nome} não esta comendo!')


    def falar(self):
        if self.falando == True:
            print(f'{self.nome} ja esta falando.')
        elif self.comendo == True:
            print(f'{self.nome} não consegue falar comendo.')
        elif self.dormindo == True:
             print(f'{self.nome} não pode falar pois esta dormindo.')
        else:
            print(f'{self.nome} comecou a falar.')
            self.falando = True

    def parar_falar(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer.')
            self.comendo = False
        else:
            print(f'{self.nome} já esta calado!')

    def dormir(self):
        if self.dormindo == True:
            print(f'{self.nome} ja esta dormindo.')
        elif self.comendo == True:
            print(f'{self.nome} não consegue dormir no meio da comida.')
        elif self.falando == True:
            print(f'{self.nome} precisa parar de falar para começar a dormir.')
        else:
            print(f'{self.nome} foi dormir.')

    def acordar(self):
        if self.dormindo == True:
            print(f'{self.nome} acordou!')
        else:
            print(f'Mais acordado que tá, não da pra {self.nome} ficar!')

class banco:
    def __init__(self,numero, nome, tipo):
        self.numero = numero
        self.saldo = 0.00
        self.nome = nome
        self.tipo = tipo
        self.status = False
        self.limite = 1000

    def ativarlimite (self,):
        if self.limite:
            print (f'{self.nome} Seu Limite de Crédito foi liberado!')
            print(f'Saldo anterior R${self.saldo:.2f}')
            calc = self.saldo + self.limite
            print(f'Seu novo saldo R${calc:.2f}')
    def depositar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui uma conta ativa.')
        if valor > 0:
            print(f'Saldo anterior = {self.saldo:.2f}')
            self.saldo += valor
            print(f'Seu novo saldo é {self.saldo:.2f}')
        else:
            print('Valor inválido.')

    def sacar(self,valor):
        if self.status == False:
            print(f'{self.nome} não possui uma conta ativa.')
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            soma = (self.saldo+self.limite)-valor

            print(f'Você sacou {valor:.2f}, seu novo saldo é de {soma:.2f}')
        else:
            print('Saldo insuficiente.')
    def ativarconta(self):
        if self.status == False:
            print(f'{self.nome}, sua conta foi ativada')
            self.status = True
        else:
            print('Sua conta já está ativada')
    def verificarsaldo(self):
        if self.status == False:
            print(f'{self.nome} não possui uma conta ativa.')
        else:
            self.saldo
            print(f'Você tem R${self.saldo:.2f} ')


class Animal ():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer (self):
        print(f'o {self.nome} foi comer...')
    def emitirsom(self):
        print(f'Seu gatinho {self.nome} está miando')

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
        print(f'Meu gatinho {nome}')
    def emitirsom(self):
        print('Miauu, Miauuu, Miauuu')
    def comer(self):
        print('Foi comer sua ração')

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
        print(f'Meu Cachorro {nome}')
    def emitirsom(self):
        print('Au, Au, Au, Au')
    def comer(self):
        print('Ama seus petiscos')

class Coelho(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
        print(f"Minha Coelha {nome}")
    def emitirsom(self):
        print('ronronando')
    def comer(self):
        print('Está comendo seu capim favorito')
class Vaca(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
        print(f'A vaca {nome}')
    def emitirsom(self):
        print('Muuuuu,Muuuuuu, Muuuuuuu')
    def comer(self):
        print('Come muito capim')

class Forma ():
    def __init__(self):
        self.area = 0.0
        self.perimetro = 0.0

class retangulo(Forma):
    def __init__(self, base, altura):
        super().__init__(base, altura)
        calcularAre = (base*altura)/2
    def calcularArea(self, base, altura):
        self.area = (base*altura)

class triangulo:
    def __init__(self, base,altura):
        super().__init__(base,altura)
        caculaPerimetro = (base*altura)/2
        print(f'O perimetro é {caculaPerimetro}')







